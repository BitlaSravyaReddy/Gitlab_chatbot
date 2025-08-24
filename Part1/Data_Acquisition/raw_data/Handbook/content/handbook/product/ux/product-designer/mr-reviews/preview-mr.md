---
title: Preview Merge Request Changes
description: "How to preview merge request (MR) changes, to review, test, or even contribute them."
---

## Overview

This page shows different ways to preview merge request (MRs) changes.
For the full review process, see [Product Designer MR Reviews](/handbook/product/ux/product-designer/mr-reviews).

## Preview options

You can preview MR changes for the app, documentation, Pajamas, or company handbook using these methods:

- **Gitpod** ([Get started](#gitpod) and [Help](#help)): Cloud environment that provides a ready-to-use app with one click. Works for GitLab instances (using GDK, see below), docs, Pajamas, and handbook.
- **GitLab Development Kit (GDK)** ([Get started](#gdk) and [Help](#help)): Run GitLab on your local machine. Requires technical knowledge and can break during updates.
- **Review Apps** ([Get started](#review-apps)): Unique links created for each MR. Great for documentation but limited for GitLab instances ([improvements planned](https://gitlab.com/groups/gitlab-org/-/epics/6660)).
- **Sync with author**: Although we have a [bias towards asynchronous communication](/handbook/values/#bias-towards-asynchronous-communication), sometimes a quick call with the MR author is the most efficient approach.

{{% details summary="Comparison table" %}}

| | Gitpod (cloud) | GDK (local) | Review App | Sync with author |
|------|------|------|------|------|
| First start* | 🏃‍♀️ Fast (<5 min) | 🐢 Very slow (30+ min) | GitLab (>30 min)<br>Docs (>20 min)<br>Pajamas (~10 min)<br>Handbook (~10 min)| 🏃‍♀️ Fast (few mins) |
| Restarts | 🏃‍♀️ Fast (<2 min) | 🤷 Depends on your machine | 🚀 Very fast (secs) | 🏃‍♀️ Fast (few mins) |
| Make changes | ✅ | ✅ | ❌ | ✅ |
| Preview/test | ✅ | ✅ | ✅ | ✅ |
| Save state<sup>§</sup>| ✅ | ✅ | ✅ | N/A |
| Toggle feature flags | ✅ | ✅ | ✅ | ✅ |
| Test data for GitLab instances | ✅ | ✅ | ✅ | N/A |

{{% /details %}}

### Contributing

Product Designers should have general knowledge of Git and DevOps flows. Using GitLab in a live environment and making small contributions helps build:

- Empathy for user workflows.
- Understanding of the product.
- Skills to make small improvements directly (UI copy, component migration, etc.).

### Gitpod

To use Gitpod:

1. Create a free Gitpod account.
1. Connect it to your GitLab account. This happens automatically when launching from GitLab.com, but if it doesn't work,
see [how to manually connect them](https://www.gitpod.io/docs/configure/authentication/gitlab#connecting-your-gitlab.com-account).

Resources:

- [Launch Gitpod](https://docs.gitlab.com/integration/gitpod/#launch-gitpod-in-gitlab)
- [Gitpod for the GitLab project](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitpod.md) (i.e. cloud GDK)
- [📺 Get started with Gitpod](https://www.youtube.com/watch?v=AOn7orCcTx8&list=PL05JrBw4t0KqrLsB8wlEhl2F9hXZlMmNR&index=13)
- [📺 Review MRs with Gitpod](https://www.youtube.com/watch?v=M7b19Dq-1tw&list=PL05JrBw4t0KqrLsB8wlEhl2F9hXZlMmNR&index=11)
- [GDK commands](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/gdk_commands.md) (start, stop, update, etc.)
- [Preview/change GitLab](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/preview_gitlab_changes.md)
- [Preview/change docs](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitlab_docs.md)
- [Apply GitLab paid license](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/index.md#use-gitlab-enterprise-features)
- [Configure additional GitLab features](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitpod.md#configure-additional-features) (runners, feature flags, advanced search, etc.)
- [More how-to topics for GDK](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/index.md)
- [Check out branches](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitpod.md#check-out-branches)
- [Commit and push changes](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitpod.md#commit-and-push-changes)
- [Prevent auto-deleting workspaces](https://www.gitpod.io/docs/configure/workspaces/workspace-lifecycle#garbage-collection)
- [Gitpod official documentation](https://www.gitpod.io/docs)

### GDK

- [One-line installation](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/index.md#one-line-installation)
- [📺 Review MRs with GDK](https://www.youtube.com/watch?v=M7b19Dq-1tw&list=PL05JrBw4t0KqrLsB8wlEhl2F9hXZlMmNR&index=11)
- [Browse your dev server](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/browse.md)
- [GDK commands](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/gdk_commands.md) (start, stop, update, etc.)
- [Preview/change GitLab](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/preview_gitlab_changes.md)
- [Preview/change docs](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/gitlab_docs.md)
- [Apply GitLab paid license](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/index.md#use-gitlab-enterprise-features)
- [Toggle feature flags](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/preview_gitlab_changes.md#enable-or-disable-gitlab-feature-flags)
- [More how-to topics for GDK](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/howto/index.md)

### Review Apps

- [Use Review Apps in MRs](https://docs.gitlab.com/ci/review_apps/#how-review-apps-work)
- [Log into Review Apps](https://docs.gitlab.com/development/testing_guide/review_apps/#log-into-my-review-app)
- [Prevent auto-stopping](https://docs.gitlab.com/development/testing_guide/review_apps/#auto-stopping-of-review-apps)
- [📺 Toggle feature flags](https://www.youtube.com/watch?v=VBo667LiwBQ). You can enable feature flags using tools like `curl` or [Postman](https://www.postman.com)..

## Help

If you get stuck:

1. If using GDK (locally or in Gitpod), try to [troubleshoot it yourself](https://gitlab.com/gitlab-org/gitlab-development-kit/-/blob/main/doc/troubleshooting.md) first.
   Then, don't hesitate to reach out for help (see below).
1. **Gitpod help**
    1. Ask in the `#gitpod-gdk` Slack channel.
    1. Contact: [Marcel van Remmerden](/handbook/company/team/#mvanremmerden)
1. **GDK help**
    1. See [getting help](https://gitlab.com/gitlab-org/gitlab-development-kit#getting-help).
    1. Ask in the `#gdk` Slack channel.
    1. Contact: [Taurie Davis](/handbook/company/team/#tauriedavis), [Sunjung Park](/handbook/company/team/#sunjungp)
