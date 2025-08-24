---
title: Sending Notices
category: GitLab.com
description: How to send notices out to GitLab.com users and customers to inform them of various actions on namespaces under their control
---

## Overview of the process

At times the [Support team will be asked to send notices](/handbook/support/internal-support/#contacting-users-about-gitlab-incidents-or-changes) to GitLab SaaS users or customers to inform them of actions that we have taken (or will be taking) on namespaces or projects under their control.

This workflow describes how to fulfill different types of contact requests and the helpful tools you can use in the process.

## Tools and Approvals

| Number of users | Which thing to use | Approvals required | Notifications required |
| --- | --- | --- | --- |
| 1-2 | [Manually create a Zendesk ticket](#manually-create-a-zendesk-ticket) | None | None |
| 3+ | [Mass Emails through Marketing Department](#mass-emails-through-marketing-department) | Director | [Support Preparedness issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/new?issuable_template=Support%20Preparedness) + FAQ |

- Support team can be asked to contact users **during an incident**. Such requests are filed by infra team [using `confidential_incident_data` issue template](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/new?issuable_template=confidential_incident_data) in [production](https://gitlab.com/gitlab-com/gl-infra/production/-/issues/) issue tracker. These must be fulfilled by CMOC during the shift.
- As a [Stable Counterpart](../support-stable-counterparts.md) you may choose to manually create tickets for a higher number of users at your discretion. This should be done solely for technical matters ("your usage is causing issues, may we suggest a different approach"), never for marketing reasons ("we have a new way to do xyz and would like you to adopt it").

## Avoid sending RED data

In all outbound contact requests explicitly avoid sending RED data. (see: [Data Classifaction Standard](/handbook/security/standards/data-classification-standard/)). This avoids:

- data transposition errors (accidentally sending another customers data to a customer)
- customer-internal data leaks (person `x` who received the email was not authorized to know about project `y`)
- putting customer RED data into systems where it is not allowed (system `z` is only classified for YELLOW data, but is used to send RED)

If there is any doubt about whether a particular piece of data is appropriate to send, start with asking in `#support_leadership` and escalate to `#privacy-team_help` / `#security` as required.

Some examples:

- **Don't** send the full path (for example, `/big-co/sub-proj/super-secret-project`), instead send the project/namespace ID and instructions for translating it.

### Tips for avoiding RED data in notices

- Make use of the built-in [Project](https://docs.gitlab.com/user/project/working_with_projects/#access-a-project-by-using-the-project-id) and [Group](https://docs.gitlab.com/user/group/#access-a-group-by-using-the-group-id) redirects when sharing a link to the resource. They will be redirected if the user has appropriate permissions to view the resource.
  - Project example: `https://gitlab.com/-/p/278964` will redirect to `https://gitlab.com/gitlab-org/gitlab`.
  - Group example: `https://gitlab.com/-/g/9970` will redirect to `https://gitlab.com/gitlab-org`.

## How to send notices

Most notices should be sent in the form of Zendesk tickets. Always send these tickets to users with `Owner` level permissions in the namespace or project in question.

Most contact requests will involve contacting all of the owners of only one project or only a few specific users. If you're tasked with contacting the owners of a project and know that there's only one, feel free to look up their email address using your admin account or [ChatOps](/handbook/support/workflows/chatops/#user).

However, some contact requests may involve contacting all of the owners of multiple projects. Support Engineers should direct requests for reaching out to multiple owners across multiple projects to do [Mass Emails through Marketing Department](#mass-emails-through-marketing-department)

Make sure to [add an admin note](/handbook/support/workflows/admin_note/) on a user/group we took action on. This will ensure that we can track a block/change reason if a user reaches out to us using a different channel.

### Manually create a Zendesk ticket

**Warning** This often requires the ability to *create users* in Zendesk, which
is only available on specific roles i.e. CMOCs. That access is *very* risky and
should only be used as documented in this section.

**Note** This only applies to Zendesk Global at this time.

When you need to send an outbound request, it must be done in a very specific
manner to ensure it routes properly and the end-user we wish to contact receives
the correct notification.

To do this, start by hover over the `+ Add` at the top-left of Zendesk and then
click `Ticket`.

The first thing you need to do is select the requester. To do this, click in the
text box below `Requester` at the top-left of the page and put the email you are
looking to reach out to.

The action taken next depend on whether the user in question exists or not:

- If the user exists, it will show said user in a drop-down (clicking said entry
  in the drop-down will select the user).
- If the user does not exist, no results will be found and you will need to
  click the `+ Add user` link in the drop-down. Doing so will bring up a modal
  where you will enter the name and email of the user to create. If you are
  unsure of the name, it is always safest to use the email itself for both the
  name and email field. Click the blue `Add` button to create the user.
  - **Warning** Never create a user in any other fashion. This is the one and
    only way a user should ever be manually created within our support system by
    any team other than Support Readiness. Never utilize this method when CC'ing
    a user.

After doing this, you should add the subject of the ticket. This should always
be done via the top-center part of the page.

After filling out the subject, you now need to apply the macro
`General::Outbound Contact Request`. This step is **vital** and should never be
skipped. This macro will ensure the ticket is setup properly for an outbound
request. Skipping this step can result in the new ticket not routing properly
and encountering an untold number of problems.

After this has been done, you will then enter the description for the ticket.
This is the core of the message you are wanting to send to the end-user.

Once this has been completed, the last step is to then finish creating the
ticket by submitting it as *pending*. This is done by clicking the downward
arrow at the bottom-right of the page and clicking `Submit as Pending`.

### Mass Emails through Marketing Department

Outside of Zendesk we may be asked to be involved in the process of sending mass notices to users. For larger email campaigns, involve the marketing team:

1. [Open an issue](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new?issuable_template=request-operational-email) in the [marketing/marketing-operations](https://gitlab.com/gitlab-com/marketing/marketing-operations) issue tracker using the `request-operational-email` template. You may also need to create a supplementary issue using [request-target-list template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new?issuable_template=request-target-list).
1. Fill the template out in its entirety.
1. Submit the issue and be ready to adjust the subject and/or body of the notice based on feedback.

Note that this process requires a number of approvals from the management, so plan ahead and make sure that the issue is completely ready for review at least one week before sending out emails.

## Tools

The following tools can be used to facilitate different types of contact requests.

### Email Grab Script

The [Email Grab Script](https://gitlab.com/gitlab-com/support/runbooks/-/blob/master/code/group_project_user_owner_emails.rb) is a Ruby script that will return the primary email addresses of the owners of a group or project. Currently, it can only be used if you possess a GitLab SaaS admin account. It can also be supplied only a list of usernames, in which case it will return the primary email addresses of those users. To use it:

1. Install the required [labclient](https://rubygems.org/gems/labclient/versions/0.5.1) gem with `gem install labclient`.
1. Copy the script to your local machine and give it a name, like `emailgrab.rb`.
1. Replace `YourSuperSweetPAT` with a `read_api` scoped PAT from your GitLab SaaS admin account.

- **Note**: If a new PAT was created from an admin account, that account will receive a slack message from the SIRTbot app asking if the PAT creation was legitimate. Remember to fill this out for security auditing.

1. [Comment out](https://docs.ruby-lang.org/en/3.0/syntax/comments_rdoc.html) the sections of the script that you will not be using, either `groups`, `users`, or `projects`.
1. Add your data to the section you will be using.
1. Run the script with `ruby emailgrab.rb`.

The results will be created as `namespace-contacts.csv` in the same directory that the script is located in.
