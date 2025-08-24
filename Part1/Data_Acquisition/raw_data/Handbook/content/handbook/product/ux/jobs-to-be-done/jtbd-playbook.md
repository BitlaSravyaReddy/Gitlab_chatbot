---
title: JTBD Research Playbook
description: >-
  GitLab follows a process based on [Jim Kalbach's JTBD Playbook](https://www.amazon.com/Jobs-Be-Done-Playbook-Organization/dp/1933820683) to develop [job canvases](/handbook/product/ux/jobs-to-be-done/jtbd-canvas-anatomy) and identify ranked customer outcomes.
---

This playbook enables all GitLab team members to conduct JTBD research. For a deep dive into each aspect of a job canvas, review the [Anatomy of a JTBD canvas](/handbook/product/ux/jobs-to-be-done/jtbd-canvas-anatomy). Reach out to a UX Researcher or JTBD expert if you have any questions.

### A Note on Time, Confidence, and Validation

Running through the playbook process typically requires at least one quarter. Timelines vary based on job complexity and team JTBD experience.

Creating an unvalidated, assumptive [JTBD canvas](https://www.figma.com/file/Z4lsAOLH1ANN3pstQFYgSk/Jobs-to-be-done----Playbook-Template?type=whiteboard&node-id=0%3A1&t=oMR9VPNke7aIfCoU-1) can be faster and valuable for team alignment. However, even with high domain knowledge, Job Performer interviews are recommended to validate Outcome statements.

Confidence Levels:

- **High/Verified**: Validated through Job Performer interviews
- **Medium/Somewhat Assumptive**: Based on existing user research
- **Low/Assumptive**: Based on domain knowledge without research

### References

- [JTBD overview](/handbook/product/ux/jobs-to-be-done/)
- [Anatomy of a JTBD canvas](/handbook/product/ux/jobs-to-be-done/jtbd-canvas-anatomy)

## Playbook Process

### Create an issue

Create an issue in [UX Research Project](https://gitlab.com/gitlab-org/ux-research/-/issues) using the **[discover-jtbd](https://gitlab.com/gitlab-org/ux-research/-/blob/master/.gitlab/issue_templates/discover-jtbd.md)** issue template. Tag your UX Researcher or ask for support in the `#ux_research` Slack channel.

### Workshop 1: Scope Definition

Using the [JTBD Canvas Template](https://www.figma.com/file/Z4lsAOLH1ANN3pstQFYgSk/Jobs-to-be-done----Playbook-Template?type=whiteboard&node-id=0%3A1&t=oMR9VPNke7aIfCoU-1), you will define your Domain, Job Performer, and Main Job through a one-hour workshop with your Product Design DRI, Product Manager, and optionally Engineering and UX Research team members.

#### Exercise 1: Domain Selection (10 min)

When considering the Domain, ask yourself: Where do you want to innovate?

1. Brainstorm (5 min): List potential domains. Sections, Stage Groups, or Categories may be a good starting point.
1. Select (5 min): Choose one domain and add it to the canvas.

#### Exercise 2: Job Performer Selection (10 min)

When considering the Job Performer, ask yourself: Who are you innovating for? Where is there a need in our market? Who are we passionate about serving? What's relevant or core to our business strategy?

1. Brainstorm (5 min): List actors/stakeholders who relate to the selected domain.
1. Vote (5 min): Each workshop participate votes
   - <3 participants: 2 votes each, you can vote on the same item
   - >3 participants: 1 vote each
1. Move winner to canvas

#### Exercise 3: Main Job Selection (15 min)

When considering the Main Job, ask yourself: What has strategic value? What are we passionate about? What can we best support? What aligns with our business, and what is the Job Performer's core objective?

1. Brainstorm (10 min): List all jobs your selected Job Performer tries to accomplish
1. Vote (5 min): Each workshop participate votes
   - <3 participants: 2 votes each, you can vote on the same item
   - >3 participants: 1 vote each
1. Move winner to Main Job section
1. Move others to Related Jobs section

#### Exercise 4: Aspirations Selection (15 min)

When considering aspirations, ask yourself: What does our Job Performer aspire to become after completing the Main Job? What are their ultimate goals beyond completing this task?

1. Brainstorm (10 min): List what Job Performer wants to become after completing Main Job
1. Vote (5 min):
   - <3 participants: 6 votes each, you can vote on the same item
   - >3 participants: 3 votes each
1. Move top 3 to Aspirations section

### Conduct Investigation Interviews

Conduct 5-10 one-hour interviews with representative Job Performers to understand and validate the bottom half of the JTBD Canvas: Job Map, Emotional/Social aspects, Outcomes, and Job Differentiators. Add more interviews if needed until patterns emerge.

Structure:

- Moderator and notetaker present
- Notetaker documents Job Steps during interview
- Review canvas with participant for accuracy

Interview Goals:

- Map [Job Steps](/handbook/product/ux/jobs-to-be-done/jtbd-canvas-anatomy#job-steps-how-does-the-job-performer-get-the-job-done)
- Identify [desired Outcomes](/handbook/product/ux/jobs-to-be-done/#Outcomes-how-does-the-job-performer-measure-the-success-of-getting-the-job-done)
- Discover [Related Jobs](/handbook/product/ux/jobs-to-be-done/jtbd-canvas-anatomy#related-jobs-what-else-is-the-job-performer-trying-to-get-done)
- Understand [Job Differentiators](/handbook/product/ux/jobs-to-be-done/#circumstances-what-are-the-factors-or-condictions-that-make-a-difference-in-how-the-job-gets-done)

See the Figjam template [interview guide](https://www.figma.com/file/Z4lsAOLH1ANN3pstQFYgSk/Jobs-to-be-done----Playbook-Template?type=whiteboard&node-id=78-2318&t=oMR9VPNke7aIfCoU-4) for helpful prompts.

### Complete Canvas

After interviews, synthesize the collected information into your JTBD Canvas, focusing on common patterns and discarding outliers. Consider collaborating with a UX Researcher for their expertise in [data synthesis](/handbook/product/ux/ux-research/analyzing-research-data/).

#### Exercise 1: Complete Job Map

1. If per-interview Job Maps were not created during interviews, create them now:
   - Capture steps chronologically by reviewing interview notes/videos
   - Rewrite steps following the [Job Step guidelines](/handbook/product/ux/jobs-to-be-done/jtbd-canvas-anatomy#job-steps-how-does-the-job-performer-get-the-job-done)
1. Create unified Job Map:
   - Group steps into Beginning, Middle, and End categories
   - Organize related steps into vertical stacks
   - Label stacks with a high-level, single-word verb descriptor

#### Exercise 2: Construct Outcome Statements

1. Identify how the Job Performer would measure the success of completing the Main Job and create a sticky for each success measure
1. Format following the [Outcome guidelines](/handbook/product/ux/jobs-to-be-done/#Outcomes-how-does-the-job-performer-measure-the-success-of-getting-the-job-done)
1. Aim for 50-100 statements for [later validation](#outcome-opportunity-scores-survey)

#### Exercise 3: Synthesize Emotional and Social Aspects

1. Emotional Aspects:
   - Extract references to how the Job Performer feels when performing the Main Job
   - Format per [guidelines](/handbook/product/ux/jobs-to-be-done/#Emotional-and-Social-aspects-how-does-the-job-performer-feel-while-doing-the-job-how-do-they-want-to-be-perceived-while-doing-the-job)

2. Social Aspects:
   - Extract references to how the Job Performer wants to be perceptived when performing the Main Job
   - Format per [guidelines](/handbook/product/ux/jobs-to-be-done/#Emotional-and-Social-aspects-how-does-the-job-performer-feel-while-doing-the-job-how-do-they-want-to-be-perceived-while-doing-the-job)

#### Exercise 4: Gather Job Differentiators

1. Identify factors that affect how the Job Performer completes Main Job
1. Format per [guidelines](/handbook/product/ux/jobs-to-be-done/#job-differentiators-what-are-the-factors-or-conditions-that-make-a-difference-in-how-the-job-gets-done)

### Workshop 2: Map and Prioritize

Using your Job Canvas, you will select your Job Steps, Emotional & Social Aspects, and Job Differentiators through a one-hour workshop with your Product Design DRI, Product Manager, and optionally Engineering and UX Research team members.

#### Exercise 1: Review and Select Job Steps (15 min)

When considering the most important job steps, ask yourself: Which steps are most challenging yet crucial to success?

1. Review Job Map (5 min)
   - Verify accuracy against interview data
   - Make necessary adjustments
1. Vote on Critical Steps (10 min)
   - <3 participants: 2 votes each, you can vote on the same item
   - >3 participants: 1 vote each
1. Discuss votes to align on priorities
1. Identify top voted steps
1. Copy final Job Map to canvas, marking selected steps

#### Exercise 2: Select Emotional Aspect Statements (10 min)  

When considering emotional aspects, ask yourself: Who are you innovating for? Where is there a need in our market? Who are we passionate about serving? What's relevant or core to our business strategy?

1. Review (5 min)
   - Share emotional aspects with team
   - Ensure understanding
1. Vote (5 min)
   - <3 participants: 6 votes each, you can vote on the same item
   - >3 participants: 3 votes each
1. Arrange votes in priority pyramid
1. Confirm team alignment on top choices
1. Move top emotional aspects to canvas

#### Exercise 3: Select Social Aspect Statements (10 min)

Repeat Exercise 2 to select the Social Aspect Statements.

#### Exercise 4: Select Job Differentiator Statements (10 min)

Repeat Exercise 2 to select Job Differentiator Statements.

🎉🥳 Congratultations you have successuflly created a validated JTBD Canvas! 🥳🎉

### Outcome Opportunity Scores Survey

Run this survey using the [qualtrics template](https://gitlab.eu.qualtrics.com/survey-builder/LS_2l5ektxWK1wFRuC/edit?ContextLibraryID=GR_6ziMa2ooJx4Y6SF) to prioritize your Outcome Statements. It is recommended to work with your UX Researcher to craft and delivery this survey.

For each Outcome Statement, ask:

1. How _important_ is this (Outcome) to you?
2. How well is this (Outcome) currently being _satisfied_?

Requirements:

- Screen for participants who perform the Main Job
- Target ~50 qualified responses
- Include both GitLab and non-GitLab users
- Use 10-point scale (1='very low', 10='very high')

Resources:

- [Analysis spreadsheet](https://docs.google.com/spreadsheets/d/109GZqTYPpOLpHLj-gwV_ldMFwIKa9MaaLPyLJ4kdoQs/edit?usp=sharing)

#### Calculating Scores

[The analysis spreadsheet template](https://docs.google.com/spreadsheets/d/109GZqTYPpOLpHLj-gwV_ldMFwIKa9MaaLPyLJ4kdoQs/edit?usp=sharing) offers a step by step guide to exporting data from a Qualtrics survey and generating a ranked list of Outcome statements with opportunity scores.

[Opportunity scores](https://medium.com/uxr-microsoft/what-is-the-opportunity-score-and-how-to-obtain-it-bb81fcbf79b7) run from 0-20. Even scores below 10 indicate room for improvement - prioritize highest scores within your range.

![JTBD Opportunity Score](/images/product/ux/jobs-to-be-done/JTBD_OpportunityScore.png)

1. Satisfaction gap: Importance - Satisfaction
1. Opportunity score: Importance + Satisfaction gap

| Score | Priority Level |
|-------|---------------|
| 16-20 | Immediate action needed |
| 10-15 | High priority |
| 7-9   | Monitor |
| ≤6    | Lower priority |

### Generate Job Stories

Job Stories synthesize data from your Job Canvas to encapsulate customer pain points without prescribing solutions. They help align development with company vision and strategy. Each domain typically has 3-5 Job Stories.

Key characteristics:

- Evidence-based from Job Canvas data
- Specific about the pain point
- Builds empathy through context
- Aspirational but achievable
- Self-evident and well-researched

Pain points must:

- Express needs, not solutions
- Be concrete, not abstract
- Be measurable, not anecdotal

#### Job Story Format

1. **When I** [at this Job Step] + [under the conditions of these Job Differentiators]
2. **I want** [this New Ability/customer imperative]
3. **So I can** [reach these Outcomes] + [and have these Emotional/Social Aspects]

#### Ways to use Job Stories

- Generate How Might We (HMW) statements
- Define Design Sprint challenges
- Create testable MVP hypotheses:
  - We believe that [job performers]
  - Will achieve [desired outcome]
  - While performing [job step]
  - Using [proposed solution].
  - Success will be evidenced by [specific measure]
- Ensure issues are solving validated problems
- Define usability testing criteria

<!-- Figure out how to incorporate this into UX Theme workshop

### Align on Ranked Outcomes: Workshop

Here's where the magic happens. If you have the ranked Outcomes by opportunity score from your survey, you have a list of the areas that will be most impactful to your users' experience of your product. Now is the time to meet with your stakeholders and discuss the top ranked Outcomes. Our [FigJam template](https://www.figma.com/file/Z4lsAOLH1ANN3pstQFYgSk/Jobs-to-be-done----Playbook-Template?type=whiteboard&node-id=0%3A1&t=qrubQYZLbPWYJjN3-1) has a workshop template and guide you can use to help address each Outcome statement.

A few things to think about during the workshop:

- Are the Outcomes already being addressed with current and planned work? If not, should they be incorporated into future planning?
- Where in the product is each Outcome done? Are there specific pages, controls, or parts of the UI that we can focus on?
- Who owns each Outcome? Are there other teams that 'own' some of the areas of opportunity? Who can you speak with to see if they are working on this Outcome already?
- What can be done to achieve the stated Outcome? Think of some potential solutions.

The result of the workshop should be that the team understands the top opportunities for that Main Job and Job Performer, and has discussed ways to address them.

You and your team now have a list of the most important areas to focus on - a list that you can share with other teams and stakeholders (even customers!) to help bring clarity and confidence to your product roadmap.

The list of opportunities will remain relevant for a long time (until you release changes to your product that address the opportunities), because they aren't based on particular features or solutions, but larger Outcomes that users want to achieve. Re-survey your Job Performers about certain Outcome statements after your team has made some changes, in order to see if the opportunity score has decreased (meaning you've made positive progress to fulfilling the desired Outcome).

-->

<!-- TODO: Connect to UX Themes (in a future MR) -->
