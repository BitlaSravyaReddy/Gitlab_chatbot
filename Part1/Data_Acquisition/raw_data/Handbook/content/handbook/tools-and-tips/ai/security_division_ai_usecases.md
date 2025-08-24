---
title: "AI use cases within the Security Division at GitLab"
---

Learn how the [Security Division](/handbook/security/) leverages AI platforms such as [Claude](/handbook/tools-and-tips/ai/claude/) and [GitLab Duo](/handbook/tools-and-tips/ai/gitlab-duo/) to optimize workflows, improve productivity and automate manual tasks.

## Security Tools Using AI

The Security Division integrates AI capabilities into various tools and automations. Most use cases integrate AI capabilities into existing tools and capabilities to improve productivity and automate manual processes and tasks.

| Tool | AI Engine | Use Case | Team |
|------|-----------|----------|------|
| [AI-assisted Incident reporting](https://gitlab.com/gitlab-com/gl-security/security-operations/sirt/tines/-/issues/299) | Claude | Helps users to report security issues more quickly and efficiently by pre-filling the incident report forms based on a short description of the issue. | [Security Incident Response Team (SIRT)](/handbook/security/security-operations/sirt/) |
| [AppSec Assistant](https://gitlab.com/gitlab-com/gl-security/product-security/appsec/tooling/assistant) | GitLab Duo | AI reviews development issues to identify security risks at design time | [Product Security Engineering](/handbook/security/product-security/security-platforms-architecture/product-security-engineering/)on behalf of [Application Security](/handbook/security/product-security/application-security/) |
| [Automate our Continous Control Monitoring Program](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-compliance/team/-/tree/AWS-API-test/Continuous%20Control%20Monitoring/AWS?ref_type=heads) | Claude | Generate entire scripts used for: Pull data from resources (e.g. AWS); Pull policies from a yaml file; Perform an audit analysis and Conclusion (example [here](https://gitlab.com/gitlab-com/gl-security/security-assurance/security-compliance/continous-control-monitoring-program/-/issues/2)) | [Security Compliance](/handbook/security/security-assurance/security-compliance/) |
| [Generation of Test Cases for gitlab-assistant](https://gitlab.com/gitlab-com/gl-security/security-assurance/governance-and-field-security/governance/security-assurance-automation-subgroup/gitlab-assistant) |GitLab Duo | Generate basic and complex test cases for a Python module that standardizes scripting of solutions across the team when building automations and functionality for interactions with GitLab. The module introduces business logic beyond the basic API endpoint interactions. | [Security Assurance](/handbook/security/security-assurance/) |
| [GitLab Duo generated CVE descriptions](https://gitlab.com/gitlab-com/gl-security/engineering-and-research/automation-team/h1bot/-/merge_requests/46) | GitLab Duo | Generates CVE description from the imported HackerOne reports that can optionally be used in our CVE's. | [Application Security](/handbook/security/product-security/application-security/) |
| [Incident Summarization (/sirt_summary)](https://internal.gitlab.com/handbook/security/security_operations/sirt/platforms/slack/bots_commands/#sirtmanager) | Claude | Incident summarization slash command in Slack | [Security Incident Response Team (SIRT)](/handbook/security/security-operations/sirt/) |
| [Sir Tanuki](https://internal.gitlab.com/handbook/security/security_operations/sirt/operations/incident_response/sirtanuki/) (SIRT Incident Review Bot) | GitLab Duo | The SecOps Incident Reviewer (Sir) Tanuki is SIRT’s GitLab Duo-powered incident report reviewing tool. It works by leveraging GitLab Duo to analyze security incident issues and give feedback on the different sections of the issue description. | [Security Incident Response Team (SIRT)](/handbook/security/security-operations/sirt/) |
| [TLDR Customer Threat Detections](https://gitlab.com/gitlab-com/gl-security/security-operations/signals-engineering-public/tldr) | Claude | Signals Engineering uses Claude to generate new TLDR threat detections - a Slack slash command (/tldr) is available to kick off a new Claude written MR for review. | [Signals Engineering](https://internal.gitlab.com/handbook/security/security_operations/signals_engineering/) |
| [Signals Engineering Auto Metric Stats](https://gitlab.com/gitlab-com/gl-security/security-operations/signal-engineering/signal-engineering-automation/auto-sirt-metric-stats) | Claude | Every week before the weekly SET meeting, Claude auto-summarizes comments SIRT Engineers left when closing alerts during the past week which get added to a weekly detection digest issue | [Signals Engineering](https://internal.gitlab.com/handbook/security/security_operations/signals_engineering/) |

## AI Driven Process Efficiencies

| Process | AI Engine | Efficiency Details | Team |
|------|-----------|----------|------|
|Tableau Data Manipulation | Claude |Leverage Claude to generate syntax for calculated fields in Tableau to enable data manipulation. These fields enable us manipulate existing data and create new dimensions and measures to support the Security metrics program.  | Security Governance |
| Policy Generation and Optimization | Claude | Create the foundations of Security and Technology policies and reduce verbosity of policy language to align with Governance expectations. | Security Governance |
| Security Training Content Script Creation and Editing | Claude | Create scripts for AI created Security Training videos and editing of Security training content for readability and conciseness. | Security Governance |
| Blog and White Paper Optimization | Claude | Optimize the language and readability of blog posts and white papers to support a polished product for customers and the community. | Field Security |

## Ideas, Experiments and Tests

The security division works out of GitLab issues to keep track of AI-integrated ideas, experiments, and tests. Generally it is a good idea to add the `AI` GitLab label to issues for tracking.
