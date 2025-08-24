---
title: Account Ownership Verification
category: GitLab.com
subcategory: Accounts
description: "Workflow detailing how and when to verify account ownership including disable 2FA"
---

## Overview

This workflow covers how a user can provide account verification. It should be used for any [account changes](../workflows/account_changes.md).

Account actions can only be completed if the [workflow](#workflow) below is successful.

## Related topics

### User Account Verification

GitLab.com requires that users without 2FA enabled verify their email address when a login attempt meets certain high-risk criteria. For users requesting support when their email address is no longer valid and are unable to receive the email, please see the [Email account lost workflow](/handbook/support/workflows/lost_emails).

If the user has questions about the email, phone, or credit card verification GitLab is requiring, please refer to the [Internal Handbook for the workflow](https://internal.gitlab.com/handbook/support/workflows/phone-number-verification/) to follow.

### GitLab Team Members

If the user is a GitLab team member, have them [contact IT Ops](/handbook/security/corporate/end-user-services/_index.md).

## 2FA removal within GitLab

See the [2FA Removal workflow](../workflows/2fa-removal.md) for instructions to process 2FA removal requests.

## Workflow

The workflow applies to all cases where account verification is required, aside from 2FA removals.

### Keeping the Ticket Simple and Accurate

Because an ownership-verification ticket is a matter of record, the ticket must be simple, accurate, and tightly focused on the access issue.
Do not allow the customer to bring up unrelated topics.

### Step 0: Ticket metadata

Ensure that the ticket form, category, subcategory, and topic are accurate.

Most SaaS Account categories have automations or triggers.

#### Account verification matrix

The table below provides a summary of the available verification options based on the owner and user type:

| Requester | Target | Challenges | Support PIN | Notes |
| --- | --- | --- | --- | --- |
| Enterprise Owner | Own account | Owner passes challenges on own account | Support PIN must be provided by a different owner | If no other owner is available for vouch, see [internal handbook](https://internal.gitlab.com/handbook/support/#account-verification-challenge-questions) for other challenges. |
| Enterprise Owner | Member of paid group or intent to be added or Enterprise User | Owner or target user passes challenges on their own account | Support PIN is from requesting owner |  Multiple enterprise users may be handled per ticket. Target user does not have to be CCed on ticket. |
| Owner | Non-enterprise user | Target user passes challenges on own account | Support PIN from owner | One user per ticket. Communication is direct from the target user who must be CCed on ticket.  |
| Paid User | Own account | User passes challenges on own account | N/A | If owner is needed, owner must open a new ticket. |
| Paid User | Other member of same paid group | Target user passes challenges on own account | N/A | If owner is needed, owner must open a new ticket.|
| Free User | Non-member of group with intent to be added | Not allowed - request must come from group owner | Owner vouch required |  |

See the [Enterprise User section](../workflows/gitlab-com_overview.md#enterprise-users) on how to identify if a user is an Enterprise User.

### Step 1: Sending Challenges

If you need a basis for a response where you send the challenges, use the [`Support::SaaS::Gitlab.com::Account Ownership Verification - GitLab.com` macro](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/Account%20Ownership%20Verification%20-%20GitLab.com.md?ref_type=heads).

### Step 2: Checking challenge answers

> **Note**: In case the user sends back very minimal information and it's clear it's not sufficient or the answers are vague, reply asking for more information immediately after their response. You can provide some additional guidance, such as "please provide the exact date and time of the commit, not just an approximate one".

1. To verify the challenge answers, use the Zendesk GitLab User Lookup App or, for those who have admin access, check at `https://gitlab.com/admin/users/USERNAME`.
1. Use the ZenDesk [GitLab Super App's](/handbook/security/customer-support-operations/docs/zendesk/apps/#gitlab-super-app) `2FA Helper` or `2FA validator` to determine the [risk factor](https://internal.gitlab.com/handbook/support/#risk-factors-for-account-ownership-verification) (GitLab internal) based on the user's answers. Data classification criteria and any notes are in the [GitLab Internal Handbook - Data Classification table](https://internal.gitlab.com/handbook/support/#data-classification), which is considered the source of truth.
   - Challenge answers must be evaluated against a paid namespace if the user is a member of any paid namespace. If the user is not a member of a paid namespace, refer to [Conditions for 2FA Reset Consideration](../workflows/2fa-removal.md#conditions-when-account-is-used-to-access-customers-portal) for further guidance.
   - If a group owner is answering on an [enterprise user's](/handbook/support/workflows/gitlab-com_overview#enterprise-users) behalf, see the [Account verification matrix](#account-verification-matrix) for which account to evaluate the answers against. Even if the Enterprise user is not a current member of the paid namespace, the data classifcation is RED.
   - If you need to leave a comment manually (instead of through the app), use the [`Support::SaaS::Gitlab.com::2FA::2FA Internal Note` macro](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/2FA/2FA%20Internal%20Note.md?ref_type=heads) to put an internal note on the ticket.

1. **If verification passed:** Request that your decision be peer-reviewed by another member of the team through Slack `#support_gitlab-com`. They will perform the steps in 3a
1. **If the verification failed**: Move to step 3b

### Step 3a: User successfully proves account ownership

This section is typically done by the peer reviewer. If needed, the peer reviewer (or approving manager) may leave an approval note, in which case the original reviewer will perform the actions.

1. If you agree with the decision, sign into your admin account and locate the username in the users table or by going to `https://gitlab.com/admin/users/usernamegoeshere`
      1. Please see [Account Changes workflow](../workflows/account_changes.md).
      1. Under the account tab, click `Edit`, add an [Admin Note](../workflows/admin_note.md), and save.

### Step 3b: User Fails to Prove Account Ownership

> **Note**: Do *not* provide hints to answers, or let the user know which challenges they got right or wrong. That is how social engineering works!

1. If the user is unable to pass the risk factor but we have not provided all the applicable challenges, you may offer further challenges. This is true for all users, including owners.
   - Most commonly, an `Owner in the top level namespace` (with a valid subscription) vouch is requested. Use the [`Support::SaaS::Gitlab.com::2FA::2FA ask owner vouch` macro](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/2FA/2FA%20Ask%20owner%20vouch.md?ref_type=heads). See the [Verifying an Owner Vouch section](#authenticating-an-owner-vouch) for more information. The originating email of this request should match a verified email of the Owner's account. If the user is an Owner, vouch must be from a different Owner.
   - Some challenges can be answered with the help of their colleagues. Use the [`Support::SaaS::Gitlab.com::2FA::2FA Removal Verification - GitLab.com - Failed - Ask colleagues for help` macro](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/2FA/2FA%20Removal%20Verification%20-%20GitLab.com%20-%20Failed%20-%20Ask%20colleagues%20for%20help.md?ref_type=heads) to let them know which challenges they can try to work with their colleagues to answer.
   - When we receive a subsequent response, go back to [evaluating the challenges](#step-2-checking-challenge-answers) to see if they now pass.
1. If the user is unable to pass the available challenges:
   1. Inform them that without verification we will not be able to take any action on the account. For 2FA, use the [`Support::SaaS::Gitlab.com::2FA::2FA Removal Verification - GitLab.com - Failed - Final Response` macro](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/2FA/2FA%20Removal%20Verification%20-%20GitLab.com%20-%20Failed%20-%20Final%20Response.md?ref_type=heads).
   1. Mark the ticket as "Solved".

#### Authenticating an Owner Vouch

In a paid namespace: If the user elects to have an Owner vouch for their request, apply the macro [`Support::SaaS::Gitlab.com::2FA::2FA ask owner vouch`](https://gitlab.com/gitlab-com/support/zendesk-global/macros/-/blob/master/active/Support/SaaS/GitLab.com/2FA/2FA%20Ask%20owner%20vouch.md?ref_type=heads). This will direct the requester to have an Owner (top-level) create a Snippet with a Support-provided string. Once they have replied verifying they have done so:

1. Use your Admin or Auditor account to browse to the Snippet provided (for example `https://gitlab.com/-/snippets/2057341`)
   - Verify the text of the Snippet matches the string you specified
   - Verify that the author of the Snippet is an Owner and direct member of the top-level paid group
1. If the Owner passes, you may count this towards the account verification challenges.

Note: Due to this [bug](https://gitlab.com/gitlab-org/gitlab/-/issues/337939) some group owners are not able to create snippets. In that case, we can ask the Owner to generate and share with us a [Support PIN](https://docs.gitlab.com/user/profile/#generate-or-change-your-support-pin) instead.

If another user is CCed on the ticket, once you've verified the PIN ask them to generate a new PIN to revoke the previous one.

## Account Ownership Changes

This section has been [moved to the Account Changes workflow](../workflows/account_changes.md#account-ownership-changes).
