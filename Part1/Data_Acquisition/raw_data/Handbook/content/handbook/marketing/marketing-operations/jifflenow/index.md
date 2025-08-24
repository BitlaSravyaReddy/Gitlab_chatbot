---
title: JiffleNow
description: Automated appointment scheduling of in-person, and virtual B2B meetings at events or campaigns.
---

<link rel="stylesheet" type="text/css" href="/stylesheets/biztech.css" />

## Overview

JiffleNow is an automated appointment scheduling of in-person, and virtual B2B meetings at events or campaigns. To following along on the implementation project, follow this link: https://app.asana.com/0/1208791785314172/1208791670565152

## Access

- Sales users (for requesting meetings): Access for Meeting Requestors via SFDC is granted via the JiffleNow Permission set and most sales profiles are already included. If you are unable to access Jifflenow through SFDC, please create an [AR](https://gitlab.com/gitlab-com/team-member-epics/access-requests/-/issues/new?issuable_template=Individual_Bulk_Access_Request) and make sure the Sales Systems team is tagged (Similar to SFDC access requests).
- All non-Sales users (requesting and managing meetings) and sales users that need to manage their availability for an event: Access to Jifflenow is managed through Lumos. If you do not have the Jifflenow tile in Okta, please request access to JiffleNow via Lumos in OKTA. You will need access through Okta to request meetings if you are not a sales user.
  - If you are designated as a meeting manager for a particular event, a request to provision Okta for your access will be created as part of the set-up process in Jifflenow.

MOps provisioner: For `Requestor` role, you do not need to do anything in JiffleNow. Once Okta is provisioned, the user will have access to request meetings. If a person just needs access to reports and dashboards, you can add them as a `Requestor`, then toggle the Reports & Dashboard toggle on in their profile. For all other roles, you will add the person to the specific event they need access to with the correct role and engagement type. This will be outlined in the event request task in Asana.

### When to use Jifflenow

Jifflenow is not required for all events where there is meeting space. At this time, use of Jifflenow is recommended for the following scenarios (unless noted, all criteria must be met):

1. There is at least one dedicated meeting space. Meeting at the booth does not meet this requirement, unless there is a separate enclosed meeting space in the booth.
2. There will be one or more C-level executive taking meetings at the event.
3. If there are no C-level exectives attending, there must be at least two other VP-level executives. However, if requirement 4 can be met, two Director+ executives can be set-up to take meetings. 
4. A member of the EBA team must manage the executive schedules for this event and approve meetings in Jifflenow. Alternatively, another designated meeting manager can approve meetings in Jifflenow, but this will also require the meeting manager to manage the executive's schedule in the system and coordinate meeting times with them.

### Requesting an event in Jifflenow

We use Jifflenow for events where we will have executive meetings. Please follow the instructions below to request creation of an event in Jifflenow.

- SLA: 15 days - Please request your event to be created in Jifflenow at least 15 days before you would like the event to go live. Meeting scheduling should be live at least 30 days prior to the event date, so the Jifflenow request should be submitted no less than 45 days prior to the event date. You can submit the request as soon as you have the necessary details.
- Request: Please [complete this form](https://form.asana.com/?k=ZW0w5_ppBQLh2gCyZEOFcg&d=306855239930259) to request your Jifflenow instance. This will create a task in Asana.
  - In order to build the event in Jifflenow, we will require all requested information on the form, especially the meeting location, available hours, available executives, and SFDC campaign IDs.
- Create a Slack channel for Executive Meetings for this event. Examples: `#googlenext-execmtgs-2025` or `#aws-reinforce-execmtgs-2025`
- Events are built in a sandbox and we test the meeting requests and notifications in sandbox. All tests must be completed in the sandbox. Once the event is pushed to production, tests cannot be deleted without intervention from support and will be included in metrics.

### User Roles

- **Requestor** - Anyone that has access to schedule meetings within the tool.
- **Meeting Manager** - Users assigned to this role manage the meeting approval process, user accounts, rooms, and calendars and help govern access to the Jifflenow portal. They have full access to all meetings and can view, edit, or cancel any request placed by anyone within an event. Meeting Managers have the highest level of access in Jifflenow.
- **Junior Meeting Manager** - While a Meeting Manager has full access to all requested meetings, a Junior Meeting Manager may be given limited access to all meetings within a particular meeting type. Someone may need this if tasked with managing a set of rooms or approving a subset of requests based on specified criteria. They can approve meetings for the types they are assigned to.
- **Executive Admin** - Executive Admins manage meeting activity on behalf of the specific internal attendees they are assigned to. The EA role cannot approve meetings, but they can endorse their executive's participation in meetings.

## Training

We have put together a comprehensive [training slide deck](https://docs.google.com/presentation/d/1yzGICzWa1687_da4tte7rV3qnMbwtZjEVpgTDb3XjAA/edit#slide=id.g1d24c3e4ddd_5_252), and we also have linked training videos below:

- [EBA and Meeting Manager Training](https://drive.google.com/file/d/1MlgZaD-Z41DSaVfAAql4uR5gIIz4velv/view?usp=drive_link)
- [Meeting Requestor Training - for Sales and Field](https://drive.google.com/file/d/1JXDmdWs2391CW4h7C3Q2rX8I4NNJPYZv/view?usp=sharing)
- [Dashboards and Reporting](https://drive.google.com/file/d/1SWb7RiWQ7dZeWXkPu4wBf-mVfB0fm3z7/view?usp=sharing) 
- [Processing Inbound Requests](https://drive.google.com/file/d/1yGMK4qmw25-9oPeaHByXOnGYkiXbxRsz/view?usp=sharing)
- [Updating availability (for executive attendees)](https://drive.google.com/file/d/19YqsLddRDBYwhrVn2wNH-xHFOiyvAebL/view?usp=sharing)
- [Managing On-Site Meetings](https://drive.google.com/file/d/1dLb_xCytBSYj4pj41TREDl_M-knT2VqE/view?usp=sharing) 
- [Mobile App for meeting managers](https://support.cvent.com/s/communityarticle/Using-the-Jifflenow-Mobile-App-for-Meeting-Managers)
- [Mobile App for attendees](https://support.cvent.com/s/communityarticle/Using-the-Jifflenow-Mobile-App-for-Attendees)

## Salesforce.com Integration

This connection will allow for Sales to book meetings directly within Salesforce.com and allow JiffleNow to access and link contact records. Meeting requestors can access JiffleNow to schedule meetings through a button on the Contact, Account and Opportunity record.

New records created through Jifflenow (for example, people added onsite) will be created as Leads in salesforce, or meeting details will be added to their existing record. This applies even if the meeting isn't booked through Salesforce.

### Support

Reach out in #mktgops for assistance with Jifflenow.

For event specific help, search Slack for the event and ask your question in the relevant `execmtgs` channel:

### External JiffleNow Invites

For major events, it is common for other companies to utilize JiffleNow as well, which can cause confusion for EBAs managing executive calendars. Here is how to tell if an invite is for a GitLab initiated meeting, or an external initiated meeting:

1. GitLab meeting invites will be from `GitLab` or `GitLab Events Team` with a domain including `meetings.gitlab.com`. Calendar invites will be slightly different, but will still include `meetings.gitlab.com` in the domain.  
2. Take a look a the meeting invites. If anyone from GitLab with a GitLab email address is listed in "External Attendees", it was not scheduled through our instance.
3. At the bottom of the email, there will be a help contact. Our help contact will always be someone at GitLab (or in the case of internal requests, a Slack channel).
4. If an INTERNAL calendar invite doesn't have the Confidential note at the top, it isn't from us.

## Onsite Event Management

How onsite meeting bookings are handled will be determined event-by-event. It is recommended that the DRI have a meeting with all meeting managers (regardless of if they will be onsite or not) to determine how they would like to manage onsite meetings. For example, for some events, the EBA team would prefer to continue to manage the meeting requests that occur onsite and the onsite team should contact the appropriate EBA for booking.

Regardless of how the team decides to book new meetings onsite, external attendees must be checked in to meetings they attend. 

To check-in an attendee:

- Click on the meeting from the Jifflenow "Meetings" tab.
- On the right side panel that appears, click "check-in" on the attendee.

This will automatically check in the meeting as well. It is important to check-in the individual attendees so their record in Salesforce is updated properly. The process described above is the same for booth demo check-ins.

When booking a new meeting onsite, you will select the attendees and time following the regular booking process. Meeting managers can use "Quick Submit" to bypass the standard booking form. As a meeting manager, you have the ability to add/remove attendees, or change the duration of the meeting. Detailed instructions will be available in the training videos above or the internal handbook. 

## Mobile App

To use the mobile app for onsite meeting management, you must be set-up in Okta to access Jifflenow. We recommend the mobile app for onsite meeting managers.

Download the [Jifflenow app](https://www.jifflenow.com/mobile-app-product/) from the appropriate app store for your device.

## Meeting types

- Executive Meeting: This is a meeting with a GitLab executive (VP or C-Level). These meetings are requested through sales / internal GitLab team members, or partners. We do not have a public form to sign-up for these meetings. Anyone interested in one of these meetings should talk with thier GitLab representative.
- Booth demos/meetings: This is a meeting or demo at a booth demo station. We do not schedule a specific GitLab team member to attend this meeting, we only schedule time slots. This type of request can be promoted publicly and can be requested through our website.
- Meet with an expert: Similar to a booth demo, but typically occurs when we have designated meeting space at an event (that is not being used for Executive Meetings). We may or may not assign a specific GitLab team member to attend these meetings. This type of request can be promoted publicly and can be requested through our website.
- Off-site meeting: These meetings take place outside of our designated meeting space. This allows us to schedule executives so they show as unavailable, but we do not use our meeting space. The most common example is at large events, a partner would like to meet with an executive in their meeting space. This meeting type allows for requesting that executive (to block their time), but in their location.

## How To Request Meetings

### Requesting Meetings outside of standard meeting space

If you have already set a meeting location outside of our space, for example in a partner’s meeting space:

1. Select Executive Meeting with Other Executives
2. De-select meeting space
3. Click `Other Location` and add the details of the location
4. Please do not request this meeting until you have a location
5. Select your attendees and meeting time as normal

### Requesting Standard Meetings

1. Navigate to the Account, Contact or Opp in SFDC.
2. In the top right drop down, you'll find JiffleNow Meetings.
3. Select the appropriate event, and click Request Meeting.
4. From there, you can request different meeting types that are available. Make sure to link the correct Account and Opportunity (if applicable - you must type it in).
5. In the next screen: Select attendees, Internal and External. Pick the room and the available time.
6. To add attendees not listed in the internal or external list, click the + next to ATTENDEES. Enter their contact details and select them for the meeting. If you would like to add a new external attendee to SFDC, you can toggle the “Sync contact to SFDC” and it will be added to the account.
7. Then, add details about the meeting and attendees in the right panel. (SFDC should update most of it)
8. You must include an Executive Request Briefing Doc. For C-Level meetings, you are required to have Regional VP approval before requesting the meeting.
9. Once complete, select submit. This will then route for approvals through the EBA team, depending on the participants.
10. Once fully approved, this will trigger email invitations to all participants.

### View Requested Meetings (For Attendees)

1. In salesforce - On the left side, click on the 9 dots (app launcher) and type in JiffleNow
2. Click "JiffleNow Home Page" along the top row
3. Select the 3 dots and click Meetings
4. Along the left side, under `Internal Attendees` type your name
