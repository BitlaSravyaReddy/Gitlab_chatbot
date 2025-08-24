---
title: Ticketing Style Guide
category: Handling tickets
subcategory: Writing responses and handling feedback
description: Guidelines on structuring ticket responses.
---

## Why do we need a Ticketing Style Guide?

To maintain the quality of our customer experience as the Support team grows, we have gathered a collection of best practices and suggestions for styling and responding to Zendesk tickets.

Consistency is what enables any Support Engineer to jump into an unfamiliar ticket and get to work fairly quickly. Consistency enables scaling, and consistency is what we're hoping to achieve with this guide.

Some of the suggestions in this guide will encounter cases that warrant exceptions, and that's OK.

Everyone in the Support Team is welcome to contribute or modify the suggestions in this guide given that they provide the "Why", especially when a practice has proven to work, or not work for them through experience.

## Readability

1. If your reply consists of more than 6 lines, consider breaking it to sections using HEADERS. Example:

   ```text
   ### Logs analysis

   In reviewing your logs we've noticed the following highlights:
     1. ...
     2. ...
     3. ...

   ### Next steps

   It looks like you're hitting [this issue](issue-link)

   Let's try the following:
     1. Perform some action `A` followed by a `gitlab-ctl reconfigure`.
     2. If the output is `X`, then try `Y`.
   ```

   This will help the customer as well as fellow support engineers to quickly find the information they're looking for.

1. Aim to add a **public 1 line summary** of the latest current issue for every 3 replies you send to the customer. Example:

   ```text
   Thanks for providing all this info.

   ### Current Status

   So far we've established that you're facing a 500 error intermittently when loading an MR. This also seems to happen only for MRs with large diff content.

   ### More sections
   ```

1. For lengthy or more complicated tickets, a more detailed summary can be very helpful. For example:
   
   ```text
   ### Problem
   - States what exact issues the customer is experiencing
   ### Context
   - Versions, recent changes to their instance, deployment type, etc.
   ### What we've ruled out
   - Useful when taking over an NRT
   ### Theories
   - Potential explanations of the problem
   ### My questions
   - My questions for further investigation
   ### Customer questions
   - Questions the customer wants answered
   ### Next steps
   - Questions/requests for the customer, things Support needs to do, etc.
   ```

   This will ensure that the customer and you remain on the same page regarding what the issue is.

   This will also help other support engineers to jump into the ticket and catch up on the context more efficiently.

## Technical Content

1. Summarize your understanding of the customer's issue to verify that you are pursuing a valuable troubleshooting path. Customers may focus on one detail or desired outcome, but overlook other necessary information which you want to review. Ensuring you and the customer share a common understanding of the issue and the path forward is very important.

1. Ask for `gitlab.rb`, or any other missing information or logs, but don't let your reply consist of only that. Describe why you're asking for the additional info. Example:

   ```text
   Would you please provide your `gitlab.rb` for all your nodes? Specifically, I'm interested in seeing your Redis configuration for each node.

   It is possible that you've configured the caching differently in each node, which could result in inconsistent behaviors such as what we're seeing in this case.
   ```

   This will help the customer understand how they can debug this issue themselves.

   It will also help other support engineers to understand what you were aiming to look for in the provided data, and keep the debugging direction consistent over the next replies.

1. When requesting logs from the customer, only ask for as much as you think you'll need to diagnose the problem. Example:

   ```text
   If the issue is reproducible and is not front-end related, ask for `gitlab-ctl tail`, if it's intermittent, ask for GitlabSOS.
   ```

   This makes it easier to debug the issue as you'll go through the minimal number of log files, and save the customer from breaking up a large GitLabSOS file, unless GitlabSOS is necessary.

1. If you have multiple questions for the customer, consider numbering your questions throughout the ticket. For example:

   ```text
   - Q1: What is your current version of GitLab?
   - Q2: What upgrade steps did you perform prior to this issue occurring?
   - Q3: Can you share your gitlab.rb file for review?
   ```

   This can help to organize the information you need, and also avoid repeating questions. If a question is not answered, you can refer back directly by asking `Can you help by providing the response to Q2?`
