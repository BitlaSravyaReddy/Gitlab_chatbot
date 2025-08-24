---
title: "Impartner"
description: "PRM and Partner Portal"
---

GitLab uses Impartner as our primary Partner Relationship Management (PRM) platform, partner portal, MDF requests and marketing center for both Alliance and Channel Partners.

## PRM MDF Approval/ Process

The Channel Marketing team offers Market Development Funds to support the Partner's marketing campaigns and events. Channel Partners submit the MDF request and claim to the Partner Portal, and they must be approved before being reimbursed. 

This process is reflected in Iteration 2, [see flowchart](https://www.figma.com/board/5JXv8yRHDyXttWt669A67E/MDF-Process-Iterations?node-id=0-1&p=f&t=PhdMoT9RvpJz9VKz-0).

<iframe style="border: 1px solid rgba(0, 0, 0, 0.1);" width="800" height="450" src="https://embed.figma.com/board/5JXv8yRHDyXttWt669A67E/MDF-Process-Iterations?node-id=0-1&embed-host=share" allowfullscreen></iframe>

The emails to Partner and GitLab team members in the PRM Approval Process can be viewed in [this document](https://docs.google.com/document/d/1LfI-J77ag1CBRYUtjG5sQF-YuQFPnfT9ol0J26bmNjk/edit?usp=sharing).

### Change Management

1. The MDF request and claim will sync to Salesforce, however the attachments will not sync to Salesforce. That said, when we complete the POP task on the epic/issue, we will have to use Impartner as the SSOT. Please link the Impartner URL to the epic/issue.
2. There will be a new MDF dashboard, and Partner will be able to add a claim directly from the dashboard when the request is Approved.
3. There is a new required field on the Claim form asking for a Claim Title. We will need to provide guidance to Partner so they know how to name the Claim. Claim Titles need to be unique for each submission otherwise the workflows will fail.
4. Partners are asked to submit the lead list and proof of performance on the Claim, and Invoice when we receive a notification when the PO is created.

### Step 1 - MDF Request Submission

On the MDF Request Form, Partners are required to provide the following:

1. Activity Name
2. Type of Marketing Activity
3. In Person or Virtual Event
4. Description
5. Expected Start Date of Activity
6. Expected End Date of Activity
7. Total Cost of Activity (USD)
8. Target Number of Contacts
9. Estimated Pipeline Created (USD)
10. Partner Investment (Your Investment in USD)
11. Total Amount Required (From GitLab MDF Program in USD)
12. Vertical Industry Target Type
13. Segment Target Type

Once submitted, the Partner will receive a confirmation email indicating that their MDF request has been received.

### Step 2 - MDF Request Approval

The MDF Request Approval process will kick off as soon as the Partner submits the MDF Request.

The GitLab team member of the Activity Location will receive a notification requesting to accept or reject the MDF Request. This means if global Partner runs an event in AMER, the approval will be routed to the AMER CMM, and if they run an event in EMEA, the approval will be routed to EMEA CMM.

The GitLab team member must use the links below to review the MDF request submission, however, you can only approve or deny directly from the email notification.

Should you want to review all your requests, [see section](/handbook/marketing/marketing-operations/impartner/#prm-mdf-view).

Note that, when you have a planned PTO, Marketing Ops will need to add your manager as a secondary approver. Previously, you can do this in Salesforce, however, you'll need to create an issue request for support from MktgOps.

#### MDF Request Status

The MDF Request Status can be found in the MDF Request Details section.

- Open - when partner submits Request
- Approved - when Request is approved
- Closed - when Request and Claim are completed
- Denied - when Request is denied
- Canceled - when Request is canceled

### Step 3 - MDF Claim Submission

Once the MDF Event End Date has been reached, the Partner will receive reminder notification on the 2nd, 14th and 28th day since the End Date to submit their MDF Claim.

On the MDF Claim Form, Partners are required to provide the following:

1. Claim Title
1. Claim Amount
1. Paid Date
1. Proof of Performance attachment
1. Lead List attachment

Once submitted, the Partner will receive a confirmation email indicating that their MDF request has been received. If the Partner doesn't upload more than 2 attachments, the Partner will be notified to ensure they have provided all the necessary attachments.

### Step 4 - Check Attachments and Claim Approval

When the Partner has uploaded the Proof of Performance and Lead List attachments, the GitLab team member will be asked to check to ensure they are in-fact the right attachment.

- If they are missing an attachment, the GitLab team member is required to update the field, `Missing POP` (under the MDF Claim Details section) with the missing item. This will trigger an automated message to Partner will add the selected item to the Claim.
- If all attachments are received and looks good, the GitLab team member will update the `Approval Status` to `Denied` or `Approved` (under the Claim section).

#### MDF Claim Status

The MDF Claim Status you are to used is under the Claims section, called `Approval Status`.

- Open - when partner submits Claim
- Approved - when POP is approved
- Denied - when POP is denied

## Canceled MDF Request

When an MDF request has been cancelled, CMM will need to change the status on the MDF Request Details: `Status` => `Cancelled`. Partners will receive a notification informing them the Fund Request has been canceled. If Partners try to submit a Claim, it will automatically be rejected.

## PRM MDF View

To access your MDF request, go to PRM, and retrieve the `MDF` tab. If you do not see it, go to the `More` tab, there you'll be able to see the hidden tabs.

The preset filter will display all MDF requests that are Pending, Approved and Denied.

Should you wish to have a customized view, following the instructions below.

1. Go to the `Pending` tab
1. Select the three dots in a circle, and `Create From Current View`
1. Update the Name to "My Pending Requests"
1. Set Visibility: "Private - can only be seen by me"
1. In Manage Filters, Click on `+Add`
     
      1. Field: `Channel Marketing Manager - Name`
      1. Operator: `equals`
      1. Type: `Value`
      1. Value: Select your name

1. In Column Configuration, add any additional fields.
1. Save and repeat for the other statuses - Approved and Denied.

## MDF Dashboard Access

Partner needs to be granted access to the MDF dashboard. To do so, they must be an Authorized partner and MDF administrator.

To update the user to an MDF administrator:

1. Go to the user profile and select edit
1. In the Delegated Administrative Privileges section, check `MDF Administrator` under Administrative Privileges

## PRM - Salesforce Integration

The integration from PRM to Salesforce is customizable per object.

- Impartner `Lead` is mapped to SFDC `Lead`
- Impartner `MDF Request` is mapped to SFDC `Funds Request`
- Impartner `MDF Claim` is mapped to SFDC `Funds Claim`

### MDF Request and Claim Salesforce Sync

There is a two way sync between MDF Request and MDF Claim objects. The ID indicator between both sync is the Funds Request Number, also known as the MDF Number.
