---
title: SME Operations - Collaboration Project, Groups, Slack Channels

description: Describe SME Collaboration Projects, Google Groups and Slack Channels necessary for SME Program Operations

---

## StackOverflow (TBD)

The preferred channel is our [StackOverFlow for Teams](/handbook/solutions-architects/tools-and-resources/#stack-overflow-for-teams) within #cs-questions.

* Maintain List of SMEs (also in StackOverFlow) and SME Associates

Make sure that whoever is designated as an SME is listed as such in Stack Overflow. This will ensure that questions tagged with those relevant topics get routed to the right folks.

It should be part of the regular rigor that SMEs review questions in Slack (specifically #cs-questions) and Stack Overflow to ensure the answers are upvoted and relevant as new changes/features get released.

We can also use Stack Overflow for FAQs and Articles related to those particular areas.

TODO: Need to detail what exactly is the process to add SMEs to StackOverFlow

## SME Google Groups

Each SA Area Lead should set up SA and CS SME Google Groups for calendars. Have also both SA program Leads owners also, as a backup in case SA Area Lead is OOO

Use list of [SMEs](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/cs-subject-matter-experts/-/tree/main#who-are-the-current-smes-and-what-areas-are-they-focused-on) to form Groups

| SME Area                | SME Group                                                    |
|-------------------------|--------------------------------------------------------------|
| SME Area Leads Group    | sme-leaders    |
| AI                      | sme-ai         |
| Security & Compliance   | sme-appsec     |
| Dedicated               | sme-dedicated  |
| Plan                    | sme-plan       |
| CICD/Runner             | sme-ci         |
| Metrics & Observability | sme-metrics    |

**Vertical SME Google Groups**

| Vertical           | SME Group           |
|--------------------|---------------------|
| Embedded DevOps    | sme-embedded-devops |
| Financial Services | sme-finserv        |
| Healthcare         | sme-healthcare     |
| Telecommunications | sme-telco          |

## **SME Slack Channels** {#sme-slack}

To facilitate effective communication and collaboration between Subject Matter Experts (SMEs) and the field teams, the following Slack channel structure is recommended:

### SME Program Leadership Channel

Purpose: Async Coordination among SME Area Leaders on any changes or decisions made concerning the SME program.

| SME Area                       |  Slack Channels        |
|--------------------------------|------------------------|
| SME Program Leadership Channel |  #sme-program-leaders  |

### Channel for all SMEs in All Areas

Purpose: This is the main channel for all SME-related discussions and announcements. It serves as a central hub for:

* General SME program updates
* Cross-domain collaboration
* Sharing best practices and success stories
* Coordinating SME activities across different areas of expertise

| SME Area | Slack Channel             |
|----------|---------------------------|
| All SMEs | #subject-matter-experts   |

### SME Area Internal Slack Channels {#sme-internal}

Purpose: These SME Pod channels are mainly for SME Program Leads, SME Area Leads, SMEs and SME Associates. They are used for:

* Asynchronous meetings
* Discussions on architectural challenges
* Competitive analysis
* Identifying and addressing enablement needs
* Tracking and managing SME requests

| SME Area                  | Slack Channel           |
|---------------------------|-------------------------|
| AI                        | #sme-ai-internal        |
| Security & Compliance     | #sme-appsec-internal    |
| Dedicated                 | #sme-dedicated-internal |
| Plan                      | #sme-plan-internal      |
| CICD/Runner               | #sme-ci-internal        |
| Metrics & Observability   | #sme-metrics-internal   |

### SME Public Channels {#sme-channels}

These channels are open to all SMEs, Product Managers (PMs), and all field members. They serve to:

* A place for team members supporting customer evaluations of GitLab features
* Submitting SME requests for specific opportunities
* Coordinating SME involvement in customer engagements
* Asking product questions pertaining to specific subject matters

| SME Area                  | Slack Channel        |
|---------------------------|----------------------|
| AI                        | #sme-ai              |
| App Security & Compliance | #sme-appsec          |
| Dedicated                 | #sme-dedicated       |
| Plan                      | #sme-plan            |
| CICD/Runner               | #sme-ci              |
| Metrics & Observability   | #sme-metrics         |

**Vertical SME Public Slack Channels**

| Vertical              | Slack Channel           |
|-----------------------|-------------------------|
| Embedded DevOps       | #sme-embedded-devops    |
| Financial Services    | #v_finserve_global      |
| Telecommunications    | #sme-telecommunications |
| Healthcare            | #sme-healthcare         |

## SME Collaboration Projects

Each SME Area Lead should set up SME Collaboration project (See [AppSec Example)](https://gitlab.com/gitlab-com/customer-success/sa-sme-team-appsec-and-compliance)

| SME Area                    | Collaboration Project   |
|-----------------------------|-------------------------|
| SME Program Logistics       | [SME Program Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/cs-subject-matter-experts) |
| AI                          | [AI SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/ai-sme)                       |
| AppSec                      | [App Security SME Project](https://gitlab.com/gitlab-com/customer-success/sa-sme-team-appsec-and-compliance)         |
| Dedicated                   | [Dedicated SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/sa-sme-team-dedicated) |
| Plan                        | [Plan SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/agile-planning-sme)         |
| CICD/Runner                 | [CI/CD SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/cs-sme-ci)                    |
| Metrics & Observability     | [Metrics SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/metrics-analytics-and-observability-sme)  |
| Aerospace Vertical          | [Aerospace SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/aerospace-sme)        |
| Automotive Vertical         | [Automotive SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/automotive-sme)|
| Embedded DevOps Vertical    | [Embedded DevOps SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/embedded-devops-sme) |
| Healthcare Vertical         | [Healthcare SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/healthcare-sme) |
| Financial Services Vertical | [Financial Services SME Project](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/financial-services-sme) |
| Telecommunications Vertical | [Telecommunications SME PRoject](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/telecommunications-sme)|

### SME Metrics {#sme-metrics}

To effectively measure the impact and success of the SME program, we will track the following metrics:

1. Technical Win Rate:
   * Metric: Percentage of wins in opportunities with SME involvement using SA Activity type SA Assistance - Subject Matter
   * Calculation: (Number of won opportunities with SME engagement / Total number of opportunities with SME engagement) * 100
   * Goal: Increase win rate by 10% compared to baseline within 12 months
2. Knowledge Transfer Effectiveness:
   * Metric: Number of SME-led training sessions, knowledge base articles created and shared, and training session survey results
   * Calculation: Sum of training sessions conducted, articles published by SMEs, and session survey results average rating
   * Goal: Minimum of 4 training sessions and 10 knowledge base articles per quarter
3. Stack Overflow Engagement:
   * Metric: Response rate and quality of SME answers on Stack Overflow
   * Calculation: (Number of SME responses / Total number of relevant questions) * 100; Average upvotes per SME answer
   * Goal: 90% response rate to relevant questions; Average of 5 upvotes per SME answer

Reporting and Analysis:

* Generate quarterly reports to track progress and identify trends using visualization tools
* Based on reports and survey data, conduct quarterly reviews to assess SME program effectiveness and make necessary adjustments

By consistently tracking and analyzing these metrics, we can ensure the SME program's continuous improvement and show its value to the organization.

## New SME Area of Expertise Process

TBD - Define the process to determine whether a SME Area of Expertise should be established or not.

These are the differences between SMEs Areas of Interest and Formal SME Programs

| <br><br> | SME Area of Interest | Formal SME Areas |
|---|---|---|
| <br><br> | 1. CICD/ Runners<br>2. Metrics & Observability<br>3. Embedded Systems | 1. AI<br>2. App Security<br>3. Dedicated<br>4. Plan |
| Leadership Structure | No official SME Area Leader, or SMEs.<br>Can be a pool of interested folks of SME Associates.<br>One person driving program | [x] SME Area Leads<br>[x] SMEs<br>[x] SME Associates |
| Operations | [ ] Formal List of SA and CS SMEs<br>[x] List of SME Associates or Interested Folks<br>[ ] SME Google Groups<br>[x] Slack Channels - General<br>[ ] Slack Channel - Request a SME<br>[ ] Collaboration Project<br>[ ] StackOverFlow | [x] Formal List of SA and CS SMEs<br>[x] List of SME Associates<br>[x] SME Google Groups<br>[x] Slack Channels - General<br>[x] Slack Channel - Request a SME<br>[x] Collaboration Project<br>[x] StackOverFlow |
| Cadences | [ ] ARR Driver<br>[ ] SME Area Leads Meetings<br>[x] SME Area Pod Cadences<br>[ ] PM/ SME Area Cadences<br>[x] PM Roadmaps<br>[x] Technical Skills Exchange<br>Meetings can be in the form of trainings, async, office hours etc<br> | [x] ARR Driver<br>[x] SME Area Leads Meetings<br>[x] SME Area Pod Cadences<br>[x] PM/ SME Area Cadences<br>[x] PM Roadmaps<br>[x] Technical Skills Exchange |
| Process to Request a SME | No | Yes |
| Customer Feedback Mechanisms | No | Yes (with Issue Boards etc) |
| Engagement with PM | Some | Yes |

Once a SMEs Ares of Interest becomes a formal SME Programs These are the tasks needed to complete setup:

* Selection of SME Area Leads, SMEs
* Who decides on new SME Area
* Rollout to SA and CS Community
* Enrolling PMs
* Maintain List of SA SME Participants - Confirm List of [SMEs](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts/cs-subject-matter-experts/-/tree/main#who-are-the-current-smes-and-what-areas-are-they-focused-on)
* Maintain list of potential SMEs (SME Associates) as a pool for each area
* Create the necessary SME google groups for calendar purposes
   1. Open an [Access Request](/handbook/security/corporate/end-user-services/onboarding-access-requests/access-requests/) with IT to have the Google Group created.
   2. Use the same naming convention as other SME areas, provide the DRI's as Group Owner and Group Manager. You can clone this [issue](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/34007) as an example.
   3. Once the Google Group has been created by IT the group owner/manager can navigate to the Google Groups page to add SME's as group members.
* Set up Stack OverFlow with SMEs to answer questions.
* Set up SME Collaboration project
   1. Navigate to the [SME Subgroup](https://gitlab.com/gitlab-com/customer-success/subject-matter-experts)
   2. Click **New Project**
   3. Create your project using the same naming nomenclature as the other projects in the subgroup
* Set up both a public SME Slack Channel for the field and a private internal channel for the SME pod using the naming conventions outlined above (example *#sme-(area)* and *#sme-(area)-internal*)
* Update Handbook on SME Operations
