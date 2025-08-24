---

title: Email Logging in Gong
description: >-
  Guide for Solutions Architects on how to set up automatic email logging with customers in Gong, ensuring better visibility,
  collaboration, and data-driven insights across the organization.
---

## Overview

Email communication with customers is an essential part of the Solutions Architect role. Gong automatically captures these communications to ensure better visibility, collaboration, and data-driven insights across the organization.

## Setting Up Gong Email Connection

1. Log into Gong using Okta SSO authentication
2. Click on your initials or profile picture in the top right corner of the screen
3. Select "My Settings" from the dropdown menu
4. Locate the "Emails" section
5. Check for green checkmarks next to these two permissions:
   - "All emails you send to or receive from your CRM contacts are imported"
   - "Email write-permission is turned on for composing emails in Gong"
6. For any missing checkmarks:
   - Click the "Connect" button next to the permission
   - Sign in with your GitLab Google Account when prompted
   - Repeat for each missing permission

Once properly connected, you should see "Currently connected: YourHandle@gitlab.com" displayed in the Emails section.

## How Email Logging Works

Once configured, Gong automatically:

- Captures emails between you and contacts in your CRM
- Associates emails with the relevant accounts and opportunities
- Makes emails searchable and analyzable within Gong
- Maintains email history for account continuity

No manual logging or selection of emails is required - Gong handles this automatically based on your CRM contacts.

## Privacy and Compliance

Gong is configured to:

- Only capture business-related emails with CRM contacts
- Respect GitLab's data protection policies
- Maintain customer confidentiality
- Adhere to relevant privacy regulations

## Troubleshooting

### Common Issues

1. **Emails Not Appearing in Gong**
   - Verify your email connection is active in My Settings
   - Confirm the contact is properly recorded in your CRM
   - Check that your permissions are still valid

2. **Wrong Email Association**
   - Review contact details in CRM
   - Update contact information if needed

### Getting Help

- Contact Gong support through the help portal
- Reach out in #temp-gong-launch Slack channel
- Submit a ticket to the IT team for persistent issues

## Related Resources

- [Gong Documentation](https://help.gong.io)
- [GitLab Email Policy](/handbook/communication/#email)
- [Communication Guidelines](/handbook/communication/)
