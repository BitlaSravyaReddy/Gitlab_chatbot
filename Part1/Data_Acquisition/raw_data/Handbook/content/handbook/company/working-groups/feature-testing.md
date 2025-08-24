---
title: "Feature Testing Working Group"
description: "Establish the credibility of a permanent alternative to the usage of Capybara for Feature Testing."
status: active
---

## Attributes

| Property          | Value                                                                                                                                |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Date Created      | 2024-11-01                                                                                                                           |
| Target End Date   | 2025-02-01                                                                                                                           |
| Slack             | [#wg_feature-testing](https://gitlab.enterprise.slack.com/archives/C082VBQSFSQ)                                                      |
| Google Doc        | https://docs.google.com/document/d/1ZS4L-vVVVqRAjdOmr4X8ENYD5YEyFxEV8wxuR1OtNvE/edit?tab=t.0                                         |
| Epic              |                                                                 |
| Overview & Status | See [Exit Criteria](#exit-criteria)               |

### Context

The current approach to feature testing, using RSpec and Capybara, has a number of drawbacks:

* Due to lack of coverage or quantity of quarantined specs, the feature suite overall provides limited confidence in code changes and fails to catch regressions.
* Low level of stability leads to high frequency of broken master.
* Limited debugging tools make it difficult to create stable tests and debug flaky ones.
* Maintenance of tests written in Ruby is frequently the responsibility of Frontend engineers, who may or may not have skill in this language.

### Goals

This Working Group has the following goals:

1. Establish the credibility of an alternative JavaScript-based testing system, [Playwright](https://playwright.dev/), as an alternative to Capybara.
2. Create a proof of concept using Playwright with a part of the GitLab platform.
3. Create an architecture blueprint with a strategy on how to migrate to Playwright.

#### Exit Criteria

| Criteria                      | Start Date | Completion Date | Progress | DRI                 |
| ----------------------------- | ---------- | --------------- | -------- | ------------------- |
| CI/CD and environment setup   | 2024-12-11 |                 |          | Javiera Tapia       |
| 3 converted spec examples     | 2024-12-11 |                 |          | Natalia Tepluhina   |
| Migration Plan                |            |                 |          |                     |

#### Details

**CI/CD and environment setup**

Need to determine how to spin up a Playwright server within the GitLab build
process.

**3 converted spec examples**

Full examples for an apples-to-apples comparison with currently flaky tests:

* https://gitlab.com/gitlab-org/gitlab/-/blob/wild-standalone-test/spec/features/boards/boards_spec.rb
* https://gitlab.com/gitlab-org/gitlab/-/blob/wild-standalone-test/ee/spec/features/epic_boards/epic_boards_sidebar_spec.rb
* https://gitlab.com/gitlab-org/gitlab/-/blob/wild-standalone-test/spec/requests/api/commits_spec.rb

The plan is to measure and compare the following metrics:

* % of runs failed
* Time to run spec
* Debugging steps

**Migration Plan**

Strategy to take to gradually migrate to Playwright.

### Update 2025-01-22

#### Current Progress and Challenges

After extensive efforts on the proof of concept to replace Capybara with Playwright, the working group has encountered significant challenges that impede further progress:

* Authentication Issues: Integrating Playwright with our existing authentication mechanisms has proven to be complex and while seemingly solved, it is in a way that makes it difficult to troubleshoot future problems.
* Increased Complexity: Troubleshooting the Playwright POC revealed that migrating to a new testing framework introduces additional layers of complexity, making maintenance and debugging more challenging than anticipated.
* Resource Constraints: The time and resources required to overcome these roadblocks are substantial, diverting focus from other critical testing improvements.

Given these obstacles, the working group recommends discontinuing the current experiment to replace Capybara with Playwright.

#### Recommendation

With the conclusion of the Playwright experiment, the working group has closed. We propose the following recommendations to increase testing coverage and reduce flakiness within our existing Capybara/RSpec framework:

1. Increase Test Coverage:

* Identify Gaps: Conduct a thorough analysis to identify areas with insufficient test coverage and prioritize adding tests to those regions.
* End-to-End (E2E) Tests: Gradually introduce E2E tests for critical user flows, encouraging authoring of these E2E tests by frontend/fullstack engineers.

1. Training and Documentation:

* Skill Development: Provide training sessions for engineers on best practices with Capybara and RSpec to improve test writing and maintenance.

1. Regular Maintenance and Review:

* Flaky Test Identification: Establish a routine for identifying and addressing flaky tests promptly to maintain test suite reliability.
* Continuous Improvement: Foster a culture of continuous improvement where feedback from test runs is regularly used to enhance testing strategies.

By implementing these recommendations, we aim to strengthen our feature testing framework, increase coverage, and significantly reduce flakiness, thereby enhancing overall code quality and stability.

### Roles and Responsibilities

| Working Group Role | Person              | Title                                               |
| ------------------ | ------------------- | --------------------------------------------------- |
| Executive Sponsor  | Tim Zallmann        | VP of Engineering, Core Development                      |
| Facilitator        | Donald Cook        | Engineering Manager, Plan:Project Management             |
| Functional Lead    | Natalia Tepluhina        | Principal Engineer, Plan         |
| Functional Lead    | Ksenia Kolpakova         | Engineering Manager, Test Engineering |
| Functional Lead    | Javiera Tapia            | Backend Engineer, Create:Source Code  |
| Member             | Désirée Chevalier        | Senior Software Engineer in Test, Plan |
| Member             | Doug Stull               | Staff FullStack Engineer in Growth |
