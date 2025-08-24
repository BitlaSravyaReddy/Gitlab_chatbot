---
title: Knowledge Base
description: GitLab Support's Knowledge Base
---

The knowledge base (KB) is a repository of solutions to commonly-encountered problems, created and maintained by Support Engineers (SE).
The knowledge base turns the effort used to solve a single ticket for one customer into a public resource for all GitLab users.

Benefits:

- Deflects ticket creation.
- Resolves user problems faster.
- Creates consistent, standard answers.
- Creates an environment of trust.
- Gives Support more time to focus on harder issues or improvements.

## Principles

- **Turn it into a habit.** If the issue is worth solving, it is worth saving.
  - Start a knowledge article every time you solve a problem for a customer, a team member or yourself.

- **Accelerate knowledge capture.** Our tools and processes should enhance the speed at which we add knowledge to the Knowledge Base.
  - Capture Knowledge in the moment when the context is clearest and we are able to access customer feedback.
  - Provide feedback as soon as possible if you find a better way to do something.

- **Capture customer context.** Prioritize capturing the right knowledge, in the context of the customer.
  - Focus on documenting the errors and issue as described by the customer for improved findability from other users.
  - Include clear steps and context when documenting solutions. When in doubt, ask, [would Josh Darnit be able to do it?](https://www.youtube.com/watch?v=cDA3_5982h8)

- **Always be iterating.** The Knowledge Base is as much for us as for our customers. We review and update knowledge as we use and reuse it.
  - Reuse is Review: We improve the quality of our knowledge by always iterating.

## How Knowledge Articles differ from GitLab docs

The Knowledge Base and our product documentation are both key elements of GitLab's digital support experience that serve different needs

### Docs

Docs answer: "How does this work?"

- Teaches about product features and how to use them.
- Provides an overview of the current version of our products.

### Knowledge Articles

Knowledge Articles answer: "How do I fix this?"

- Solves problems encountered while using our products.
- Includes solutions to problems in past versions of our products.

## Why you should create a knowledge article

Knowledge articles help users to do tasks, get answers to questions and fix issues they may encounter while using our products.

Creating a clear, well-written knowledge article empowers customers to solve issues on their own and helps Support Engineers quickly access accurate, consistent information. Knowledge articles build trust and ensure reliable, repeatable support experiences.

We use *types* of knowledge to efficiently provide the information for our end users. This includes:

- How-To
- Break/Fix
- FAQ (Question and answer)
- Troubleshooting

## When to create a knowledge article

In short, you should create an article when someone will benefit from the information.

Some questions to consider:

- Will it help customers find information quickly?
- Does it answer a common question / issue?
- Does it document a repeatable way to do something?
- Would this information help a customer get what they need without Support intervention?
- Is this information that may need frequent updates?
- Is this a new issue (with or without a solution) that may cause an influx of support tickets?

### What Training is Available for Knowledge Articles in ZenDesk?

A list of available training can be found in [Knowledge Base Training Resources](../knowledge-base/knowledge-base-training).

## Implementation

We use ZenDesk to create, modify, and  publish knowledge base articles.

Knowledge base articles are dynamically suggested to a user while submitting a ticket.

Integrating with Zendesk offers the following benefits:

- Centralized Knowledge Base
- Scalable and Customizable
- Seamless Integration with Tickets
- Improved Support Engineer Productivity
- Streamlined Analytics and Reporting
- Streamline "Knowledge Centered Service" (KCS), adopting knowledge into the workflow

Knowledge base articles can be found at:

- [Global support knowledge base](https://support.gitlab.com/hc/en-us/sections/15215649512604-Knowledge-Base)
- [US Government support knowledge base](https://federal-support.gitlab.com/hc/en-us/sections/29015014994068-Knowledge-Base)
  **Please Note:** US Government articles as of May 2, 2025 are no longer updated to be consistent with the Global Support Site. No new articles will be available on the US Government page until a later date. Date TBD.

### Roles and Permissions

There are three roles: Support Engineer, Knowledge Champions and Knowledge Admins.

- **Support Engineers**: Create, update and use KB articles in tickets.
- **Knowledge Champions**: Review, publish, archive and control permissions.
- **Knowledge Admins**: Make sure everything runs smoothly.

Most Knowledge Base tasks are performed within the Zendesk platform (Support and Knowledge Portal). However, some tasks by Knowledge Admins will require manual work outside of Zendesk.

{{< cardpane >}}
{{% card header="**Knowledge Workers (Support Engineers, Everyone)**" %}}

| Task | Executed In |
|------|---------|
| Create (draft) articles | Zendesk Knowledge|
| Modify (update) articles | Zendesk Knowledge |
| Link Knowledge article in a Ticket | Zendesk Support |

{{% /card %}}

{{% card header="**Knowledge Champions (Technical Reviewers)**" %}}

| Task | Executed In |
|------|---------|
| Review/Approve articles | Zendesk Knowledge |
| Publish articles | Zendesk Knowledge |
| Create (draft) articles | Zendesk Knowledge |
| Modify (update) articles | Zendesk Knowledge |
| Link Knowledge articles in Zendesk ticket | Zendesk Support |
| Add / Remove Guide Permissions | `support-team.yaml` See: [support-team-yaml docs](/handbook/security/customer-support-operations/docs/gitlab/support-team-yaml-files) |
| Archive articles | Zendesk Knowledge |

{{% /card %}}
{{% card header="**Knowledge Admins (Customer Support Operations)**" %}}

| Task | Executed In |
|------|---------|
| Restore articles | [Feature Request](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?description_template=Feature) |
| Delete articles | Have Knowledge Champion archive, [Feature Request Issue](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?description_template=Feature) to have it permanently deleted |
| History of articles | Zendesk Knowledge (Changelog, available to everyone)|
| Creating permission sets | [Feature Request](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature) with Customer Support Operations |
| Create (draft) articles | Zendesk Knowledge |
| Modify (update) articles | Zendesk Knowledge |
| Link Knowledge articles | Zendesk Support |
| Create section | [Feature Request](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature) with Customer Support Operations |
| Update section | [Feature Request](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature) with Customer Support Operations |
| Delete section | [Feature Request](https://gitlab.com/gitlab-com/gl-security/corp/cust-support-ops/issue-tracker/-/issues/new?issuable_template=Feature) with Customer Support Operations |

{{% /card %}}
{{< /cardpane >}}

### Contributors (Knowledge Workers)

Everyone can contribute to knowledge! The most important thing is to capture the knowledge you've created while solving a problem.
The review process will ensure the content is technically accurate and clear.

### Technical Reviewers (Knowledge Champions)

There will be Support Engineers and Support Managers trained as technical reviewers for knowledge articles across the globe.

[Available Technical Reviewers (by Geo)](https://docs.google.com/spreadsheets/d/14CIIVup-tS5HdLyl0wInf-2m50AptauyhG-ZW5uhs-I/edit?gid=0#gid=0)

Technical Reviewers should be Subject Matter Experts (SMEs) in certain areas (Such as Runner, Authentication, Migrations, etc.). The Technical Reviewers are tasked with **reviewing knowledge articles** based on their knowledge of features.
Technical Reviewers perform the following actions.

#### Responsibilities

Technical Reviewers are expected to:

- Prioritize and Normalize checking the **Manage Articles list** as part of their daily workflow and routine.
- Collaborate with Knowledge article contributors on the technical accuracy of the content, prioritizing having updates published as soon as possible.
- Technically review knowledge articles and determines if the article can be Published for customers (or should remain internal).
- Understands the material and requirements for the article being published.
- Identify trends and opportunities from reporting.
- Provides feedback for knowledge articles.

### Getting Help

Questions can be asked in the dedicated [#spt_knowledge-base](https://gitlab.enterprise.slack.com/archives/C07QDCG4AGH) Slack channel.

For any issues with permissions, please use the knowledge dedicated Slack channel:  [#spt_knowledge-base](https://gitlab.enterprise.slack.com/archives/C07QDCG4AGH) - and  tag  or open an [Issue](https://gitlab.com/gitlab-com/support/support-team-meta) and tag {{< member-by-name "Kirsty Allen" >}}.

### Using AI to generate content

- **ZenDuo** can assist with generating a *first pass* of an article. **Always** review generated data by Duo for technical accuracy. You are still the subject matter expert (SME) of the article and original customer issue.
- Only use ZenDuo or Duo chat when providing customer data. Other LLM services, such as Claude, are not approved for [Red data](../../security/standards/data-classification-standard.md#red).
