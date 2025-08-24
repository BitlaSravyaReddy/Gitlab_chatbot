---
title: "Asana"
description: "Asana is a collaborative work management platform that will support GitLab's mission to enable everyone to contribute to and co-create the software that powers our world. GitLab's Marketing team is planning to use Asana to track projects (e.g., Product Launches), connect work to goals, and coordinate work across the team. Asana will have access to Orange data including pre-release product launch information and GitLab issues and epics in private projects."
---

## About Asana

[Asana](https://app.asana.com/) is a collaborative work management platform that will support GitLab's mission to enable everyone to contribute to and co-create the software that powers our world. GitLab's Marketing team is planning to use Asana to track projects (e.g., Product Launches), connect work to goals, and coordinate work across the team.

## Why?

Our team is using Asana to add a made-for-marketing project and task management tool so that we can streamline and simplify projects and processes, improve efficiency, collaboration, and transparency, and free up time for our team to better understand how our customers use GitLab.

We've consistently heard from team members across the marketing org that there is an opportunity to improve efficiency. The main problems we are looking to solve are:

- Stretching GitLab to perform as a project management tool for Marketing processes it was not built for, and use cases it will never be used for by our customer base.
- This can cause undue administrative work, bottlenecks and detracts from our day-to-day commitment to efficiency.
- Adding a made-for-marketing project and task management tool will improve efficiency, freeing up time for our team to learn about and understand how our customers use GitLab

## Users

Asana licenses will be rolled out across the entire Marketing Org.

View Only licenses are available to all GitLab team members. If you would like a view only license, please request access in Lumos (please be sure to select View Only permission).

## User Provisioning Guide

### Overview

GitLab team members can request Asana access through the Lumos app store. This guide outlines the provisioning process for Marketing Operations team members.

### Request Flow

1. **Team Member Request**: GitLab team member submits Asana access request via Lumos app store
2. **Manager Approval**: Request is automatically sent to the requester's manager for approval
3. **Marketing Ops Review**: Once approved by manager, request is forwarded to Marketing Operations for provisioning

### Access Entitlements

#### Marketing Team Members

- **Entitled to**: Full Asana license
- **Provisioning method**: Automatic via SCIM (approve in Lumos)

#### Non-Marketing Team Members

- **Entitled to**: View-only access
- **Provisioning method**: Manual invitation through Asana admin console and Lumos

### Provisioning Process

#### Step 1: Verify Team Membership

Check if the requester is on the Marketing team to determine their access entitlement.

#### Step 2A: Full License Request (Marketing Team Member)

If the requester is on the Marketing team and requesting a full license:

1. Approve the request in Lumos
2. User will be automatically provisioned via SCIM

#### Step 2B: Full License Request (Non-Marketing Team Member)

If the requester is NOT on the Marketing team but requested a full license:

1. Comment on the Lumos thread explaining they are only entitled to view-only access
2. Ask the requester to re-submit their request specifically for view-only access
3. **Deny the original Lumos request** (requests cannot be edited)

#### Step 2C: View-Only Request (Any Team Member)

For view-only access requests, manual provisioning is required:

##### Manual Invitation Process

1. Navigate to the [Asana admin console](https://app.asana.com/admin/306855239930259/members)
2. Click **"Invite Members"** in the top right corner
3. In the invitation dialog:
   - **Email**: Paste the requester's email address
   - **Team**: Select `All Marketing` from the "Add to team" dropdown
   - **Projects**: Optionally select specific projects to add them to
   - **License**: Select **"View Only"** from the license dropdown
4. Send the invitation
5. **Important**: Click **"Confirm Provisioning"** on the Lumos request

### Key Points to Remember

- **Marketing team members** are entitled to full licenses
- **Non-marketing team members** are entitled to view-only access only
- **Full license requests** from non-marketing members must be denied and re-submitted as view-only requests
- **View-only access** always requires both manual provisioning through the Asana admin console and confirmation in Lumos
- **Always confirm provisioning** in Lumos after completing manual invitations

### Quick Reference

| Requester Team | Request Type | Action |
|----------------|--------------|--------|
| Marketing | Full License | Approve in Lumos (auto-provision via SCIM) |
| Non-Marketing | Full License | Comment, ask to re-submit for view-only, deny request |
| Non-Marketing | View Only | Manual invitation + Confirm in Lumos |

## How to get help with Asana

If you have questions, first self-service by reviewing this Handbook page, [Asana Help Center](https://help.asana.com/s/?language=en_US), and/or [Asana Academy](https://academy.asana.com/). If you cannot find a solution on your own, feel free to let us know using this [GitLab Internal Support Form](https://form.asana.com/?k=rIdwTWezTYqZhSI9vgJZsQ&d=306855239930259).

## Self-Paced Learning

The [Asana Academy](https://academy.asana.com/) is a great resource with live and on-demand webinars and workshops.

## Getting Started in Asana

### Tasks

Tasks are the basic unit of action in Asana. Tasks are most similar to GitLab issues. You can create new tasks, duplicate an existing task, merge two tasks together, create subtasks, or delete a task. Create a task if you have a smaller effort that logically fits into an existing Project.

Asana is most useful when individuals can contribute ideas and move action items forward. Tasks are the foundational work items within Asana. Task names should be specific, clear, and action-based. Use a verb where possible. For example, instead of titling a task “Blog post,” title it “Write [title] blog post” and create a second task called “Publish [title] blog post.”

#### Tasks Descriptions

A task description should give the assignee all the necessary information to complete the task. Here are some tips:

- Link to relevant work in the task description by `@mentioning` related people and hyperlinking relevant tasks, projects, or messages.
- Add links and attachments to include external work, centralizing information.
- Mark a task as dependent upon another, so teammates start that task when the prior task is completed.
- Use rich text in task descriptions to clarify your message with formatted text and lists.

#### Assigning Tasks

Every task in Asana can have only one assignee, who serves as the Directly Responsible Individual (DRI). This person is accountable for ensuring the task is completed. However, tasks often require collaboration with multiple team members. Here's how to effectively manage task ownership and collaboration:

##### DRI (Task Asignee) Guidelines

The DRI should be:

- The person primarily responsible for the outcome of the work
- Someone with the authority to make decisions about the task
- Available during the task's timeline

##### Collaboration Structure

Task collaborators (followers) should include:

- Stakeholders who need to stay informed
- Team members providing input or review
- People who need visibility into the task's progress
- Project managers overseeing the work

To add collaborators:

1. Click the "+" button in the task's collaborators field
1. Search for and select team members
1. Or use @mentions in comments to automatically add collaborators

##### When to Use Subtasks for Team Collaboration

When you assign a subtask, be sure the assignee has enough context from the parent task or within the subtask description. Avoid burying subtasks under too many layers. You can always convert subtasks to tasks.

Create subtasks when:

- Different team members are responsible for distinct pieces of work
- A task requires multiple sequential steps with different owners
- You need to track individual contributions within a larger task

Example structure:

Main Task: Q4 Blog Post Launch [DRI: Content Manager]
  └─ Subtask 1: Draft content [DRI: Writer]
  └─ Subtask 2: Design graphics [DRI: Designer]
  └─ Subtask 3: SEO review [DRI: SEO Specialist]
  └─ Subtask 4: Final approval [DRI: Content Manager]

#### Task Best Practices

- Provide clear context in the task name and description
- Provide a realistic and reasonable due date. As a team, you can decide how due dates are changed. Communicate in the comments of a task to indicate if a due date is flexible, or to re-negotiate a due date if needed.
- Hypertext relevant tasks or projects by @mentioning a person, project, task, or team.
- Add task collaborators to keep your team informed.

### Projects

Projects are used to organize and track all of the steps that must completed for a process or initiative. A project helps you map out the work needed to complete an initiative, maintain a process, or hit a goal. Projects are most similar to GitLab Epics.

Create a project if you have a large effort (10+ tasks) that involve a subset of an existing Team or the whole Team.

#### Creating and naming new projects

Projects allow you to organize all tasks related to a specific initiative, goal, or significant work in one place. Similar to tasks, anyone can create a project.

There are three general types of projects and associated naming conventions. Naming conventions can help keep your tasks and projects organized and help your team find information more quickly. When creating a new project, first decide what type of project you are creating.

1. Deadline-bound projects have a clear start and end date and clear exit criteria
   a. [FYXX] - [Subteam Name] - [Concise Project Name]
      i. FY25 - Product Marketing - GitLab Duo Launch Plan
      ii. FY25 - Content - Blog Post - Enterprise Agile Planning
2. Ongoing/Operational Processes represent an ongoing process with no specific end. Work moves through a repeatable set of stages
   a. OP - Calendar - Events
   b. OP - Calendar - Email
   c. OP - Intake - Marketing Ops
3. Reference Projects are a way to capture and organize information. These projects do not contain any actionable work.
   a. REF - Asana Naming Conventions
   b. REF - Events - AMER - Preferred Vendor List

#### Project Templates

Create a custom template or use an Asana created template to standardize common workflows and projects. Templates help get projects off to a quick start and ensure you haven’t missed any vital steps.

## When to Use Asana vs Other Tools

### Quick Decision Guide

Before starting your work, ask yourself:

- Is this Marketing Division work that involves multiple stakeholders? → Use Asana
- Is this a code change or technical documentation? → Use GitLab
- Do you need immediate, real-time communication? → Use Slack

### Detailed Breakdown by Tool

#### Asana: Project & Task Management

**Best for:**

- Marketing campaign planning and execution
- Cross-functional collaboration within Marketing
- Project tracking and status updates
- Action items and next steps
- Task delegation and progress tracking

#### Slack: Real-time Communication

**Best for:**

- Quick questions
- Real-time collaboration
- Team announcements
- Informal discussions

#### GitLab: Technical Work, Documentation, and Collaborating Outside of Marketing

**Best for:**

- Handbook updates
- Code changes / merge requests
- Opening issues to request support from teams outside of Marketing

### Cross-Tool Workflows

#### Asana + GitLab

1. Create the main project in Asana
2. Create relevant GitLab issues
3. Link the GitLab issues in your Asana tasks (in task description or use a custom field)
4. Update status in Asana, technical details in GitLab
5. Document important decisions or updates from the issue in Asana

#### Asana + Slack

1. Keep all project details and discussions about the project in Asana
2. Use Slack for time-sensitive updates only, or for cross-posting links to important Asana updates
3. Document important Slack decisions in Asana
4. Share Asana task links in Slack when needed

#### Example of Cross-Tool Workflow

##### Website Update Project

**Asana:**

- Main project management
- Timeline tracking
- Stakeholder updates
- Content approvals

**GitLab:**

- Merge requests
- Technical documentation
- Implementation details

**Slack:**

- Urgent deployment questions
- Quick status checks

#### Best Practices

**Do:**

- Create Asana tasks that link to relevant GitLab issues
- Move Slack discussions to Asana tasks when they become actionable items
- Use Asana for all project-related communications and updates
- Document important Slack and/or GitLab decisions in Asana

**Don't:**

- Create duplicate tracking systems across platforms
- Have lengthy project discussions in Slack
- Use GitLab for marketing task management
- Keep project documentation solely in Slack

#### Need Help Deciding?

If you're unsure which tool to use:

1. Consider who needs to be involved
2. Think about the type of work being done
3. Assess the timeline and urgency
4. When in doubt, start in Asana and link to other tools as needed

**Remember:** The goal is to keep related work together while using each tool for its strengths. When in doubt, ask yourself "Where would others look for this information?"

## Integrations with Asana

### GitLab

Certain GitLab issues auto-create Asana projects and tasks based on a custom built workflow. More details to be added, but currently only available as a part of the Field Marketing workflow from Allocadia > GitLab > Asana. The majority of tasks and requests should live solely in Asana, please utilize the guide above to know when and how to use GitLab vs Asana.

Details about integration (To be documented)

### Slack

Turn any Slack message into an actionable Asana task with just a few clicks. A few things you can do:

1. Create a new task, assign it to yourself or a teammate, and add it to an existing project
2. Mark a task complete, or make a comment
3. Receive updates on task creation, completion, or
4. Stay up to date on projects with AI-generated Summaries
   - Once an Asana task link is pasted in Slack, you can simply click on the "Summarize task" button and a summary is generated.
   - You can ask questions Asana AI in Slack to understand the latest updates on projects and tasks, identify next steps, uncover key blockers, and more.
5. Create rules in Asana to trigger updates to Slack channels.

### Google Workspace

#### Google Docs & Sheets 

Connection will allow you to paste Asana projects/tasks and have them format well within the doc. To create tasks, you must use the Chrome Extension.

#### G-Mail
 
Turn emails into tasks by syncing email threads into Asana. You can also mark tasks as complete, reply and post comments from notifications sent to your inbox.

#### Google Drive

If you are using the Asana App, in order to connect your GDrive, follow these steps: (must have YubiKey)

1. Make sure your YubiKey is registered in Okta
2. Start the connection process using this guide - https://asana.com/apps/google-drive
3. After entering your email address, you'll be prompted for your Okta password. Please enter that.
4. Next you'll be prompted to use biometrics, but no pop-up will appear. Simply press the YubiKey at this point and the login process should continue.
5. You may see a black window for a few seconds. Please keep this window open and wait for the next step to load.
6. Confirm that you want to link the account.

#### Google Calendar  

Sub-region and country calendars can be syce via Google Calendar, regardless of Asana license. GitLab team members interested in subscribing to a sub-region or country calendar via Google Calendar should visit the [Asana Internal Handbook page](https://internal.gitlab.com/handbook/marketing/marketing-ops-and-analytics/marketing-operations/asana/#sub-region-and-country-views) for instructions.

### Chrome Browser

Utilize the Asana plugin in your chrome browser to quickly create tasks and add to projects.

### Figma

Limited integration, but allows you to view live embeds of Figma diagrams and charts directly inside of project briefs.

**In Figma**

- Open the file you want to embed in your Project Brief.
- To link to a specific frame in the Figma file, select the frame.
- Click the Share button in the toolbar.
- Update your link sharing permissions to determine who can view and interact with the file embed (Optional).
- Click Copy link when you're ready to embed the file.

**In Asana**

- Open the project where you'd like to embed a Figma file.
- Go to the Overview tab.
- In the Key Resources section, click Create a Project Brief. If there's already a Project Brief, click anywhere on the title.
- When the Brief opens, click Edit in the top right.
- Click the place in the Brief you'd like to embed.
- Paste in the Figma link and a preview will expand below it.
- You can also click the + icon to the left of the line you're on and choose Insert Media. Paste the Figma link into the box and click Embed link.
