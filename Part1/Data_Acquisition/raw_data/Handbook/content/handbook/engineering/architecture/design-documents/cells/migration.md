---
title: 'Cells: Organization migration'
status: proposed
creation-date: "2024-05-01"
authors: [ "@dbalexandre", "@mkozono" ]
coach: [ "@ayufan" ]
dris: [ "@sranasinghe", "@luciezhao" ]
approvers: [ "@sranasinghe", "@luciezhao" ]
owning-stage: "~devops::systems"
participating-stages: ["~devops::data stores", "~devops::systems"]
toc_hide: true
---

## Summary

When we reach production and can operate organizations on new [cells](../cells), we need to be able to move [organizations](https://docs.gitlab.com/ee/user/organization/) from GitLab.com into a cell or between any two cells. [The Org Mover project](https://gitlab.com/groups/gitlab-org/-/epics/12857) provides a CLI orchestrator tool that makes the process of moving organization data from one cell to another a breeze. It's designed to ensure no data loss or corruption with minimal downtime.

It is important to note that the tool itself isn't responsible for moving data, but it takes care of setting up all the required logistics. It will be developed as a gem within the [gitlab-org/gitlab](https://gitlab.com/gitlab-org/gitlab) codebase.

## Motivation

Org Mover will allow organizations to be moved to our scalable cells architecture, future-proofing our GitLab.com services as GitLab grows. This way, we guarantee that we will be able to deliver a consistently excellent service for our GitLab.com customers with all the advantages that come with the cells architecture.

### Goals

- Move organizations off GitLab.com or between Cells to rebalance them with minimal downtime:
  - Maximum downtime requirements for moving an organization and cutting it over to the target cell are as follows:
    - Cells 1.5 - 24 hours
    - Cells 2.0 - Ideally 0. Low enough to not have to coordinate the migration with them.
  - Reuse Geo code to replicate non-PostgreSQL data continuously for a particular organization.
  - Implement a reliable and scalable tool to copy all PostgreSQL data for a particular organization from the source database and writes it to the target database present in another cell.
  - Create the Org mover CLI orchestrator tool that will:
    - Set up and manage the replication of non-PostgreSQL data for a particular organization.
    - Put an organization into a maintenance mode.
    - Start the PostgreSQL data copy.
    - Handle tables exempt from sharding.
    - Handle the ElasticSearch and Zoekt data.
    - Rebuild the ClickHouse data.
    - Monitor the replication process.
    - Perform the switchover.
    - Remove all organization data that has been moved over.
  - Implement robust error handling and monitoring to quickly identify and resolve any issues in the data synchronization process.
- Ensure there's no data loss or corruption during the move. The process must ensure that all data at the source cell is copied to the target cell.
- Ensure the process for moving data from one cell to another is timely and allows for reasonable throughput. Moving many organizations simultaneously shouldn't put undue strain on the infrastructure.
- Ensure there is no downtime while turning on/off the replication on live systems. Both GitLab.com and the target cell will have live organizations with users consuming services. Therefore, we cannot afford to incur downtime to configure the replication.

### Non-Goals

- The decision of which organization lives in which cell.
- Support for self-hosted installations.
- Geo may or may not be configured, or partially configured, on GitLab.com. This document does not require a decision at the time of writing.

## High-Level Proposal

A organization move can be broken down into five distinct high-level phases:

1. **Continuously replicate an organization's non-PostgreSQL data from the source cell to the target cell.**

    1. Org Mover will reuse [Geo](https://docs.gitlab.com/ee/administration/geo/) code to transfer non-PostgreSQL data continuously to the target cell.

       The purpose is to reuse GitLab Geo code to replicate organization data outside the PostgreSQL database (files, Git data, object storage, container registry, etc.) from the source cell to the target cell. Given that cells cannot use PostgreSQL streaming replication, we need to make Geo independent of the method of PostgreSQL replication. This way, the target cell can connect directly to the source cell database or use PostgreSQL logical replication.

1. **Prepare the organization for the switchover.**

    1. Put the organization into a [maintenance mode](https://gitlab.com/groups/gitlab-org/-/epics/13800).

       A switchover requires a maintenance window in which updates to the source cell are blocked to ensure the switchover can occur without data loss. To block new writes to the data on the source Cell, we put the organization in maintenance mode. This means that the organization's users cannot make any writes to it while in maintenance mode.

       The maintenance window ends once the replication of all the organization's data is completely finished and verified and the routing table is updated. So, to keep the window as short as possible, we should ensure that non-PostgreSQL data replication and verification processes are as close to 100% as possible during active use, and that the newer changes are almost immediately replicated to the target cell before putting the organization in maintenance mode.

1. **Copy organization's PostgreSQL data from the source cell to the target cell.**

    1. Copy data for a particular organization from the source database and write it to the target database present in another cell.

       Copy data for a particular organization from the source database in multiple tables based on `organization_id` and write it to the database present in the target cell.

       Early Org Mover will implement a tool that uses the [COPY approach](https://gitlab.com/gitlab-org/gitlab/-/issues/473894) to transfer PostgreSQL data during cutover. This requires a long downtime to move large organizations, but can be very quick for small organizations.

       The tool is also responsible for the secrets/tokens stored at rest (database). It will establish a trust between the source and target cell to either re-encrypt data inline or prepare the encrypted data on the source cell to be re-encrypted with a transport key and re-encrypted to the target cell after the process finishes. This document does not require a decision at the time of writing.

    1. Handle tables exempt from sharding.

       Some tables are missing the sharding key, so the Org Mover will need to know how to move the data in each of these tables to the target database. This must happen after the organization database data copy is complete.

    1. Handle the ElasticSearch and Zoekt data.

       TBD

    1. Rebuild the ClickHouse data.

       We don't have the `organization_id` available in ClickHouse to move the data to another cell, and most data in ClickHouse is built from PostgreSQL. So once the organization database data copy is complete, we must rebuild the ClickHouse data from PostgreSQL data.

       It is important to note that the Analytics Data Working Group is investigating different ways of syncing data, which would automatically pick up database-level changes and apply them to ClickHouse databases. Since the Org Mover re-creates data on the target cell and drops data from the source cell, changes will be picked up by ClickHouse automatically, and the Org Mover does not need to know about ClickHouse. This is still in [the research phase](https://gitlab.com/gitlab-org/architecture/gitlab-data-analytics/design-doc/-/blob/master/areas/synchronization.md?ref_type=heads#goals-and-objectives.).

1. **Switchover and update the routing information.**

    There are no new writes to the organization data in the source cell, and the
    organization database in the source cell is equal to the organization data in
    the target cell. So, we change the routing information for the organization
    `cell_id`. When we update the `cell_id`, it will automatically make the given
    cell authoritative to handle traffic for the given organization, and we can
    disable the maintenance mode.

1. **Remove all organization data that has been moved over.**

    1. Delete organization's stale data from the source cell:

        1. Remove all data from the PostgreSQL database.

        1. Remove all data from tables exempt from sharding.

        1. Rebuild the ClickHouse data.

        1. Remove all non-PostgreSQL data.

    1. Delete organization's stale data from the targer cell:

        1. Remove all data from the Geo tracking database.

## Implementation Roadmap

Based on roadmap planning as of April 2025, the Org Mover implementation will proceed through several phases:

### FY26 Q1-Q2: Design and Foundational Work

1. **Org Mover Design** (FY25 Q4 - FY26 Q2)
   - Run POCs to validate technical approach
   - Investigate, discuss, and make critical design decisions
   - Define the interfaces and components

2. **Org Mover Foundational Work** (FY26 Q1 - FY26 Q2)
   - Refactor, fix, and improve scalability of Geo code and data structures for Org Mover on .com
   - Prepare the existing codebase for the requirements of organization-level operations

3. **Org Mover Org Checksums 1** (FY26 Q2-Q3)
   - Build selective checksumming by organization
   - Ignore tables where sharding keys are not available

### FY26 Q3-Q4: Implementation and Testing

1. **Org Mover Partial PG Copy** (FY26 Q3)
   - Implement functionality to move an organization's PostgreSQL data from one cell to another in GDK
   - Ignore tables where sharding keys are not available

2. **Org Mover Org Checksums 2** (FY26 Q4)
   - Finish building selective checksumming by organization
   - Depends on completion of sharding work

3. **Org Mover Org Checksums 3** (FY26 Q4)
   - Selectively roll out checksumming per component on GitLab.com
   - Validate checksumming features on .com
   - Let SREs begin cleaning up data on .com

### FY27 Q1-Q2: Production Validation

1. **Org Mover Test Org Move** (FY27 Q1)
   - Move test organizations on GitLab.com
   - Validate end-to-end process in production
   - Identify and address any issues discovered in production
   - Repeat as frequently as possible

2. **Org Mover 1: Internal Org Move** (FY27 Q1)
   - Move an internal organization on GitLab.com that we actually use
   - Depends on a way to block user writes to the organization
   - Depends on organization data deletion, so we can reset the destination after each dry run
   - Validate production performance with our own real data

3. **Org Mover 2: Customer Org Move** (FY27 Q2)
   - Move a real customer organization on GitLab.com

### FY27 Q2-FY27 Q4: Downsize Legacy Cell

1. **Org Mover 3: Minimize Toil** (FY27 Q2-Q3)
   - Automate Org Mover operations to allow for multiple concurrent moves with minimal manual labor

2. **Org Mover 4: Reduce downtime with PG Logical Replication** (FY27 Q4)
   - Implement PostgreSQL logical replication for organization moves
   - Reduce downtime during cutover phase
   - Note: May [increase load on legacy database](https://gitlab.com/gitlab-org/gitlab/-/issues/523306), so we expect
     logical replication to not be usable until many organizations have already been moved

### FY28: Cell Rebalancing

1. **Org Mover From Any Cell** (FY28 Q1)
   - Support manual bi-directional moves (not just from legacy cell)

## Organization Isolation and Sharding Dependencies

The Org Mover project has key dependencies on other Tenant Scale initiatives:

1. **Sharding Work Completion** (FY26 Q1-Q3)
   - Required for clean, performant data separation during migration
   - Required for Org Mover Org Checksums 2

2. **Organization Data Isolation** (FY26 Q4)
   - Required for clean, performant data separation during migration

3. **Org on new cell** (FY26 Q4)
   - Required for testing an organization that was migrated to a new cell

## Migration approaches at different major iterations of Cells

As we build out Cells, we need a way to test the functionality at each [major iteration](_index.md#cells-iterations). We want to dog food the new Cells deployment together with Organizations. The first iteration of Cells will have limited functionality, therefore, we cannot move all GitLab top-level groups out of the Legacy Cell to another Cell without severely impacting productivity. The following section outlines our approach to moving select top-level groups off the Legacy Cell into another Cell for dog food purposes, and how we reconcile the top-level group as the Cells development progresses through the iterations.

We will need to adopt different approaches for each major iteration of the Cells evolution based on which technologies are available at each iteration.

As we discuss creating and migrating Organizations, it's important to call out that top-level groups will retain their URL as they move between Organizations. For example, when a customer's top-level group is moved from the [default Organization](../organization/_index.md#glossary) to their own Organization, their method of access remains unchanged. This means bookmarks, Git remote URLs, etc., for projects in these top-level groups remain unchanged and require no action from users or updates to automation after a migration.

### Cells 1.0

Cells 1.0 will use [Direct Transfer (DT)](https://docs.gitlab.com/ee/user/group/import/) to move internal top-level groups to a separate Organization.

We still need to evaluate and address any gaps, but this is the only option available in this time frame.

DT is a `copy` instead of a `move` operation.
This means that DT will generate new IDs when the data is imported into a new Organization.
It does not make sense to evolve DT to work as a `move` operation, because its core purpose is to import and export data.

It makes sense for DT to evolve to work with Organizations in time for Cells 1.0. This is not a throwaway effort, because DT will need to be supported when we have Cells and Organizations.

Limitations:

- Only top-level groups can be moved between organizations.
- New IDs will be generated which will break automation and integrations - This is acceptable since we will only be moving a limited set of internal top-level groups.
- Public top-level groups cannot be hosted on other Cells, only on the Legacy Cell.
- Several [features available on GitLab.com are not supported on Cells](iterations/cells-1.0.md#features-on-gitlabcom-that-are-not-supported-on-cells) at this iteration.

We will migrate a few small GitLab internal top-level groups to Organizations on another Cell using direct transfer. There will be migrations of Organizations between Cells for Cells 1.0. The specific top-level groups to be migrated will be identified in due course.

![gitlab-org-migrations-cells-1-0](/images/design-documents/cells/gitlab_org_migrations_cells_1_0.drawio.png)

All existing top-level groups on GitLab.com are part of the `default Organization`.
A list of all GitLab top-level groups can be found [in this Google doc (internal link)](https://docs.google.com/spreadsheets/d/18JSGNWYXhAofSqPPLCh_wb0dc9wTT9HuOucHegmsYhA/edit#gid=0).

We will create a new temporary Organization (GitLab Inc.) in a Cell (not Legacy Cell).

We will use [direct transfer](https://docs.gitlab.com/ee/user/group/import/)
or [congregate](https://gitlab.com/gitlab-org/professional-services-automation/tools/migration/congregate) to migrate select top-level groups belonging to GitLab Inc. from the `default Organization` in the Legacy Cell to the GitLab Inc. Organization on the other Cell. If [Org mover](https://gitlab.com/groups/gitlab-org/-/epics/12859) is ready in time, we will use it instead.

All traffic to the top-level groups being migrated will be blocked for the duration of the migration. After the migration is complete, traffic will be resumed and redirected to the other Cell where the groups are located. They will be read/write and fully operational.

### Cells 1.5

At this Cells iteration the focus will be moving top-level groups into Organizations and then migrating those Organizations from the Legacy Cell to other Cells.

We will establish a process for moving top-level groups between Organizations on the same Cell. This functionality is net new and will need to be developed in time for Cells 1.5. It is also a pre-requisite for Org mover to move an Organization between Cells. The work is tracked by [epic 11711](https://gitlab.com/groups/gitlab-org/-/epics/11711).

The solution will need to re-write the org IDs when a top-level group is moved to a new Organization.
A [new solution](https://gitlab.com/groups/gitlab-org/-/epics/11711) is preferable to using the existing DT, because DT is more complex than re-writing IDs.
The new solution would also ensure that new IDs are only generated where necessary when a top-level group is moved into a new Organization.
This improves the experience for users, as it minimizes the changes users have to make to their local repositories, bookmarks, etc. to match the new IDs and paths.

After the top-level groups for a customer are in their own Organization on [Legacy Cell)](goals.md#legacy-cell), the Organization will be put into [maintenance mode](https://gitlab.com/groups/gitlab-org/-/epics/13800) to prevent further changes to the Organization's data while it's being migrated. Org mover then moves the entire Organization from the Legacy Cell to another Cell. After the Org is on the other Cell, traffic routing for the Organization is switched to the other Cell and maintenance mode for the Organization is disabled. The new Organization will not be fully operational on the Other Cell.

Limitations:

- Only top-level groups can be moved between Organizations.
- It will only be possible to move top-level groups between organizations in the same Cell - This is acceptable because our primary use case involves creating a new Organization for a customer in Cell 1 and moving their top-level groups into this Organization. Groups will not need to be moved across Cells at this iteration.
- Public top-level groups cannot be hosted on other Cells, only on the Legacy Cell.

Note, GitLab top-level groups cannot be consolidated under a single GitLab Organization on the Cell hosting the GitLab Inc Organization at this point because many GitLab top-level groups are public groups. Public groups are only supported on the Legacy GitLab Cell. This will need to wait until the Cells-2.0 iteration.

### Cells 2.0

At this iteration it is anticipated that we will have a fleet of Cells. Load across these Cells will need to be rebalanced as Organizations grow requiring a mechanism for moving Organizations between Cells. Org mover will be evolved to move Organizations between Cells.

There is also a need to move top-level groups between Organizations that are on different Cells. The primary use case is to support mergers between two customer Organizations. We do not currently have solution for this. We will in due course evaluate whether org mover should be evolved to move top-level groups between Cells and other approaches.

Limitations:

- Only top-level groups can be moved between organizations.

At Cells 2.0, we will consolidate all GitLab top-level groups under the GitLab Organization by merging the top-levels groups that are part of the GitLab Inc Organization with the main GitLab Organization - the long term home for all GitLab top-level groups.

![gitlab-org-migrations-cells-2-0](/images/design-documents/cells/gitlab_org_migrations_cells_2_0.drawio.png)

All remaining top-level groups belonging to GitLab on the Legacy Cell will be moved to the GitLab Organization. The entire GitLab Organization will be moved to the Cell hosting the GitLab Inc Organization using org mover. Following this, the two Organizations (GitLab and GitLab Inc) will be consolidated by moving the top-level groups in the temporary GitLab Inc Organization into the GitLab Organization. The GitLab Inc org will then be deleted.
