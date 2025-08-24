---
title: "Channel  Marketing Epics"
description: "A comprehensive list of all of Channel Marketing epic codes."
---

## Channel Marketing Epics

Create epic here: https://gitlab.com/groups/gitlab-com/marketing/-/epics/new

## MDF Requests

**Note:** Do not pay out invoice/P.O. until MDF proof of performance (POP), lead list and Invoice have been processed and noted as approved by the Partner Marketing team.

```markdown
<!-- Name this Epic:  MDF - PartnerName - Activity -->

{{#fields}}

## MDF Request - {{fundRequest}}

## :key: Key Details

### :round_pushpin: DRI

* **Campaign Owner (CMM)**: {{userHandle}}
* **Ecosystem Sales Manager**: `Insert ESM`
* [ ] **Manager Approval**: `Insert Ecosystem Director` - Approval required only for EMEA.

### :handshake: Partner Details

* **Channel Partner**: {{channelPartnerName}}
* **Channel CRM ID**: {{channelPartnerCrmId}}
* **Is an Alliance Partner Involved?**: {{isAlliancePartnerInvolved}}
* **Alliance Partner**: {{alliancePartnerName}}
* **Alliance CRM ID**: {{alliancePartnerCrmId}}

### :paperclips: Quick Links

* [ ] **MDF Tracking Sheet** (add link)
* [x] **Allocadia Sub-Category ID** [{{subCategoryId}}](https://eu1.allocadia.com/budgets/{{budgetId}}/items/{{subCategoryId}}/details)
* [x]  **Allocadia Line Item ID** [{{itemID}}](https://eu1.allocadia.com/budgets/{{budgetId}}/items/{{itemId}}/details)
* [x] [**Salesforce Campaign**]({{campaignLink}})(automated)
  * [ ] **Funds Request** (add link)
  * [ ] **Fund Claim** (add link)
* [ ] [**Marketo Program**]() - [process to follow](/handbook/marketing/channel-marketing/#mdf-campaigns) Remember to paste **Allocadia Line Item ID** into Marketo Description field when syncing to SFDC. The line item in Allocadia will auto-tag/update once the SFDC Campaign is created and an ID match found.
* [ ] [**Zip**]()

## :notepad_spiral: Campaign Details

*Please do not delete anything in this section. Fill out information in full and complete your budget line item before moving to WIP.*

* **Date(s):** {{startDate}} - {{endDate}}
* **Campaign Type:** Partner - MDF
* **Worked by Sales Dev:** {{workedBySalesDev}}
* **Tactic/Event Type:** {{partnerCampaignType}}
* **Campaign Name:** {{campaignName}}
* **Location:** `Insert the location of the activity`
* **Event website:** `Insert the event website`
* **Expected number of deal registrations:** {{expectedNumberDR}}
* **Target number of contacts:** {{targetNumberContact}}
* **Estimated pipeline created (USD):**  {{estimatedPipelineCreated}}
* **Budgeted costs:** `Insert the budgeted cost`
* **Total cost of campaign:** `Insert cost of campaign`
* **Budget holder:** Channel Marketing
* **Region:** {{partnerRegion}}
* **Sub-Region**: {{geo}}
* **Sales Territory (if specific):** `Insert the sales territory`
* **Sales Segment:** Assumes both Large & MM unless otherwise explicitly noted.


## :vertical_traffic_light: User Journey

(REQUIRED: Channel Marketing Manager to provide a description of the user journey. What is this campaign? How will the partner attract leads and drive ROI from this spend?)

## Joint Messaging

Please provide high level joint messaging concepts that you will be using with the campaign

## :level_slider: Sponsorship Level & Details

(Fill in if applicable, delete if not.)

## :mega: Does this event have a speaking engagement?

(Fill in if applicable, delete if not.)

## :busts_in_silhouette: Staffing

Please read through the [Event Handbook page](https://about.gitlab.com/handbook/marketing/events/#employee-booth-guidelines) for best practices at events. Once you commit to an event, please make sure to plan to attend.

* [ ] ESM
* [ ] SA Request: If you need an SA to attend, [please follow their triage process](https://about.gitlab.com/handbook/marketing/events/#requesting-technical-staffing).
* [ ] Speaker: If you need a customer speaker, [please follow the Customer Reference Process](https://about.gitlab.com/handbook/marketing/brand-and-product-marketing/product-and-solution-marketing/customer-advocacy/customer-events.html#requesting-a-reference-customer).
* [ ] GitLab AE
* [ ] Other:

### Lead Follow-up with Channel Partner

- [x] Will the partner do the initial lead follow-up? _(Auto-checked - if Sales Dev is involved make sure to uncheck)_

  - [x] YES, based on [process outlined here](/handbook/marketing/channel-marketing/#channel-partner-lead-sharing-via-vartopia).
    - [x] Partner will submit for Deal Registration via Partner Portal
      - [ ] Please describe how the partner plans to follow-up on leads received from this event/campaign:
  - [ ] No
- [ ] Please add any additional, relevant notes regarding the partnership on this event/campaign here:

## :package: Swag and Event Assets

<details>

<summary> Expand </summary>

For all details regarding swag, [please see here](https://about.gitlab.com/handbook/marketing/channel-marketing/#requesting-swag-for-channel-events-and-awards).

### Shipping Details

- [ ] Ship from Vendor:
- [ ] Please list what is being shipped (including quantities):
- [ ] Tracking:
</details>

## :checkered_flag: Post Event

<details>

<summary> Expand </summary>

* [ ] Import lead list to Google Drive
* [ ] Add proof of performance to the epic by posting the SFDC Fund Claim link

</details>

/label ~"mktg-status::wip" ~“Channel Marketing" ~"Channel" ~"MDF" ~"Pending MDF Approval"

/assign {{userHandle}}
/confidential

{{/fields}}

```

## Channel Events

**To Partner Marketing Webinars**

```markdown
<!-- Name this epic: Name of Event - Date of Event -->

## [Main Issue]() - template: https://gitlab.com/gitlab-com/marketing/channel-marketing/-/issues/new?issuable_template=ptnr_mktg_webinar_main_template

## Copy Document: https://docs.google.com/document/d/1w9yMw2DQJ5u1RxC3kYO0ZgQM5TJfKlRiGGjJqVFg1GE/edit?usp=sharing

## [Dry Run Agenda]() - template: https://docs.google.com/document/d/1vrdOEV4fbl5bzYpqQcCFnMN6QjuCIc0nRfilP3IvCfM/edit#heading=h.qv152nkfuvce

## [Landing Page]() - `to be added when live`

## Key Details
* **Channel Marketing Manager:**
* **Campaign Type:** Webinar
* **Official Name:**
* **Date(s):**
* **Campaign Name (SFDC/Marketo Name):**
Format: YYYYMMDD_FYYY_QX_Quarterly_Partner_Marketing_Webinar_Region (i.e. EMEA/AMER or APAC)
Note: Campaign format is critical to maintain reporting integrity
* [ ] [**Salesforce Campaign**]()
* [ ] [**Marketo Program**]()

## On24 Links
- [ ] [Link for AUDIENCE to join](ADD LINK TO THE AUDIENCE from ON24)
- [ ] [Link to registration reports, analytics, etc.](ADD LINK TO THE Reports from ON24)
- [ ] [Link used to review audience-view of event lobby](ADD LINK TO THE Preview from ON24)
- [ ] [Link supplied to event producer, presenters and Q&A managers to conduct dry run and join webinar day of](ADD LINK TO THE Present from ON24)

## Sub-Issue Creation
Utilize the [Workshop/Webcast SLA Workback Schedule](https://docs.google.com/spreadsheets/d/1YXriQ1clvYyBn-TDbbCVvNP6NEbrAF-0w6tIHKhDeZM/edit?usp=sharing) to calculate the due dates. `All Webcasts will be -45 day SLA webcasts since they require all new content.`

### PMM Creates and assigns all to self except Marketo LP&A

* [ ] [On24 Event Creation](/handbook/marketing/virtual-events/webcasts/#on24-webcast-setup)
* [ ] [Program Tracking](https://gitlab.com/gitlab-com/marketing/field-marketing/-/issues/new?issuable_template=program-tracking)
* [ ] [Webcast Prep Issue](https://gitlab.com/gitlab-com/marketing/field-marketing/-/issues/new?issuable_template=webcast-prep)
* [ ] [Dry Run Scheduling Issue](https://gitlab.com/gitlab-com/marketing/field-marketing/-/issues/new?issuable_template=webcast_dry_run_scheduling)
* [ ] [Write Copy Issue](https://gitlab.com/gitlab-com/marketing/field-marketing/-/issues/new?issuable_template=write-copy)
* [ ] [Marketo Landing Page & Automation Issue](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new?issuable_template=request-marketo_landing_page_request)
* [ ] [News on Demand Article/Email Creation](https://gitlab.com/gitlab-com/marketing/channel-marketing/-/issues/new?issuable_template=NoD_promotion)
* [ ] [Update Partner Portal - Partner Marketing Webinar Page](https://gitlab.com/gitlab-com/marketing/channel-marketing/-/issues/new?issuable_template=Update_Portal_PtnrMktgWebinar)
* [ ] [Create Post-event Survey](https://gitlab.com/gitlab-com/marketing/channel-marketing/-/issues/new?issuable_template=to_ptnr_postevent_survey)


/label ~"mktg-status::wip" ~"Webcast - GitLab Hosted" ~"Channel Marketing"
```
