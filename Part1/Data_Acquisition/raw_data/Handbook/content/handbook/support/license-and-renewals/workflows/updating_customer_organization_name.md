---
title: Updating customer organization name
category: General
description: This page is about steps to updating customer's organization name.
---

## General workflow

Updating company name would involve updating information on:

1. [CustomersDot](https://customers.gitlab.com/customers/sign_in)
1. SFDC
1. Zuora

Before processing the request, please ask the customer for **legal proof of organization name change** *and* **previous invoice**.

We can provide the following instruction to update the [CustomersDot](https://customers.gitlab.com/customers/sign_in) information:

1. Sign into [customers portal](https://customers.gitlab.com/customers/sign_in)
1. [Follow the steps to change the company information](https://docs.gitlab.com/subscriptions/customers_portal/#change-your-company-details).

This will update future auto-generated invoices. Updating the information in CustomersDot would trigger a sync to update `Zuora` as well.

To change the name in `SFDC`:

1. Find an open Opportunity in the SFDC Account.
1. [Follow the steps here](/handbook/legal/customer-negotiations/#how-to-reach-the-legal-commercial-team) to open a `Legal Request`.
   - Select `Assignment/Transfer/Novation Agreement` as the `Type of Legal Request`.
   - Select `Assist with answering legal question or questionnaire` under `Summary of actions(s)`.
   - Enter the Zendesk ticket link and a summary of the request in the `Notes` field.
   - Upload the legal proof of organization name change document shared by the customer.
1. After getting the approval from Legal, open a Sales Ops case:
   - From the SFDC account page, click on `Request Support`.
   - Choose `Sales Ops` and click `Next`.
   - Choose `Account name changes` under `General Account Support` dropdown list.
   - Copy and paste the link to the Legal case above.
   - Click `Submit`

Once you get a confirmation from Sales Ops, confirm that the Organization name in Zendesk is also updated. Then let the customer know that the name change has been completed.

Example of [Legal Case](https://gitlab.lightning.force.com/lightning/r/Case/500PL00000S46I7YAJ/view) and the corresponding [Sales Support case](https://gitlab.lightning.force.com/lightning/r/Case/500PL00000Ru1WdYAJ/view).
