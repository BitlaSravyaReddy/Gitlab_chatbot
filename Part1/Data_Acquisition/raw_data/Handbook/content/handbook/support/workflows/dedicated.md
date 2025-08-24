---
title: GitLab Dedicated Overview
category: GitLab Dedicated
description: "GitLab Dedicated Support overview."
---

### Overview

[GitLab Dedicated](https://docs.gitlab.com/subscriptions/gitlab_dedicated/), from a support perspective, works as a combination of SaaS and Self-Managed. Customers have full Admin access to the instance, but no access to the infrastructure, nor to the backend configurations. This workflow captures the differences, and details of providing support for GitLab Dedicated.

When working on GitLab Dedicated tickets, a good mental model to follow is to determine if the issue is an Application issue or an Infrastructure issue.

- If you're dealing with an Application issue, that is, the issue is within the GitLab application, then you can treat it like a Self-Managed instance while being mindful of the [features that are not available for GitLab Dedicated](https://docs.gitlab.com/subscriptions/gitlab_dedicated/#unavailable-features).
- If it's an infrastructure issue, you'll want to consider engaging with the SREs by opening a [Request for Help](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicated), checking [for incidents](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/incident-management/-/issues/?type%5B%5D=incident), or [raising one yourself](#raise-a-dedicated-incident). The [runbooks](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/tree/main/runbooks) used by the SREs may be useful additional context.

Use the [SaaS, Self-Managed and Dedicated Troubleshooting tables](/handbook/support/workflows/saas_sm_cheatsheet/) to learn more about the differences between `gitlab.com`, self-managed and GitLab Dedicated.

If you'd like to work on GitLab Dedicated tickets, consider [creating an issue using the template](https://gitlab.com/gitlab-com/support/support-training/-/issues/new?issuable_template=GitLab%20Dedicated) in Support Training, and read the [overview](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/).

Below is a list of other GitLab Dedicated Support workflow pages. This is list
is a temporary measure to workaround the lack of until workflow categories are reintroduced

- [GitLab Dedicated Logs](/handbook/support/workflows/dedicated_logs/)
- [GitLab Dedicated Observability and Monitoring (Grafana)](/handbook/support/workflows/dedicated_instance_health/)
- [GitLab Dedicated Switchboard Troubleshooting](/handbook/support/workflows/dedicated_switchboard/)
- [Hosted runners for GitLab Dedicated](dedicated_runners.md)

Here are links to other pages about GitLab Dedicated around GitLab:

- Docs: [Configure GitLab Dedicated](https://docs.gitlab.com/administration/dedicated/)
- Product: [Glossary of Switchboard terms](https://about.gitlab.com/direction/saas-platforms/switchboard/glossary/)
- Infrastructure: [GitLab Dedicated internal docs](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/) (GitLab internal only)
- CSM: [Engaging with GitLab Dedicated Customers](https://internal.gitlab.com/handbook/customer-success/csm/gitlab-dedicated/) (GitLab internal only)

### Handling tickets that are not about GitLab the product but related to how we handle the infrastructure

Handling GitLab Dedicated tickets should be approached the same way as other tickets: use the docs, the handbook and the various issue trackers to help address the customer request. Anything that is related to our provisioning of the tenant or how we manage the infrastructure requires a different approach:

- check the docs and the handbook
- point the customer to the [GitLab Trust Center](https://trust.gitlab.com/?product=gitlab-dedicated) at `trust.gitlab.com` for inquiries related to compliance
- point the customer to their CSM for any questions not addressed by the GitLab Trust Center

### Test and reproduction on GitLab Dedicated instance

GitLab Support has access to a GitLab Dedicated instance for testing and problem
reproduction purposes. This instance can be accessed at the following URLs:

- GitLab: https://dedicatedtestsandbox.gitlab-private.org
- OpenSearch: https://opensearch.dedicatedtestsandbox.gitlab-private.org/_dashboards
- Grafana: https://grafana.dedicatedtestsandbox.gitlab-private.org
- Switchboard: https://console.gitlab-private.org/tenants/40

To receive an invite, ask Armin, Brie, Daphne or Wei-Meng in [#support_gitlab-dedicated](https://gitlab.enterprise.slack.com/archives/C058LM1RL3V).

### Conducting a test

When running a test on the GitLab Support Dedicated instance,

- consider whether your test can be conducted in an instance deployed via the [Sandbox Cloud Realm](/handbook/company/infrastructure-standards/realms/sandbox/)
- communicate about it on the Slack channel [#support_gitlab-_dedicated](https://gitlab.enterprise.slack.com/archives/C058LM1RL3V)
- revert your changes when you are done

As the test instance is shared within the GitLab Support team, post a message at the beginning of a test with an estimate duration if the test is likely to impact the performance of the instance.
Upon test completion, revert your changes and use the emoji `:done:` to show the test is completed and the instance has been restored to the previous state.

This instance is deployed to the [`Test` environment](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/tree/main#deployed-environments).

GitLab Duo is not supported on the test instance, see [STM 6619](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/6619) for more information. 

### Administrative access to a Dedicated instance

The GitLab Dedicated team does **not** have administrative access to the [Admin Area](https://docs.gitlab.com/administration/) in the GitLab application on Dedicated instances and neither does the GitLab Support team. Select individuals in the customer organization do have access to the **Admin Area**. Any support requests that require a GitLab instance administrator to make a change in the Admin Area, for example resetting 2FA, has to be performed by the appropriate team within the customer organization.

### Sharing internal logs, data & graphs

We should not visually or physically share internal logs, data and graphs
with GitLab Dedicated customers by default. Examples of things we should
not share include, but are not limited to, screenshots of graphs, copied
log entries, and raw log dumps.

For avoidance of doubt:

- Internal logs refers to [logs not generated by the GitLab application](/handbook/support/workflows/dedicated_logs/#sharing-logs).
- Internal data and graphs include all data available in Grafana.
Here is some background to understand why:

1. GitLab Dedicated comes with a Sevice Level Availability SLO, which if not
   met results in financial penalties for GitLab.
1. Capacity is limited for the GitLab Dedicated engineering teams as of October
   2023. The teams want to spend the majority of their time on engineering
   tasks and avoid spending time answering non-critical customer questions.

Sharing internal logs, data and graphs without adequate context and explanation
may cause customers to misinterpret the provided information, creating more
work for *all* teams involved and, in the worst case, cause unnecessary damage
to GitLab's relationship with the customer.

If you assess that sharing such internal logs, data and graphs with the
customer would create results for the customer and for GitLab, consult with a
Director of Support. Be aware that a formal process for this is still being
defined, and that there will be delays as approvals are currently ad hoc.

### Working with logs

Working with logs [has been moved](/handbook/support/workflows/dedicated_logs/)

### Working with Grafana

Working with Grafana [has been moved](/handbook/support/workflows/dedicated_instance_health/)

### View instance metadata

Use the Switchboard app. More information can be found in the [Switchboard workflow](/handbook/support/workflows/dedicated_switchboard/).

#### Feature Flags are not supported

In GitLab Dedicated, [feature flags](https://docs.gitlab.com/subscriptions/gitlab_dedicated/#available-features) are not supported, meaning we do not able enable/disable a feature flag for a Dedicated instance. When customers request feature flags to be modified in the GitLab Rails console, the GitLab Support team should:

- create or find an issue in the appropriate issue tracker about making this feature generally available (without a feature flag).
- notify the [appropriate Product Manager](/handbook/product/categories/) in the issue with a comment that followed the [feedback template](/handbook/product/product-management/#feedback-template).
- notify the customer that we [don't keep tickets open](https://about.gitlab.com/support/general-policies/#we-dont-keep-tickets-open-even-if-the-underlying-issue-isnt-resolved) even if the underlying issue isn't resolved.
- check whether the customer has any questions about the next steps.

Support team members with questions can check in the [`#spt_pod_dedicated`](https://gitlab.enterprise.slack.com/archives/C058LM1RL3V) Slack channel for additional guidance.

### Feature proposals

GitLab Dedicated feature proposal issues should be created in the **Public** [`gitlab-org/gitlab` issue tracker](https://gitlab.com/gitlab-org/gitlab/-/issues/?sort=created_date&state=opened&first_page_size=100). Mention the Product Manager when opening a feature proposal issue. Use the [feedback template](/handbook/product/product-management/#feedback-template) to register a customer's interest in the feature proposal.

### Configuration changes

GitLab Dedicated uses the [Cloud Native Hybrid reference architecture](https://docs.gitlab.com/administration/reference_architectures/10k_users/#cloud-native-hybrid-reference-architecture-with-helm-charts-alternative). Instance implementation and changes are done via the [instrumentor project](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/instrumentor).

If it's an emergency, [raise a Dedicated incident](#raise-a-dedicated-incident).

When any changes are required besides those listed below, raise [an issue with `SupportRequestTemplate-GitLabDedicated`](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicated).

#### Inbound (Forward) PrivateLink Request

1. In the ticket, ask the customer to provide the [required information](https://docs.gitlab.com/administration/dedicated/configure_instance/network_security/#inbound-private-link). In this case, it's an **IAM principal**.

   - The IAM principal must be an [IAM role principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-roles) or [IAM user principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/).
   - The IAM user principal has the following format: `arn:aws:iam::<Customer_AWS_Account_ID>:user/user-name`. The IAM role principal has the following format: `arn:aws:iam::<Customer_AWS_Account_ID>:role/role-name`. Keep the format of these two in mind to avoid prolonging the ticket if an unexpected format is provided.

1. Open a new [PrivateLink Request issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicatedPrivateLinkRequest) and confirm that the `support::request-for-help` label is added.
1. Add the IAM principal to the issue. The Environment Automation team will provide a **Service Endpoint Name**.
1. The customer will follow the steps in [our documentation](https://docs.gitlab.com/administration/dedicated/configure_instance/network_security/#inbound-private-link).

#### Outbound (Reverse) PrivateLink Request

Outbound PriveLink allows any traffic from the GitLab Dedicated instance, or hosted runners for GitLab Dedicated to not be exposed to the public internet. While we advise for the onboarding to be completed, the customer can start these steps before.

1. Open a new [PrivateLink Request issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicatedPrivateLinkRequest) and confirm that the `support::request-for-help` label is added.

   - As a comment in the issue, request two **Availability Zone IDs (AZ IDs)** that can be used by the customer. For hosted runners, we only need a primary **Availability Zone ID (AZ IDs)**.

1. Provide the IAM role Principal to the customer. It has the following format: `arn:aws:iam::<AWS_Account_ID>:role/reverse_private_link@<tenant_id>`. You will find this information in the `Reverse Private Link IAM Principal` row of the `Tenant Details` section in Switchboard. Alternatively, read the instructions in the issue created for information on how to find the `<AWS_Account_ID>` and `<tenant_id>`.
1. Provide the two **AZ IDs** from the issue to the customer. An example AZ ID is: `use-az1` or `usw-az4`. Note: *These are not AWS Zone IDs.*

   - Provide the two AZ IDs early in the ticket to avoid prolonging the ticket. The AZ IDs must be in the same region as the customer's tenant instance. The customer can then make the decision of which specific zones that can be used. AZ IDs are shared between different zones in a region but cannot be used outside of the region. For example, AZ IDs in `us-west-1*` cannot be used in `us-west-2*`. Some of the zones in each reach share AZ IDs with other zones in the same region but you must work with the customer to find the overlap.

1. Ask the customer to provide the [required information](https://docs.gitlab.com/administration/dedicated/configure_instance/network_security/#outbound-private-link). In this case, it's a **Service Endpoint Name**, a list of **AZ IDs** they will be using (should match provided AZ IDs), and **Domain Name** (with one of two options).

   - The **Service Endpoint Name** uses a reverse domain name notation and has the following format: `com.amazonaws.vpce.<region>.<vpce-svc-identifier>`

1. Fill in the issue with the information provided by the customer and follow next steps in the issue.

#### IP Allowlist Request

In most cases, customers should use **Switchboard** to update the IP allowlist for their GitLab Dedicated instance. If this is not possible:

1. Ask the customer to provided the [required information](https://docs.gitlab.com/administration/dedicated/configure_instance/network_security/#ip-allowlist) in the ticket. In this case, it's a comma-separated list of IP addresses.
1. Open a [Request for Help issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicated) and confirm that the `support::request-for-help`) in the GitLab Dedicated issue tracker.

##### SCIM / OIDC with IP Allowlist request

Customers who use the IP allowlist may request to enable the SCIM or OIDC endpoints to the internet. This is a simple on/off toggle but must be performed by the Environment Automation team:

1. Open a [Request for Help issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicated) in the GitLab Dedicated issue tracker. (Confirm that the `support::request-for-help` label has been applied)

#### SAML Request

1. Ask the customer to provided the [required information](https://docs.gitlab.com/administration/dedicated/configure_instance/saml/#activate-saml-with-a-support-request) in the ticket. In this case, it's a SAML configuration block or can be a list of information provided by a customer.
1. Open a new [SAML Config Request issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicatedSAMLConfigRequest) and confirm that the `support::request-for-help` label is added.
1. Add the customer provided information and match it with the required formatting.

#### Application Logs Request

1. In the ticket, ask the customer to provide the [required information](https://docs.gitlab.com/administration/dedicated/monitor/#request-access-to-application-logs). In this case, it's an **IAM principal**.

   - The IAM principal must be an [IAM role principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-roles) or [IAM user principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

1. Open a [Request for Help issue](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicated) in the GitLab Dedicated issue tracker.
1. Provide the IAM principal to the Environment Automation team.
1. Provide the name of the S3 bucket to the customer.

### Filing issues

In cases where Customer Support need to interact with Dedicated engineers to gather information or debug a problem at tenant's request (when Grafana or OpenSearch do not suffice), raise an issue in the [Request for Help issue tracker](https://gitlab.com/gitlab-com/request-for-help/-/issues/) using [the `Request for Help` template](https://gitlab.com/gitlab-com/request-for-help/-/issues/new?issuable_template=SupportRequestTemplate-GitLabDedicated). 

RFH have an [SLA](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/runbooks/on-call.html#sla) of three working days for all severity levels. For severity 1 and 2 issues based on [Support definition](https://about.gitlab.com/support/#definitions-of-support-impact), consider [raising a Dedicated incident](#raise-a-dedicated-incident). Ask in Slack `#support_gitlab-dedicated` if you are unsure.

During the course of the investigation, you may realize that you need to escalate a Request for Help (RFH) issue to another team. You should follow the existing process to [formally request help from another group in the GitLab Development Team](/handbook/support/workflows/how-to-get-help/#how-to-formally-request-help-from-the-gitlab-development-team). When doing this:

- Summarize the investigation thus far and make sure the ask for the team you are escalating to is clear
- Apply the `~workflow-infra::Escalated` label to the RFH issue in the GitLab Dedicated issue tracker

### Handling GitLab Dedicated emergencies

GitLab Dedicated customer emergencies follow the same [definitions and exceptions](/handbook/support/workflows/customer_emergencies_workflows#determine-if-the-situation-qualifies-as-an-emergency)
as regular customer emergencies.

If the customer is reporting an availability or performance issue:

1. Check the [GitLab Dedicated incident management tracker](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/incident-management/-/issues/?type%5B%5D=incident)
   for relevant open incidents.
1. If there is an open incident:
   - Inform the customer that the GitLab Dedicated infrastructure team is actively investigating.
   - Get in touch with the Dedicated SRE on-call and determine if the customer needs to be involved
     with troubleshooting.
   - Assist the customer and the Dedicated SRE as necessary.
1. If there isn't an open incident, [raise a Dedicated incident](#raise-a-dedicated-incident).

#### Raise a Dedicated incident

When raising a GitLab Dedicated incident, you must complete all three steps:

1. Follow the [Dedicated On-Call runbook](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/team/-/blob/main/runbooks/incident-management.md#how-to-raise-an-incident).
1. In the incident channel that is automatically created on Slack, provide a summary of the current state.
1. Escalate to the Dedicated Engineer On-Call by following [the escalation process](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/runbooks/on-call.html#escalating-to-an-on-call-person)

You are now done raising the incident!

#### Engaging the GitLab Dedicated CMOC

If the nature of the emergency reaches the point where we only need to provide async status updates
to the customer, consider engaging the [GitLab Dedicated Communications Manager on Call](/handbook/support/workflows/dedicated_cmoc)
to take over.

### Troubleshooting tips

#### Tagging logs while running tests

Customers can add a custom identifier, such as the ticket ID, to the `user-agent` field when testing. This makes it easier to filter logs related to the test.

For example:

```bash
curl -k -vvv -A"GitLabSupport012345" "https://tenant.gitlab-dedicated.com/users/sign_in"
```
