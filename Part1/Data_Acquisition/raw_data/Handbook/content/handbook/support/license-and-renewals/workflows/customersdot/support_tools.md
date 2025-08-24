---
title: CustomersDot Admin Support Tools
category: CustomersDot
description: How to use the CustomersDot Admin Support Tools for L&R requests.
---

## Overview

This workflow details how to use the CustomersDot Admin Support Tools for L&R related tasks.

The CustomersDot Admin Support Tools implementation is tracked in this [epic](https://gitlab.com/groups/gitlab-org/-/epics/6828).

## Where the tool is located 

The CustomersDot Admin Support Tools can be found by logging into https://customers.gitlab.com/admin. Then scroll down to the **Support** section in the left panel.

In the **Support** section you will have the following tools to select from:

### Namespace Controls (SaaS)

There are different tabs for namespace control. 

> **Important**: Please double check and take note of the Additional computes minutes and Storage **BEFORE** and **AFTER** making the change.

View the namespace as an admin, [using the API](https://docs.gitlab.com/api/namespaces/), or with the [Zendesk Super App](/handbook/security/customer-support-operations/docs/zendesk/apps/#gitlab-super-app)

#### Set extra CI minutes

Allows setting additional compute minutes to a customer namespace to the value specified in the `New minutes total` field.

> **WARNING:** Additional compute minutes added this way will last **indefinitely** until used. If the request is to provide "extra compute minutes" during the trial period only, use the Manage GitLab Plan and Trials option which will change the *usage quota* to match a paid plan quota for the duration of the trial. We have an [open issue 13063](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/13063) to allow editing monthly quotas for trial plan.

The form has three required fields:

- **Namespace ID/Path**: The customer namespace path as it appears in the URL or its ID.
- **New minutes total**: The value of compute units to set. If you want to add X amount of compute units to a namespace:
  - Check the current "Additional Units" value (Y)
  - Add the current units (Y) + the new units you want (X)
  - Enter this total in the "New minutes total" field
For example, to add 1000 units to namespace with a total of 6000 Additional Compute Units, set the "New minutes total" field to 7000.   (***Note:** This will update the 'Additional Units' value in the namespace's 'Usage Quotas' page.* )
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

##### Bypassing credit card validation for pipeline execution

*Previously known as: `Enable CI Minutes`*

Remove the restrictions for using compute minutes for groups who are part of a sales assisted trial. This should not be confused with [credit card validation when creating a GitLab.com account](/handbook/support/workflows/reinstating-blocked-accounts/#accounts-unable-to-verify-with-a-credit-card-andor-phone-number). To remove the restriction, we add 10 additional compute minutes to the namespace if the namespace does not have any of the additional compute minutes.

- **Namespace ID/Path**: The customer namespace path as it appears in the URL or its ID.
- **New minutes total**: 
  - Check the current "Additional Units" value.
  - If the "Additional Units" is 0 or does not exist, set the value to 10.
  - If there is already "Additional Units", there is no need to update the "Additional Units". If in doubt, ask in slack for further guidance.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

#### Set additional storage

Sets [additional storage](https://docs.gitlab.com/user/usage_quotas/#excess-storage-usage) for a namespace to the value specified in the `New extra storage (MiB)` field

- **Namespace ID/Path**: The customer namespace path as it appears in the URL or its ID.
- **New extra storage (MiB)**: The new value of storage to set, in MiB
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

> Note: As storage is entered as MB, consider that GB is presented in the UI for large numbers. For example: `10000 MB = 9.76 GB`. For '10 GB of storage', you should instead use `10240`, as `10240 MB = 10 GB`

#### Clear Subscription

Unlink a group from a subscription. Note: The group will be downgraded to Free if the subscription being unlinked is a Premium or Ultimate subscription.

- **Subscription ID/name**: The subscription ID/name to be removed from a namespace.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

#### Force Associate

Associates a group with a subscription. All fields are required.

- **Namespace ID/Path**: The customer namespace path as it appears in the URL or its ID.
- **Subscription ID/name**: The subscription ID/name to be removed from a namespace.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

#### Reset max seats

Modifies the highest number of seats used on the namespace during the current subscription term.  This should typically only be used during the [reset max seats for QSR workflow](/handbook/support/license-and-renewals/workflows/quarterly_subscription_reconciliations/#resolving-max-seats-overages)

##### Note

This will change the total seats owed in the GitLab.com subscription. Before using this option check with a support manager.

- **Namespace ID/Path**: The customer namespace path as it appears in the URL or its ID.
- **Max Seats number**: New value for max seats.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

### Support Audit Events

The Support Audit Events page serves as a comprehensive audit log that tracks and documents all activities performed through the Support Admin Tools. This page provides a chronological record of administrative actions, allowing support team members and administrators to review who did what and when within the support system.

Key features of this page include:

- Action entries for the specific support admin tools used
- Namespace ID, if the action is performed on a namespace
- Request link shows the relevant Zendesk link for the action
- Requester showing who performed each action
- Timestamped entries of all support admin actions

Use the **Add filter** button at the top right of the page to select specific field to search.

### Trial Changes (SaaS)

Updates namespace trial. You can use it for the following cases:

1. Cancel trials
1. Trials
    1. Change Plan
    1. Renew/extend Date

Please note that in order to extend or renew a trial, the customer **MUST** have an active trial because a CustomersDot account needs to exist.  If the prospect has not yet initiated a trial themselves, please have them do so via the group billing page (https://gitlab.com/groups/[NAMESPACE-PATH]/-/billings).

#### Cancel Add-on Trial

This tool is applicable when a namespace already has a Premium or Ultimate plan and they trial Duo Enterprise or Duo Pro on the namespace. The tool will remove the Add-on Trial (Duo Enterprise or Duo Pro) from a namespace without affecting the Premium or Ultimate plan.

- **Namespace ID/Path**: The customer namespace path as it appears in the URL or its ID.
- **Add-on name**: Select the relevant Add-on name from the dropdown list.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

#### Update or Cancel a Trial

Search for the specific trial or the namespace. 

##### Update 

Select the **Edit** ![icon](https://gitlab.com/gitlab-org/gitlab-svgs/-/raw/main/sprite_icons/pencil.svg)

- **End Date**: The updated date the plan will end.
- **Plan**: The trial plan that you would like applied for the customer's group.  If the `x Clear` option is selected, the customer's namespace will immediately be downgraded and the trial ends.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

##### Cancel

Select **Cancel trial** ![icon](https://gitlab.com/gitlab-org/gitlab-svgs/-/raw/main/sprite_icons/cancel.svg)

- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

### Trials for SM

Creates a legacy trial license that expires on the selected date and emails it to the customer's address provided in the form.
The use of this feature should be limited for any emergency license requests when L&R is unavailable, such as during the weekends.

- **Email**: The email where the license will be sent. We recommend sending the license to the ticket requester's email, unless specified otherwise.
- **Users count**: Total number of users in the license.
  - For Self-Managed licences, GitLab will refuse to install a license key with less than the current number of billable users. Therefore, **User Count** for a trial license should *at least* be the same number as the current number of billable users plus any true-ups owed (if any).  For example, if 25 current billable users, and 5 true-ups owed, set **User Count** to at least 30.
- **Plan code**: The plan for the license.
- **Starts at**: The license start date.
- **Expires at**: The license expiry date.
- **Note**: Additional note if any.
- **Zendesk ticket link**: The link to relevant Zendesk ticket where the request is made.

Please note that the license email will mention `10-day Trial GitLab License`, it is recommended to set the expiry date 10 days from now to avoid confusion. We have an [issue](https://gitlab.com/gitlab-org/customers-gitlab-com/-/issues/12035) to remove unnecessary field like **Starts at** and **Expires at**.

### Unlink GitLab.com Account

Unlinks the GitLab.com account that is tied to the CustomersDot account provided.

- View the CustomersDot account
- Click on `Unlink GitLab User` tab
- Verify the GitLab.com account information is correct
- Provide the Zendesk ticket link where the request is made 
- Click `Confirm`
