---
title: "Developer Experience Project Management"
description: "Guidelines for project management for the Developer Experience Stage at GitLab"
---

#### Established Projects

Established Projects are those that have proven their value, are mature, and are fully integrated into regular department workflows. These projects are critical to the department's operations and require ongoing management and development.

- Ensure that the project is created under the respective Group within the [Developer Experience Group](https://gitlab.com/gitlab-org/dx) for organizational alignment.
- Make projects [Public or Internal](https://docs.gitlab.com/ee/user/public_access.html) based on the required usage needs.
- Add Ownership details for the established project by following below steps:
  - Navigate to your project and select "Settings" > "General".
  - In the General settings, find and expand the "Badges" section.
  - Enter "Maintainers" as the badge name.
  - Provide the link to the team page in the handbook. This should be the team-specific page that lists the team Slack handle, team members, and board details.
  - Use a custom badge image URL structured as suggested: `https://img.shields.io/badge/maintained_by-{{team_name}}-blue`. Replace `{{team_name}}` with the appropriate Group under Developer Experience.
  - After filling in the details, select "Add badge" to create the maintainer badge.
  - If there are multiple maintainers, create separate maintainer badges
- Adhere to [GitLab's code of conduct and privacy policies](https://about.gitlab.com/community/contribute/code-of-conduct/).

#### Project Deprecation

Deprecation of a project is a significant decision and should be based on clear, objective criteria. Here are the key factors to consider:

- Decline in usage metrics over a sustained period.
- Lack of relevance to current organizational goals or technology trends.
- Existence of newer tools or platforms that effectively replace the project's functionality.

The process of deprecating a project should be methodical and transparent to all stakeholders:

- Conduct a thorough review of the project against the deprecation criteria.
- Inform all stakeholders, including project maintainers, users, and dependent teams, about the decision to deprecate.
- For an established project, ensure all valuable data and documentation are securely [archived](https://docs.gitlab.com/ee/user/project/settings/migrate_projects.html#archive-a-project).
- Archive the project. This action will make the project read-only and prevent further changes. If needed, it can be unarchived in the future.
- Consider [deleting the project](https://docs.gitlab.com/ee/user/project/working_with_projects.html#delete-a-project) after a three-month window from the archival for established projects. Deletion can be performed immediately for personal and POC projects once the purpose is served.

## Project Management

Our sub-department's work can span over 10k+ issues hence as a result, we have specific team boards for the 3 teams in Test Platform Sub-department.

### Test Governance

[This board](https://gitlab.com/groups/gitlab-org/-/boards/7364900?label_name%5B%5D=Test%20Governance%20FY25-Q4) shows the current ownership of workkload / issues related to Test Governance.

### Development Analytics

[This board](https://gitlab.com/groups/gitlab-org/-/boards/8966549?label_name%5B%5D=group::development%20analytics) shows the current ownership of workload / issues related to Development Analytics.

### Developer Tooling

[This board](https://gitlab.com/groups/gitlab-org/-/boards/8974136?label_name%5B%5D=group::developer%20tooling) shows the current ownership of workload / issues related to Developer Tooling.
