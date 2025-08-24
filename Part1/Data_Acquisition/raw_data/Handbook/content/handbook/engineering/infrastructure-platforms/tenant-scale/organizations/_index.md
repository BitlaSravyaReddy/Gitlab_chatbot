---
title: Organizations Team
description: "Information about the Organizations team"
---

## About

The Organizations team's main focus is to develop the Organization entity needed for data sharding and isolation in the context of [Cells](/handbook/engineering/architecture/design-documents/cells/). The team also offers support for groups, projects, and user profiles within our product.

### Contact

To get in touch with us, it's best to create an issue in the relevant
project (typically [GitLab](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&first_page_size=100)) and add the
`~"group::organizations"` label, along with any other appropriate labels.

For urgent items, feel free to use the Slack channel (internal): [#g_organizations](https://gitlab.slack.com/archives/g_organizations).

### Vision

The team is working on developing a more scalable, unified architecture for GitLab through the implementation of Organizations as a new top-level entity.

Organizations serve as logical containers that enable distribution across a [cellular architecture](/handbook/engineering/architecture/design-documents/cells/) while bridging functionality gaps between self-managed and SaaS GitLab instances.
The new Organizations entity acts as an umbrella for multiple top-level groups, allowing enterprises to aggregate content across groups, implement organization-wide roles, and isolate content from other Organizations.

Simultaneously, the team aims to improve Groups and Projects by addressing several key challenges: creating more flexible hierarchies to accommodate diverse enterprise structures, reducing confusion around project nesting within groups, enhancing discoverability across the product, standardizing deletion and recovery processes, and improving archiving functionality and visibility.
These improvements collectively work toward creating a more intuitive, flexible system for enterprises to represent their business structure and manage permissions.

### Goals

The executive summary goals for the Organizations group include:

- Support GitLab.com's daily-active user growth
- Do not allow a problem with any given data store to affect all users
- Minimize or eliminate complexity for our self-managed use case

### Team Members

The following people are permanent members of the Organizations group:

{{% team-by-manager-slug manager="mandrewsgl" team="Organizations" %}}

### Stable Counterparts

The following members of other functional teams are our stable counterparts:

{{% engineering/stable-counterparts manager="glopezfernandez" role="Tenant Scale|Principal Engineer, Data Stores|Senior Distinguished Engineer, Ops and Core Platform" %}}

### Organization Rollout Counterparts

The following people are supporting our rollout of Organizations.

{{< group-by-slugs atevans>}}

## Projects

We are working on different large projects where each project has a [Directly Responsible Individual (DRI)](/handbook/people-group/directly-responsible-individuals/).
The role of the DRI involves helping to define the scope of the work needed for
the project, ensuring clarity on objectives with the responsibility of looking
forward 3-6 months to identify potential blocks or risks. Their work is not
limited to that area and they also work in other areas as needed.

| Project | DRI     | Team                               |
| ------ |---------|------------------------------------|
| [Organization backend essentials](https://gitlab.com/groups/gitlab-org/-/epics/14111) | Tim     | Chen                               |
| [Organization isolation: sharding](https://gitlab.com/groups/gitlab-org/-/epics/11670) | Chen    | Leonardo da Rosa, Krasimir Angelov |
| [Migrating project/group list pages to Vue](https://gitlab.com/gitlab-org/gitlab/-/issues/460856) | Peter   | Shane                              |
| [Group archiving](https://gitlab.com/groups/gitlab-org/-/epics/15019)| Shubham | Peter, Abdul                           |
| [Deletion flow enhancements](https://gitlab.com/groups/gitlab-org/-/epics/10087) | Remy    | Abdul, Shane                       |

## Meetings

We are a globally distributed group and we communicate mostly asynchronously,
however, we also have synchronous meetings. It's unlikely everyone can attend
those meetings, so we record them and share written summaries ([agenda](https://docs.google.com/document/d/1Z90O_U3mrUoRkmeb5ZqtoM351ASoRTnuFiuou4IMY_k/edit?tab=t.0#heading=h.cbjs5jlz67tt)).

We currently have the following recurring meetings scheduled:

### Weekly Wednesday - Organizations Team Sync

- APAC – 04:00 UTC
- EMEA/AMER – 15:00 UTC
