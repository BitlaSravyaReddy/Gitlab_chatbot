---
title: "Qualified"
description: "Qualified facilitates instant sales conversations with visitors on the GitLab marketing website"
---

## Overview

Qualified allows Sales Development Reps to have live conversations with visitors on the about.gitlab.com site. Reps can see which accounts are viewing the site, their propensity to buy and choose to engage in a conversation or wait for the visitor to reach out through the automated chat bot.

### SDR Use Case

SDRs (inbound reps) will be routed chats of visitors who have requested to chat with a human while having a conversation with our AI Rep. These leads are first order available and not associated with an "Actively Working" account. They will route via round robin pools based on the account or visitor's geography. Once a chat is routed the rep will qualify the lead and determine if a meeting needs to be booked for a discovery call. SDRs can create and update the Salesfoce lead record with information gathered during the chat. Reps can also send their calendar to the visitor to book a meeting directly from the Qualified platform.

### BDR Use Case

BDRs (outbound reps) will be routed conversations from visitors who request to chat with a human while speaking with our AI Rep associated with "Actively Working" accounts they are assigned to. BDRs will also have the ability to initiate a conversation with a site visitor from an "Actively Working" account. Once a chat is routed the rep will qualify the lead and determine if a meeting needs to be booked for a discovery call. BDRs can create and update the Salesfoce lead record with information gathered during the chat. Reps can also send their calendar to the visitor to book a meeting directly from the Qualified platform.

### Experiences

Experiences are what the site visitor sees when they are browsing the site. It appears as a chat box in the bottom right corner of the web page. Visitors can choose to engage with the experience to help them navigate the site, book a meeting with a sales development rep or choose "Just Browsing" and close the experience.

We now offer experiences in English, French, German, and Japanese. Experiences in these languages match the language of the site being viewed. For example, the French epxeriences show on pages that contain /fr-fr.

Have questions about the experiences on the website? Please reach out to us in the #mktgops Slack channel.

To request a new experience please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

### Routing

Routing rules are set up in Qualified to send a visitor to the most appropiate rep to handle the conversation.

- A visitor that is existing in our CRM and being Actively Sequenced, they will be routed to the sequencing rep.
- A visitor that is identified as being associated to a US PubSec account will be routed to the BDR Assigned on that account. If no BDR Assigned is present on the account they will be round robined to the PubSec team.
- A visitor that is identified to be associated with an Actively Working account will be routed to the BDR Assigned on that account. If the rep is not available, the visitor will be routed to the inbound SDR team based on Geo to further qualify the lead. Once routed to an SDR, ownership of the lead will be determined by our standard [Rules of Engagement](/handbook/marketing/sales-development/#rules-of-engagement-quick-guide).
- A visitor who interacts with one of our non-English experiences will be routed to the team member or members who speak the appropriate language.
- A visitor that is not being sequenced, not PubSec, and not part of an Actively Working account will be routed to the appropriate Geo based SDR round robin pool.

If you feel you have been routed a conversation or visitor in error please post a link to the lead/conversation in the #mktgops Slack channel.

### Signals

Signals data is a collection of custom fields added to the Account object, reports, and dashboard components in Salesforce to showcase Signals data for your organization. The Signals Account 360 is a robust account profile that presents an account's engagement with your campaigns and their likely purchase intent over time. Sales reps and executives alike can view the Signals Account 360 to identify which accounts and opportunities are most likely to close.

### Integrations

Qualified is currently integrated with SalesForce, Outreach, and 6sense. Information on each integration is below.

#### Salesforce

The Qualified/Salesforce integration allows reps to create and update lead records from the Qualified platform and update contact records. Because Qualified is integrated with Salesforce reps can easily see information from the SFDC record directly in the Qualified platfrom while chatting. It also allows for the ability to map any field from the lead/contact record to Qualified to give reps pertinent information.

#### 6sense

Qualified offers an integration with 6sense to help you pull in firmographic information about the website visitors from the start. Using 6sense's reverse IP lookup, you can quickly see where the visitor is coming from, their company information, segments they belong to, and insights for their product lines.

#### Zoom

A seamless integration with Zoom is coming shortly. Until then, reps can either:

1. Input their personal meeting link in the section `Calendar -> Meeting details -> Enter your own meeting details` and their mmeting link will appear in the calendar invite.

    OR

2. Manually open the calendar invite in Google calendar and click `Add video conferencing details` to add a unique Zoom link.

#### Marketo

While Qualfied can create/edit person records, leads are typically created in SFDC first. Marketo utilizes triggers from SFDC activity or campaign membership for Interesting Moments and scoring for Qualified actions.

Qualified also has an integration to view a program in Marketo, within Qualified. We have hundreds of programs, so to reduce visibility, we created a program tag type `UsedWithQualified` = `True` to surface the program to Marketo. You can do this in Marketo's individual program settings under `setup`. This tag is not required, so despite having a `false` value, you can simply not use it if you do not want to surface the program to Qualified.

### Performance Measurement

The Rep Performance Dashboard helps you understand the metrics that mean the most to your success including:

- Visitor sessions routed to reps for pouncing (proactive engagement)
- Successful pounce conversations
- Visitor sessions where a visitor waited for a rep to join the chat
- When reps were available throughout the day
- Visitor sessions that waited for a chat and had a successful conversation with a rep
- Visitor sessions that waited for a chat and had no conversation
- Total rep availability

### Qualified AI SDR

Qualified has an AI offering that they call "Piper". We have chosen to name our AI SDR "GitLab AI Rep". The GitLab AI Rep has the ability to have conversations with website visitors when human reps are not available. This gives us the ability to provide a better visitor experience on the website by easily answering visitor questions, qualifiying visitors and booking meetings with human reps 24/7.

The GitLab AI Rep is enabled to respond to site visitor chat requests. There are two paths a visitor can take when they engage with the chat. "Connect with us" indicates a high intent visitor. They will be qualified by providing a business email and AI will begin the conversation with the visitor. The AI rep will continue the conversation and look for behavior that will trigger one if it's goals. Those goals are to Book a Meeting, Route to a Rep, or provide Support related information. "I have a question" indicates a lower intent visitor. The visitor will not need to provide an email immediately. AI will jump in to handle the conversation. As the conversation continues, AI will monitor for any indication that a goal is met and one of the actions above should be triggered. If a goal is triggered, an email will be collected and the appropriate action will be performed. 

All aspects of how the GitLab AI Rep behaves is controlled in the "AI Studio" on the admin side of Qualified. The "Content" section is where the GitLab AI Rep has indexed the GitLab marketing site, GitLab documentation, and other GitLab resources to be able to converse with and answer visitor questions live. The goals of the AI Rep are to either connect the visitor to a human rep (if one becomes available) or to book a meeting with a human rep.

We have set certain rules of engagement for the AI Rep to follow which include:

1. Never discussing special pricing or promotions
2. Always directing visitors looking for support to https://about.gitlab.com/support/
3. Never direct visitors to the demo or contact us page (we want these visitors to meet with a human)
4. Always make GitLab the better choice when making comparisons

The "Scorecard" and "Inbox" sections of the AI Studio is where we have control over how the GitLab AI Rep will answer specific questions. Here is where we can insert our own commonly asked questions and see how AI will respond. We can accept AI's response, tweak it, or tell it exactly what we want to certain questions. As visitors ask question they will appear in the "Inbox" we can move the most common ones to the "Scorecard" to rate.

#### AI Rep Rollback Plan

If there is a need to turn off the GitLab AI Rep, we have build the experiences in a way to easily switch off AI and switch on a traditional experience.

In the Qualified admin settings, navigate to `Experiences` and select `Automatic`. Beginning at experiences 48 and 49 you will start to see duplicate experience titles with one having `AI` added to the end. For example `[EN] Page - Solutions - Moble` and `[EN] Page - Solutions - Mobile - AI`. If the  GitLab AI Rep needs to be turned off you will need to go down the experience list, switch off each experience that ends in `AI` and switch on the corresponding expereince without `AI`.

### Qualified AI Email

Beginning in FY26 Q1 we will be testing Qualified's AI email functionality. Our test includes two use cases.

1. Visitors to the GitLab marketing site who are offered to book a meeting through the Qualified chat and who fail to book that meeting. AI will follow up via email to attempt to re-capture that meeting booking on behalf of the Sales Development rep whose calendar was shown. These leads and contacts will MQL as usual since they have shown enough intent to either explicitly request a meeting or trigger an AI goal to offer a meeting. Once AI reaches out via email the record will move to Accepeted status and on to either Recycle or Qualifiying depending on the outcome of the email campaign. 
2. Leads and contacts added to specific content syndication campaigns. These will be earlier in the funnel prospects in an attempt to raise interest earlier and more quickly. The status of these recods in Salesforce will not be updated. Rather we will indicate that these leads are being reached out to by AI with a checkbox on the record. Once the AI email campaign is over, the box will uncheck and the record will continue it's normal lifecycle. The record will need to be routed to a Sales Development rep and if there is a response they will be able to respond back via email and dispostion the lead appropriately.

### Qualified AI Email Rollback Plan

Just like the AI chat rollback plan, in the Settings section of Qualified an Admin will be able select Email Campaigns in the AI section of the left navigation bar. You will see the various campaigns that are running and the Admin can swith off the campaign by clicking into the campaign and in the top right corner selecting Off. 

#### AI Rep Support

Have questions about the GitLab AI Rep on the website? Please reach out to us in the #mktgops Slack channel. We also have an external Slack channel with our Qualified support team. If you are not already in that channel, please ask a Marketing Ops team member to be added if you need access to our Qualified team.

To request a new feature or change please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

### Other Qualified Features

#### Smart Forms

Using smart forms with Qualified allows your existing lead capture form to qualify leads on-the-fly and route your most qualified visitors to your sales reps in real-time.

Traditional lead forms often come with the expectation that visitors coming to your website will have to wait hours or days to talk to your sales team. Smart forms allow you to alert your reps in real-time to those hot prospects on your site ready to talk with sales, or book a meeting with your sales team for a later time.

To request a new smart form please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

#### Smart Buttons

The Smart Button changes CTAs from a static one-size-fits-all form to a bespoke buying experience. When visitors meet your ideal customer profile, trigger a real-time sales conversation with your sales team to open the door to a dynamic two-way conversation. This gets buyer questions answered in real-time and helps your sales teams instantly capture more pipeline.

To request a new smart button please use [this issue template](https://gitlab.com/gitlab-com/marketing/marketing-operations/-/issues/new#) in the Marketing Operations project.

### Resources

- [Qualified University](https://www.qualified.com/university)
- [Sales Rep Setup Guide](https://www.qualified.com/university-guides/sales-rep-setup-guide)
- [Best Practices for Sales Reps](https://www.qualified.com/university-categories/sales-reps)
- [Best Practices for Sales Managers](https://www.qualified.com/university-categories/sales-managers)
