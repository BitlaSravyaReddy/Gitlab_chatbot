---
title: Hyperscaler Campaign
---

## Hypercaler Campaign

## Naming Convention Requirements

When working with hyperscaler partners like AWS and Google Cloud, it's important to follow specific naming conventions and configuration procedures. This guide explains each component of this process in detail.

Every campaign involving a hyperscaler partner must specify the Hyperscaler Partner Name after the date:
> YYYYMMDD_HyperscalerName_Campaign_CampaignType_Region

Examples:

- 20251202_AWS_AWSreinvent_Booth
- 20250409_GCP_GoogleCloudNext_Booth
- 20241114_AWS_devops.com_ModernizingFinServe_emea_amer

If there are Hyperscaler Funds involved, ensure you include the type of Funds are applied to the Campaign after the Hyperscaler Name. 

- MDF: Market Development Funds for 50% coverage
- CR: Credits for 100% coverage

Examples:

- 20250307_AWS_MDF_Campaign_CampaignType_Region
- 20250307_GCP_CR_Campaign_CampaignType_Region

Reference the [Campaigns and Programs](/handbook/marketing/marketing-operations/campaigns-and-programs/#hybrid-marketo-templates) page for naming conventions for specific campaign types.

## Salesforce Configuration Requirements

When setting up these campaigns in Salesforce, you need to take two critical actions:

1. Set the field `Is Hyperscaler Involved?` to `True` - This flags the campaign as a partnership activity.
2. Select the appropriate partner under the `Hyperscaler` field - Choose either:

   1. Amazon Web Services
   2. Google Cloud (Partner)

3. Select the Fund Type under `Will there be Hyperscaler Funding?` 

   1. MDF
   2. Credits

This configuration ensures proper attribution and tracking of partnership activities. Note that, Hyperscaler MDF is only in referrance to AWS MDF, as that is currently the MDF that's available for GitLab.

### Campaign Types Covered by These Guidelines

These naming conventions and configuration requirements apply to all activities where hyperscalers are involved, including:

- Exhibition booths at hyperscaler-hosted events (such as Google Cloud Next or AWS Summit)
- Presence at major corporate events (like AWS reInvent)
- Joint webinars with hyperscaler partners
- Digital marketing campaigns including content syndication and advertising
- Any events or activities that utilize AWS MDF (Market Development Funds) or Google credits

### Special Instructions for Content Syndication Teams

If you work with content syndication, you have an additional step: You must update the Asset Name in the Marketo token of the Content Syndication Folder to include the Hyperscaler Name.

This ensures consistency across all platforms and makes reporting and attribution more accurate. The Marketo Program Description field has been recently updated to include a reminder about adding hyperscaler partner names to campaign names whenever these partners are involved.

Following these guidelines carefully ensures proper tracking, reporting, and compliance with partnership agreements, while also making campaigns easier to find and manage across systems.

## Hyperscaler Funded Campaign

Hyperscaler funded campaign represent a strategic partnership mechanism through which cloud hyperscalers like Amazon Web Services (AWS) and Google Cloud Platform (GCP) provide financial support to partners like GitLab for joint marketing initiatives.

Presently, the Hyperscaler funds are **only available to the Field Marketing team**. We will be working in iteration to support additional marketing teams.

These funding programs operate under different models that reflect each hyperscaler's partnership approach:

- **AWS MDF Program**: Follows a matching investment model. This means for every dollar AWS contributes, GitLab must match with its own dollar.
- **Google Credits Program**: Unlike AWS, Google offers 100% reimbursement for approved marketing activities. This model allows GitLab to execute campaigns and receive full reimbursement upon providing proof that the activities were completed successfully.

From GitLab's perspective, these funds enable more expansive marketing campaigns than possible while strengthening strategic partnerships with major cloud providers. The partnership creates a "better together" narrative that helps customers understand the enhanced value proposition of GitLab running on these cloud platforms.

### Key Roles in the Hyperscaler MDF Ecosystem

1. Program Owner (Francine): Primary contact with Hyperscaler Partners

   1. Oversees the entire MDF program
   2. Reviews internal MDF request entries with Hyperscalers
   3. Submit MDF request, when approved, we'll receive a PO
   4. Request an invoice from AR team provide the PO and MDF Approval Email via issue
   5. Submit claim with proof of performance (receipt) to the Hyperscaler portal

2. Fund Requesters: Initiates funding requests

   1. Fill out the [appropriate spreadsheet](/handbook/marketing/channel-marketing/hyperscalers/#application-process) with campaign details
   2. Provides Target MQL and Target Pipeline Goals

3. Partner Marketing Manager (Gabby): Administers fund allocation

   1. Set up the Allocadia activity
   2. Create the GitLab Hyperscaler Funds issue assigned to the requester

4. Campaign Owners/Operations (Fund Requester can also be a Campaign Owner)

   1. Create their own Asana project to manage their campaign
   2. Manages execution and setup for Marketo and Salesforce
   3. Open Zip request
   4. Send Program Owner receipts for Proof of Performance

### Application Process

1. Complete the Google Sheet:

    1. AWS: [Marketing calendar - spreadsheet](https://docs.google.com/spreadsheets/d/1Ej_QJpTI0u_hPwB-jJKcqTviIAnmS1wgctfabgfUlPM/edit?gid=2978057#gid=2978057)
    2. GCP: [Marketing calendar - spreadsheet](https://docs.google.com/spreadsheets/d/1B2mSraHHhCMbK96Sx0ZQlXTI6J7tIp5LNeWdsnKetrE/edit?usp=sharing)
    3. Complete all required fields, including:

       1. Strategic Alignment
       2. Region
       3. Activity Type and Description
       4. Proposed Start and End Date
       5. Total Cost
       6. Amount Requested
       7. Target MQL
       8. Target Pipeline

2. Submit for Review:

    1. Tag Francine for approval in the Google spreadsheet
    1. Include any supporting materials that strengthen your case (past performance of similar activities, customer interest data, etc.)

### Approval Process

1. Initial Screening: Francine will review your application to ensure it meets basic requirements and aligns with strategic priorities.
2. Hyperscaler Partner Approval: Upon preliminary approval, Francine will review and seek approval for the activity and confirm funding amount from the Hyperscaler Partner.
3. System Configuration: Once approved by the Hyperscaler Partner,

    1. Channel Marketing Manager will open the Allocadia activity and Hyperscaler Funded GitLab issue
    2. Campaign Owner will be responsible for creating the Marketo campaign and sync to Salesforce using the Allocadia Subcategory ID (found in the Hyperscaler Funded GitLab issue)

### Set up

#### Allocadia

The Channel Marketing Manager will be responsible for opening the Allocadia activity under the [Regional Marketing > AMER > Hyperscaler](https://eu1.allocadia.com/budgets/122286/items?view=default) plan.

1. Create subcategory and line item

    1. Different accounting approaches apply based on the hyperscaler. AWS campaigns show both the positive contribution and the matching negative amount, while GCP campaigns show the full reimbursable amount. 

2. Details panel

    1. Planning:

       1. New FO or Growth
       2. Target MQL (syncs to SFDC Planned MQL)
       3. Target Pipeline (syncs to SFDC Planned Pipeline)
       4. Sales Dev Onsite Support
       5. Sales Dev Invite Support
       6. Subcategory (FM)
       7. GTM Motion
       8. Start Date
       9. End Date
       10. Triple Play
       11. Embedded Systems
       12. Is Hyperscaler Involved? = True
       13. Hyperscaler
       14. Will there be Hyperscaler funding?
       15. Hyperscaler Funding Amount
       16. SA Support
       17. Segment
       18. Geo
       19. Country

    2. Wishlist/Cancelled

       1. Cancelled

    3. Campaign Details

       1. Existing Salesforce Campaign
       2. Campaign Link
       3. Campaign Owner
       4. Campaign Type
       5. Budget Holder = Hyperscaler 

    4. GitLab Issue Details

       1. Operational Program Owner = Francine
       2. Partner User Handle = @fanthony2
       3. Requester User Handle 
       4. GitLab Issue Template = Hyperscaler
       5. Official Event/Campaign Name 
       6. GitLab Marketing Issue Link (Auto-populated)
       7. GitLab Issue URL Reference (Manual entry)

3. Action: Create GitLab Hyperscaler Funded Issue in the Field Marketing GitLab Project

#### GitLab Issue 

The GitLab Hyperscaler Funded Campaign issue will be used as an intermediate step prior to syncing to Asana. 

1. Channel Marketing Manager will be responsible for entering the details include region and activity quarter labels to GitLab Hyperscaler Funds issue.
2. Program Manager will request for invoice from AR using the finance issue, including PO and payment terms. MDF - [Example](https://gitlab.com/gitlab-com/Finance-Division/finance/-/issues/6464)  
3. Once the GitLab Hyperscaler Funds issue details are complete, Channel Marketing Manager adds the `Asana-Sync-Project` to the GitLab Hyperscaler Funds issue and ping the FMM and FMC to start the [Plan to WIP process](/handbook/marketing/field-marketing/#process-for-moving-events-from-plan-to-wip)
4. Channel Markting Manager will add the Asana project link to the Resources section above

#### Asana Project
 
To accommodate the Field Marketing process in Asana, we have integrated the steps for Hyperscaler Funded Campaigns into the [Plan to WIP](/handbook/marketing/field-marketing/#process-for-moving-events-from-plan-to-wip).

##### Pre-Event

1. Create Marketo/ SFDC campaign with add the Hyperscaler Name and Hyperscaler Fund Type after the date in the Campaign Name - reference a handbook for [naming convention](/handbook/marketing/marketing-operations/campaigns-and-programs/#partner-campaign-setup). _Examples: 20250307_AWS_MDF_ActivityType_ActivityName_Region;
20250307_GCP_CR_ActivityType_ActivityName_Region

   1. Create Marketo program under the [Hyperscaler Funded Campaign folder](https://experience.adobe.com/#/@gitlab/so:194-VVC-221/marketo-engage/classic/MF27058A1)
   2. Sync the Marketo program to Salesforce using the Hyperscaler Funded Campaign Allocadia Subcategory ID
   3. Update the links to Marketo and Salesforce in the Asana Project Overview

2. Opens the Zip request

   1. Acquire Contract/Invoice for the Marketing Activity 
   2. Select the appropriate purchase type: “What are you looking to purchase?” (Ensure not to select MDF)
   3. Enter the amount of the total contract cost
   4. In the Allocadia ID, specify the Line Item ID (positive value) of the Hyperscaler Fund Allocadia activity in the Zip request
   5. Add Francine as a follower to the Zip request
   6. Update the link to Zip request in the Asana Project Overview 

##### Post-Event

1. Attach Proof of Payment (POP) to the Asana Project and tag Francine

   1. Third-party receipts showing actual costs are required for cash reimbursement. It should clearly show a date, after the fund requests approval and the paid amount.

### Understanding Data Flow: From Lead to Opportunity

One of the most complex aspects of hyperscaler campaigns is tracking the customer journey from initial interest to closed business. This journey involves multiple handoffs:

- Lead Identification: When a lead comes from a hyperscaler campaign, it's tagged with the appropriate CRM Partner ID and campaign information.
- Lead-to-Opportunity Conversion: As leads convert to opportunities, the system maps partner and campaign information to maintain attribution.
- Notification Systems: Automated notifications alert Cloud ESMs (Ecosystem Sales Managers) and regular ESMS are involved when new opportunities arise from hyperscaler campaigns.
- Co-Sell Integration: Labra facilitates referrals between GitLab and Hyperscalers for co-sell opportunities, creating a structured engagement process.

Understanding this flow helps teams recognize that not all Hyperscaler campaign leads will become co-sell opportunities, but tracking remains important to demonstrate overall program impact.
