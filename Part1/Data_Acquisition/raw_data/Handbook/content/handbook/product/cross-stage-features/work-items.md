---
title: Collaboration on work items framework
description: "Collaboration process and documentation for using and contributing to the work items framework"
---

## Background

A work item is a discrete task or unit of work that needs to be completed as part of a larger project or workflow. It represents a discrete piece of work that contributes to achieving a goal or delivering a desired outcome. Work items are part of many use cases like Agile Planning, ITSM, and Security Management.
Previously, GitLab had different implementations for work items. Examples include Epics, Issues, Requirements, Incidents, and Vulnerabilities. This approach led to frustration from users due to the inconsistent experience, and the Plan stage decided to build a framework to support all work items in GitLab. This guide describes the functionality available, how to use it, and the best approach to contribute to the framework.

## Why use the work items framework?

The work items framework provides a consistent approach to creating work item objects for teams to plan and organize their work in GitLab. Consumers of the framework will benefit from the efficiency of using a framework with comprehensive out of the box functionality that is easily extendable.

## What functionality is available?

The work items framework provides a [base work item object](https://docs.gitlab.com/architecture/blueprints/work_items/#work-item-properties) with options to extend functionality using [widgets](https://docs.gitlab.com/architecture/blueprints/work_items/#work-item-widgets). Additional work item data and functionality is encapsulated within a widget. For example, the [WorkItemWidgetAssignees](https://docs.gitlab.com/api/graphql/reference/#workitemwidgetassignees) enables user assignment.

You can see the list of available widgets [here](https://docs.gitlab.com/architecture/blueprints/work_items/#work-item-widgets). Each widget, except for the core work item object, can be turned on or off for each work item type.

The work items framework also provides an out-of-the-box work item detail view and work items can be displayed in the Issues list if desired.

## Where is the work items framework used?

The work items framework is currently used in several features; including [Tasks](https://docs.gitlab.com/user/tasks/) and [OKRs](https://docs.gitlab.com/user/okrs/).

Work is ongoing to convert existing objects to Work Item Types, and implement new ones; for example [Issues](https://gitlab.com/groups/gitlab-org/-/epics/9584) and [Epics](https://gitlab.com/groups/gitlab-org/-/epics/9290).

A comprehensive list of Work Item Types currently implemented and being implemented is available in the [Architecture Blueprint](https://docs.gitlab.com/architecture/blueprints/work_items/#work-item-types).

## What functionality is on the roadmap for the work items framework?

You can see new functionality planned in the [Plan stage direction page](https://about.gitlab.com/direction/plan/) and in our [GitLab issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=popularity_asc&state=opened&label_name%5B%5D=work%20items&first_page_size=100).

## What is out of scope for the work items framework?

- Our goal is to increase the consistency in GitLab, so all work items should use the same work item detail view.
- We want to encourage teams to contribute to the framework directly instead of building separate views or extensions.

## Getting started

First, you will need to consider whether the work items framework is right for your feature, including your users and the experience they require. You can read about that process [here](/handbook/product/ux/product-design/ux-roadmaps/).

All contributions begin with the _Validation backlog_ and _Problem validation_ phases. During these phases, the Plan stage PMs should be **Informed** of upcoming validation activities and **Consulted** during problem validation. These are critical opportunities to collaborate with us and ensure that your ask is not overlapping with future roadmap items and is not against the guiding principles.

What do R, A, C, and I mean?

| Phase | Your group | Plan Stage | Description |
| ----- | ---------- | ----------------- | ----------- |
| Validation backlog | R, A | I | Your group has the appropriate freedom as **Responsible** and **Accountable**, as it's too early to know if a problem is worth solving through the work items framework. But, in the cases where your group _assumes_ that the work items framework _could be_ the right avenue to address the problem at hand, we only ask to be **Informed**, so one-way communication. |
| Problem validation | R, A | C | We're **Consulted**, meaning that we can point you to existing research, similar problems, and more. We care about this phase because it's our chance to influence how much of the work items framework could be affected by potential solutions. Depending on the nature of the functionality being built, one GM/PM from the Plan stage will be selected as DRI for collaboration.|

At the end of this phase, we will work with your group to determine a contribution model.

## Contribution models

If you decide to use the work items framework this will usually mean that you're creating a new work item type and/or creating new widgets. Sometimes, all functionality you need will already be in the framework. Hooray! If not, you can contribute to the framework to [extend it for your use case](/handbook/product/ux/product-design/ux-roadmaps/).

| Phase | Your group | Plan Stage | Description |
| ----- | ---------- | ----------------- | ----------- |
| Solution validation | R, A | C |  We're **Consulted**, meaning that we want to involved in shaping the solution. Plan team members have a broader view of the problems and use cases that the work items framework is solving. The PM and UX team can help shape the solution so that it is as generic as possible and can provide value to more than one use case. |
| Build track | R, A | I | We strive to build a framework that can easily be built upon and we only need to be **Informed** during this phase. However, we are here to help with implementation if your team needs support. |

## Creating a new work item type

If your group would like a particular work item type to describe your user's work, you can create a new work item type. Creating a new work item type sets the foundation for adding widgets that are specific to data and behavior for your use case. For example, OKRs have a [progress widget](https://docs.gitlab.com/user/okrs/#set-objective-progress) that is not present in other work item types.

You can see an example of the solution validation and build planning process in [this epic](https://gitlab.com/groups/gitlab-org/-/epics/7864). Here the PM defined the data elements and behavior desired in the Objective and Key Result work item type.

For details on the technical implementation process, please refer to our [documentation](https://docs.gitlab.com/development/work_items/#creating-a-new-work-item-type-in-the-database). You can see an example of the implementation in the introduction of OKRs:

- [Backend Work to add Objective and Key Result Work Item Types](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/101324)
- [Backend work to support creation of objectives behind feature flag](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/103355)
- [Frontend work to support creation of Objectives & include them in Issue lists](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/102721)

## Contributing to the Work Items framework

The Work Items framework is at the core of planning and collaboration in GitLab, and we welcome contributions from other teams. To help you integrate new widgets or data elements successfully, this page outlines the main considerations. Depending on the scope of your contribution, you might not need to address every point. However, reviewing them all ensures that your feature is robust, user-friendly, and consistent with the rest of GitLab.
**Tip:** Follow GitLab's work items architecture vision and [engineering best practices](/handbook/engineering/architecture/design-documents/work_items/) to ensure architectural alignment.

### General considerations

| Consideration | Details |
|---------------|---------|
| **Data Interactions** | • **Quick actions**: Ensure the widget can be updated via [quick actions](https://docs.gitlab.com/ee/user/project/quick_actions.html)<br>• **GraphQL API integration**: Provide queries and mutations for programmatic access<br>• **Bulk editing support**: Verify your widget can be included in bulk edits (e.g., for issues) |
| **Search Integration** | • **Inclusion in global search**: Make it discoverable via GitLab's global search (Open an [global search feature request issue](https://gitlab.com/gitlab-org/gitlab/-/issues/new?description_template=Global%20Search%20-%20feature) and add applicable details)<br>• **Filtering/sorting options**: Where applicable, add filter/sort options for boards, lists, or roadmaps<br>• **Indexing**: Confirm that data is indexed for quick retrieval<br>• **GLQL**: Ensure your widget can be used as a filter option, where applicable, in GitLab Query Language (GLQL) |
| **Views Integration** | • **Lists and Boards**: If recommended by UX, display widget info in lists and boards; provide sidebar editing and list creation capabilities<br>• **Roadmaps and Detail Pages**: Include the widget on roadmap cards and in appropriate sections of work item detail pages (including child/linked items) |
| **Rollup and Aggregation** | • **Hierarchical rollup**: Define if the widget's values roll up to parent items (e.g., weight, progress)<br>• **Aggregation rules**: Decide on summing, averaging, or other calculations; respect plan-based licensing rules<br>• **Summary views**: Show aggregated data clearly on roadmaps, boards, or summary widgets |
| **Conditional Behavior** | • **Interaction with other widgets**: Specify if it affects or is affected by other widgets<br>• **Behavior on closure**: Decide if it locks when a work item is closed<br>• **Data retention on cloning/moving**: Define whether data persists when a work item is cloned or moved |
| **System Notes Logging** | • **Audit trail**: Any changes to the widget should create system notes (epics, issues, tasks, etc.) |
| **Import and Export** | • **Handling of widget data**: Decide how data is treated in group/project imports, transfers, or issue imports/exports |
| **Real-time Updates** | • **Live syncing**: Changes to the widget should appear immediately in relevant views without requiring manual refreshes |
| **Permissions and Roles** | • **Access levels**: Ensure the widget respects [role-based access](https://docs.gitlab.com/ee/user/permissions.html) (Guest, Reporter, Developer, Maintainer, Owner) |
| **Widget Availability** | • Ensure the widget is enabled by default for the corresponding work item types (unless the design calls for an opt-in behavior) |

**Tip:** If you're unsure whether a particular item applies to your contribution, or if you need clarification on design, consult the [Plan UX team](https://about.gitlab.com/handbook/engineering/ux/) and the Work Items PM. We're here to help you ship features that delight GitLab users and fit seamlessly into the Work Items framework.

### Creating or modifying widgets

Widgets encompass the specific data and behaviors that differentiate work items from each other. If you need to modify or add a new work item widget, refer to [this page](https://docs.gitlab.com/development/work_items_widgets/) for the technical details on how to achieve this.
You can see an example of the implementation in the [introduction of the dates widget](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/93204). Note that this widget is planned to be used across several work item types.

### Ideas only

Sometimes, your team will not have the capacity or expertise to contribute to the framework. That is OK! We still want to hear from you. Please create an issue describing your needs and tag the @gweaver, and @amandarueda.
