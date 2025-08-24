---
title: Very Breached Tickets 
description: Describes Very Breached Tickets and the tools and process to address these.
category: Manager
subcategory: 
last-reviewed: 2023-09-14
---

## Overview

Very Breached Tickets are New tickets that have breached the FRT SLA and remain unresponded to for 2 business days after breaching.  This occurs rarely, but requires urgent intervention when it does occur.  While it would be better to prevent tickets from reaching this state, this process provides a safety-net to catch these occurrences and ensure these tickets receive an FRT response with urgency.

### Very Breached Ticket (VBT) Criteria

A ticket is considered to be a VBT when it meets all of the following criteria:

- Ticket is at FRT (First Response Time) stage
- Ticket has breached the FRT SLA relevant to its priority
- 2 business days have elapsed since the ticket breached FRT SLA

In addition, tickets received on the Emergency form that have breached NRT SLO by 2+ business days will be alerted.

### Customer Impact of Very Breached Tickets (VBT)

When a ticket meets the VBT criteria, the customer has already waited the following durations for a first response to their request:

- High priority ticket:  (4 hour response time) has waited **13 times** the SLA time;
- Normal priority ticket:  (8 hour response time) has waited **7 times** the SLA time;
- Low priority ticket: (24 hour response time) has waited **3 times** the SLA time.

## Alerting Process

The VBT Slackbot runs 3 times per day, near the beginning of business hours for each region.  When VBTs exist at time of execution, it sends a Slack alert in the [`#spt_leaders-daily`](https://gitlab.enterprise.slack.com/archives/C03LL7Z2291) Slack channel with a list of the tickets that meet the criteria.

## Response and outcome

It is expected that all tickets listed in the alert will receive a First Response before the next region's business hours commence. There is flexibility for each region to address the tickets listed as they see fit.  

Once all alerted tickets have a clear plan for a first response, add a `:white_check_mark:` reaction to the bot ping to signal that the alert has been addressed.

Regional details for how the response and outcome are achieved are noted below.

### APAC

- A support manager will add `:eyes:` emoji to the ping to indicate they are DRI for the alert.
  - If there are no `:eyes:` on the ping by 03:00 UTC, the on-call support manager must be DRI.
    - The Manager DRI may instead choose to delegate responsibility to a Senior Support engineer on any given day by `@` mentioning them in a threaded response to the alert and requesting them to assist with finding SEs to provide FRTs to all tickets listed. In this case, the Senior SE will be responsible for applying the `:eyes:` and later the `:white_check_mark:` emojis.
- The DRI will review the list and work with Support Engineers to ensure each ticket is responded to prior to the EMEA alert being executed.
- The VBT DRI role must be done in the earlier part of APAC hours for the following reasons:
  - In general, to avoid VBTs becoming further breached.
  - We need sufficient time to clear out VBTs before EMEA starts (EMEA ping happens at 07:00 UTC).

### EMEA

- TBD

### AMER

- TBD

## APPENDIX: References and resources

- Originating Discussion [Issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/5231)
- Rollout notification [Issue](https://gitlab.com/gitlab-com/support/support-team-meta/-/issues/5486) (Change Record)
- Support Ops VBT Slackbot [project](https://gitlab.com/gitlab-com/support/support-ops/other-software/vbt-slackbot)
