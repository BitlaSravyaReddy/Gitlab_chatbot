---
title: CustomerDot Account Related Problems
category: CustomersDot
description: Using the customer console for internal requests is only for special cases where the existing tools won't allow us to complete the task at hand.
---

## Overview

Sometimes customers have trouble accessing their account.
CustomersDot email and password log in has been deprecated.
Customers can instead [follow these steps](https://docs.gitlab.com/subscriptions/customers_portal/#sign-in-to-customers-portal) to log in using a one-time sign-in link.

### 1. Customer cannot sign in even after password reset

This could be because the password reset email was requested from [https://**gitlab.com**/users/password/new](https://gitlab.com/users/password/new).
We can confirm this by searching through the mailgun log. To locate the password reset email:

1. Log in to Mailgun using your account
1. On the left panel, expand `Sending` and go to `Logs`
1. On the top left, click the `Domain` dropdown and choose `mg.gitlab.com` domain to confirm that the password reset email was requested on GitLab.com.
1. If the customer is unable to log in using their GitLab.com account, request them to log in using a **one-time sign-in link**.

### 2. The CustomersDot account has not been confirmed

When the account is not confirmed, the customer cannot log in. To view whether an account is confirmed:

1. Sign into CustomerDot with your admin account
1. Find the customer account
1. Click on the `i` icon on the customer account or `Show` if you're already viewing the account
1. The confirmation is shown in `Confirmed at` field
1. If the customer has not confirmed their email/account, we can resend the confirmation email using [this form](https://customers.gitlab.com/customers/confirmation/new) and get back to the customer.

### 3. The customer is trying to sign in using another email address

Situations may arise where a customer has used a different email address for their [customers portal](https://customers.gitlab.com/customers/sign_in) account and their GitLab.com account. It may also be possible that a customer has signed up more than once using different email addresses (e.g. `firstname_lastname@organization.com` and `firstname.lastname@organization.com`). In scenarios such as these, please explain the differences to the customer, and clarify which email address they used for their GitLab subscription.

### 4. Unlinked CustomersDot account

Let's say a Customer X has an existing Customers Portal account with their email <customerX@example.com> either because:

- They had a legacy Customers Portal account that was manually created before GitLab SSO was enforced
- Or their account was created as part of a sales assisted purchase

🔧 Customer X needs to log in to their [Customers Portal](https://customers.gitlab.com/customers/sign_in) account using a [one-time sign-in link sent to their email](https://docs.gitlab.com/subscriptions/customers_portal/#sign-in-to-customers-portal) and [link their GitLab account](https://docs.gitlab.com/subscriptions/customers_portal/#link-a-gitlabcom-account)

### 5. Unlinked CustomersDot account for purchases via Sales

Let's say a Customer Y purchases a subscription through Sales. Their signed Order Form has the **Sold To** contact's email as <customerY@example.com>.
Once the Quote is processed, Zuora's [callout service](https://gitlab.com/gitlab-org/customers-gitlab-com/-/blob/main/doc/zuora/zuora_callouts.md#purpose)
triggers an account creation on Customers Portal. This service uses the `Sold To` contact's details to create the account.

For various reasons, the created Customers Portal account is not linked to a GitLab account.
For example:

- The subscription has not yet been applied to a group.
- Support used [CustomersDot Support Admin Tools force associate workaround](/handbook/support/license-and-renewals/workflows/customersdot/support_tools#force-associate) to bypass the need to have a linked GitLab account to apply a subscription and the customer never linked their GitLab account.

🔧 Customer Y needs to log in to their [Customers Portal](https://customers.gitlab.com/customers/sign_in) account using a [one-time sign-in link sent to their email](https://docs.gitlab.com/subscriptions/customers_portal/#sign-in-to-customers-portal) and [link their GitLab account](https://docs.gitlab.com/subscriptions/customers_portal/#link-a-gitlabcom-account).

### 6. Linked accounts have different emails

Let's say a Customer Z has an existing Customers Portal account (<customerZ@example.com>) either from an existing purchase or by creating a new account.
And this Customers Portal account has been linked to a GitLab account (check the `GitLab Groups` tab) whose email is <gitlabZ@example.com>.
*This could be someone else's GitLab account or Customer Z might have multiple GitLab accounts or multiple emails in their GitLab account.*

🔧 Customer Z needs to log in to their [Customers Portal](https://customers.gitlab.com/customers/sign_in) account and either:

- [Change the linked GitLab account](https://docs.gitlab.com/subscriptions/customers_portal/#change-the-linked-account) to the GitLab account with email <customerZ@example.com>
- Or update the email in their Customers Portal account to match the email in the linked GitLab account, which is <gitlabZ@example.com>.

Because we try to keep the CustomersDot account email with GitLab account email have a one-to-one mapping, consider offering the addition of multiple CustomersDot accounts to the customer's billing account.

In this case, we can recommend the following steps:

1. Unlink the GitLab account whose email is <gitlabZ@example.com> from the CustomersDot account whose email is <customerZ@example.com>.
2. The customer should then create a CustomersDot account using the GitLab account whose email is <gitlabZ@example.com>.
3. We add the new CustomersDot account whose email is <gitlabZ@example.com> to the billing account.
4. Additionally, the customer can also create a GitLab account with the email <customerZ@example.com> then [link it to the CustomersDot account whose email is <customerZ@example.com>](https://docs.gitlab.com/subscriptions/customers_portal/#link-a-gitlabcom-account).
