---
title: Integrations Support Pod
description: A dedicated group to work together on Integrations based tickets.
---

## Purpose

Creating a dedicated group to work together on Integrations based tickets.

This will allow everyone to gain more knowledge regarding the various GitLab integrations and an easier location to share the knowledge across regions.

## Current objectives

- Collaborate on tickets related to the [various GitLab Integrations we have](https://about.gitlab.com/direction/foundations/#integrations)
- Gain and share knowledge
- Documentation updates

## Support Pod members

- Lead: {{< member-by-name "Anton Smith" >}} (`@anton`)
- {{< member-by-name "Justin Farmiloe" >}} (`@jfarmiloe`)
- {{< member-by-name "Emily Chang" >}} (`@emchang`)
- {{< member-by-name "David Wainaina" >}} (`@dwainaina`)

## Collaboration channels

- Slack channel: [#spt_pod_integrations](https://gitlab.enterprise.slack.com/archives/C08VB43K9N0)
- Epic - https://gitlab.com/groups/gitlab-com/support/-/epics/145

## Create Integrations view

Since limitations in Zendesk prevent each pod from having a shared view, you will have to create one manually.
Follow the steps below and you should have a personal view in no time.

1. Click on `Manage views`
1. In the new Window on the top right click `Add view`
1. Give the view a nice name (`Integrations (All regions)`)
1. Move to `Conditions`
   1. `Tickets must meet all of these conditions to appear in the view`
      1. Click `Add condition` and from left to right
         - `Status`
         - `Less than`
         - `Pending`
      1. Click `Add condition` and from left to right
         - `Tags`
         - `Contains at least one of the following`
         - `support_category_integrations_datadog support_category_integrations_datadog_setup support_category_integrations_datadog_errors support_category_integrations_datadog_questions support_category_integrations_datadog_other support_category_integrations_gitpod support_category_integrations_gitpod_setup support_category_integrations_gitpod_errors support_category_integrations_gitpod_questions support_category_integrations_gitpod_other support_category_integrations_jira support_category_integrations_jira_setup support_category_integrations_jira_errors support_category_integrations_jira_questions support_category_integrations_jira_other support_category_integrations_plantuml support_category_integrations_plantuml_setup support_category_integrations_plantuml_errors support_category_integrations_plantuml_questions support_category_integrations_plantuml_other support_category_integrations_project_ support_category_integrations_project_asana support_category_integrations_project_bamboo support_category_integrations_project_discord support_category_integrations_project_emails_on_push support_category_integrations_project_github support_category_integrations_project_google_chat support_category_integrations_project_irker support_category_integrations_project_jenkins support_category_integrations_project_mattermost support_category_integrations_project_ms_teams support_category_integrations_project_status_emails support_category_integrations_project_pivotal support_category_integrations_project_prometheus support_category_integrations_project_slack support_category_integrations_project_unify_circuit support_category_integrations_project_webex support_category_integrations_project_webhooks support_category_integrations_project_other support_category_integrations_external_trackers support_category_integrations_external_trackers_bugzilla support_category_integrations_external_trackers_ibm support_category_integrations_external_trackers_redmine support_category_integrations_external_trackers_youtrack support_category_integrations_external_trackers_zentao support_category_integrations_external_trackers_other support_category_integrations_gmail support_category_integrations_gmail_setup support_category_integrations_gmail_errors support_category_integrations_gmail_questions support_category_integrations_gmail_other support_category_integrations_sourcegraph support_category_integrations_sourcegraph_setup support_category_integrations_sourcegraph_errors support_category_integrations_sourcegraph_questions support_category_integrations_sourcegraph_other support_category_integrations_trllo support_category_integrations_trllo_setup support_category_integrations_trllo_errors support_category_integrations_trllo_questions support_category_integrations_trllo_other support_category_integrations_visual_studio support_category_integrations_visual_studio_setup support_category_integrations_visual_studio_errors support_category_integrations_visual_studio_questions support_category_integrations_visual_studio_other support_category_integrations_akismet support_category_integrations_akismet_setup support_category_integrations_akismet_errors support_category_integrations_akismet_questions support_category_integrations_akismet_other support_category_integrations_kroki support_category_integrations_kroki_setup support_category_integrations_kroki_errors support_category_integrations_kroki_questions support_category_integrations_kroki_other support_category_integrations_mailgun support_category_integrations_mailgun_setup support_category_integrations_mailgun_errors support_category_integrations_mailgun_questions support_category_integrations_mailgun_other support_category_integrations_pim support_category_integrations_pim_setup support_category_integrations_pim_errors support_category_integrations_pim_questions support_category_integrations_pim_other support_category_integrations_recaptcha support_category_integrations_recaptcha_setup support_category_integrations_recaptcha_errors support_category_integrations_recaptcha_questions support_category_integrations_recaptcha_other support_category_integrations_other support_category_integrations_other_setup support_category_integrations_other_errors support_category_integrations_other_questions support_category_integrations_other_other 
1. Move on to `Formatting options`
   1. This is kind of up to your flavour but below are some suggestions.
      1. Next SLA breach
      1. Priority
      1. Preferred Region for Support
      1. Subject
      1. Organization
      1. Assignee
      1. Request date
      1. Latest update by assignee
1. Change `Order by` to `Next SLA breach`, `Ascending`
1. Click `Save`

Congratulations you now have a personal Integrations Pod View.
