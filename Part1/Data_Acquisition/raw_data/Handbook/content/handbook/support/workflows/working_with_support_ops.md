---
title: Working with Customer Support Operations
category: References
subcategory: General
description: Documenting the various types of Customer Support Operations related tickets and the escalation process to notify Support Operations.
---

## Overview

Customer Support Operations sits under Security, alongside teams like Corporate Identity and IT End User Support. As a corporate provider, Customer Support Operations is specifically tasked with providing support *for Customer Support*.  

This page exists primarily as a quick-reference, linking to sources of truth and making sure Customer Support has the information needed to get things done!

### Quick Links

| Resource | Link |
|----------|------|
| **Issue Tracker** | [Customer Support Operations Issue Tracker](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker) |
| **Bug Report Template** | [Create Bug Report](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Bug) |
| **Feature Request Template** | [Create Feature Request](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature) |
| **Incident Handling** | See [Incidents](#incidents) |
| **Slack Channel** | [#support-operations](https://gitlab.slack.com/archives/C018ZGZAMPD) |
| **System Criticality Sheet** | [Customer Support Operations System Criticality](https://drive.google.com/drive/u/0/search?q=Customer%20Support%20Operations%20System%20Criticality%20type:sheets) |

> **Important:** All issues for Customer Support Operations should be created in the [Customer Support Operations Issue Tracker](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker).

## Self-Service Options

Before creating an issue, check if your request can be self-serviced. The following items can be handled directly by Support team members:

- **Zendesk Managed Content** - Updates to macros, triggers, and other Zendesk content can be managed directly by Support team members with manager approval. See: [Working on Zendesk Content](/handbook/support/workflows/working-on-zendesk-content/)
- **Support Team YAML Files** - Changes to support team configuration files can be made through direct merge requests. Customer Support Operations must approve to merge. See: [Support Team YAML Files](/handbook/security/customer-support-operations/docs/gitlab/support-team-yaml-files/)

> **Note:** If an issue is opened for something that could have been self-serviced, the issue will be closed with instructions on how to self-serve the change. If you need help, reach out in `#support-operations` and we can guide you through!

## Workflows

### Ticket where customer is asking for support portal changes

Occasionally, a customer might mis-file a ticket and send a request for support portal changes using a Support form. In these cases, please change the form to `Support Ops` in Zendesk and Customer Support Operations will handle it from there. Please do not send a public reply (as that removes our SLA clock from the ticket).

### Asking general questions

For general questions and assistance, reach out via the [support_operations Slack channel](https://gitlab.slack.com/archives/C018ZGZAMPD). From there, a member of the Customer Support Operations team will respond and work with you to help address the question. 

### Basic Issue Flows

All requests for Customer Support Operations should be created in the [Customer Support Operations Issue Tracker](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker) using the appropriate template. With the exception of a few [self-service options](#self-service-options), nearly everything starts with an issue!

If what you want to get done is:

- On the roadmap? *Create a [Feature Request issue](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)!*
- Not on the roadmap, but seems easy? *Create a [Feature Request issue](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)!*
- Maybe easy, but maybe hard? I definitely know what I want though. *Create a [Feature Request issue](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature)!*
- Reporting a bug? *Create a [Bug Report issue](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Bug)!*
- ... well, actually, I don't totally know yet. *Create an RFC issue in `support-team-meta`* (or work otherwise within the [Change Management in GitLab Support](/handbook/support/managers/change-management/) framework)

If you're creating an issue, the Customer Support Operations team expects that:

- **You're empowered to make decisions**. That is, you're a DRI at the appropriate level to steward your change or you've been delegated that responsibility by an appropriate DRI.
- **You're responsive.** You're prioritizing working on the thing you want so that it can be shipped on time, and to spec.
- **You'll be ready to validate and sign off.** When Support Operations deploys something to staging, you need to be ready to test (or delegate / organize testing) and sign off on acceptability before it can go live in production.

More about [Working with Customer Support Operations](/handbook/security/customer-support-operations/#working-with-us).

More about [stages that Customer Support Operations uses to represent progress](/handbook/security/customer-support-operations/workflows/gitlab/working-issues/).

#### Bugs

Bugs should be reported using the [Bug Report Template](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Bug) in the Customer Support Operations Issue Tracker (project path: `gitlab-com/gl-security/corp/cust-support-ops/issue-tracker`).

When creating a bug report:

1. Select the Bug template from the dropdown
2. Fill in all required fields, especially steps to reproduce
3. Select appropriate severity

Bugs are generally of a high priority to fix, and will get scheduled in the current iteration. Depending on workload, severity, fix complexity and [system criticality](https://drive.google.com/drive/u/0/search?q=Customer%20Support%20Operations%20System%20Criticality%20type:sheets) may get scheduled in the future.

More about the [Bug Report issue flow](/handbook/security/customer-support-operations/#bug-reports).

#### Feature Requests

The focus for feature requests is on aligning them with our existing [Support Roadmap](https://roadmap-e17445.gitlab.io/). For larger requests, you may need to work with the leadership team to escalate issues to re-plan any conflicts and protect strategic items. For smaller requests, they can often be added in as we go, as long as they don't get in the way of delivering current roadmap items.

Feature requests should be submitted using the [Feature Requests Template](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature) in the Customer Support Operations Issue Tracker (project path: `gitlab-com/gl-security/corp/cust-support-ops/issue-tracker`).

When creating a feature request:

1. Select the Feature template from the dropdown
2. Clearly describe the business need and expected outcome
3. Include any relevant stakeholders using the `/cc @username` syntax

More about the [Feature Requests issue flow](/handbook/security/customer-support-operations/#feature-requests).

## Incidents

Things do break! Customer Support Operations is here to help.

First, check the [Customer Support Operations System Criticality Sheet](https://drive.google.com/drive/u/0/search?q=Customer%20Support%20Operations%20System%20Criticality%20type:sheets) to determine the severity of the issue.

### Incident Reporting Process

1. Start by posting in the [#support-operations](https://gitlab.slack.com/archives/C018ZGZAMPD) Slack channel (during [Global Support Hours](https://about.gitlab.com/support/#hours-of-operation))
2. Wait for a response. Continue down this list if you get no response for:
   - 24 hours for issues with Administrative systems 
   - 8 hours for issues with Business Operational systems
   - 30 minutes for issues with Business Critical Systems
   - 10 minutes for issues with Mission Critical Systems
3. [Create a new PagerDuty incident](https://gitlab.pagerduty.com/incidents/create) with "Customer Support Operations" as the Impacted Service (See: [Support Operations On-Call Workflow](/handbook/security/customer-support-operations/workflows/support_operations-on-call))
4. Be available to work with the on-call to develop a plan to resolve the problem

When creating an incident issue, include:

- Clear description of what's happening
- Impact on users/customers
- Any error messages or screenshots
- Steps you've already taken to troubleshoot

More about [how Customer Support Operations handles incidents](/handbook/security/customer-support-operations/workflows/incidents/).

## General tips

1. **Start early** - if you are the DRI for a key strategic item on the Support Roadmap, start working with Ops early. Create a tracking issue so a plan can be formed and blockers discovered early.
1. **Don't "save up" work** - if items are important to the business, they should be tracked. If they're not tracked, they won't get prioritized. 
1. **Have strong opinions on outcomes** - avoid strong opinions on technical implementation.
1. **Don't be quiet** - as a DRI, if a technical implementation isn't looking like it's going to meet the criteria, speak up whether it's in the Validation stage or not. It's better to ship the right thing a bit late than the wrong thing quickly.

## Deployments and Delivery

Unless otherwise communicated, changes ship on the 1st of the month. This is to align any changes to metrics with month boundaries.

Once you've signed off on work, make sure you're following the steps in [Change Management in Support - Rolling out a Change](/handbook/support/managers/change-management/#rolling-out-a-change) to make sure everyone on the team is aware.
