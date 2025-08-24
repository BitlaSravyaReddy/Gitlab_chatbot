---
title: Restoring Deleted Data Requests for GitLab Dedicated
category: GitLab Dedicated
description: "Workflow for cases when a customer requests deleted projects or groups to be restored on GitLab Dedicated."
last-reviewed: 2025-03-13
---

## Overview

Use this workflow when a customer requests that we restore projects or groups that have been deleted from a GitLab Dedicated instance. This workflow is specifically for handling deletions of projects and groups.

## Process

1. Work with the customer to explore the self-serve options for recovering this data. Specifically:
   1. Have the customer [view project pending deletion](https://docs.gitlab.com/user/project/working_with_projects/#view-projects-pending-deletion). If [delayed project deletion](https://docs.gitlab.com/user/project/working_with_projects/#delayed-project-deletion) is enabled, they may be able to **Restore** the deleted project(s).
   1. Have the customer check whether having one of their team members [`git push` a local clone](https://docs.gitlab.com/topics/git/project/) would suffice, clarifying that project issues, merge requests, settings etc. won't be recovered. 
1. If the customer can not self-serve the recovery, inform them that we will not be able to assist further with the request 

If you are unsure how to communicate this news to the customer, ask in [#support_gitlab-dedicated](https://gitlab.enterprise.slack.com/archives/C058LM1RL3V) or reach out to the customer's CSM for guidance.

The [Disaster recovery](https://docs.gitlab.com/subscriptions/gitlab_dedicated/data_residency_and_high_availability/#disaster-recovery) feature in GitLab Dedicated is intended for complete disaster recovery scenarios.

## Additional Resources

- [Restoring Deleted Data Requests](restore_requests.md) for GitLab.com
- [Updates to GitLab’s delayed deletion feature for projects and groups](https://about.gitlab.com/blog/2023/04/03/delayed-deletion/)
