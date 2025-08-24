---
title: Localization Engineering
description: Technical details of GitLab's localization infrastructure and engineering processes.
---

Technical overview of GitLab's localization infrastructure and engineering processes across documentation and product interfaces. Includes translation environments, branch management, development workflows, and preview systems for internationalized content.

## Iteration Process

We start our iteration on a Tuesday. We release throughout the iteration. Iterations are 2 weeks long. 

See our [Localization engineering iterations here](https://gitlab.com/groups/gitlab-com/localization/-/cadences/).

### Labels and Workflow Boards

We use issue boards to track issue progress throughout an iteration. Issue boards should be viewed at the highest group level for visibility into all nested projects in a group.

The Localization team uses the following issue labels for distinguishing which part of the org the work belongs to and distinguishing between specialities:

| Organization          | Title       |
| ----------    | -----------|
| [Documentation - docs.gitlab.com](https://gitlab.com/gitlab-com/localization/docs-site-localization/-/issues/?sort=created_date&state=opened&label_name%5B%5D=L10n-docs&first_page_size=100) | `~"L10n-docs"`     |
| [Marketing - about.gitlab.com](https://gitlab.com/dashboard/issues?sort=created_date&state=opened&label_name[]=L10n-mktg) | `~"L10n-mktg"`     |
| [Localization engineering work](https://gitlab.com/gitlab-com/localization/docs-site-localization/-/issues?label_name=L10n%3A%3Aengineering) | `~"l10n::engineering"` |

The Localization team uses the following scope labels to categorize documentation engineering work.

| What & Current Issues          | Title       |
| ----------    | -----------|
| [Documentation engineering work to be triaged](https://gitlab.com/gitlab-com/localization/docs-site-localization/-/issues/?sort=created_date&state=opened&label_name%5B%5D=L10n-docs-engineering%3A%3Atriage&first_page_size=100)| `~"l10n-docs-engineering::triage"`   |
| [Documentation engineering work required for launch](https://gitlab.com/gitlab-com/localization/docs-site-localization/-/issues/?sort=created_date&state=opened&label_name%5B%5D=L10n-docs-engineering%3A%3Alaunch-required&first_page_size=100)| `~"l10n-docs-engineering::launch-required"` |
| [Documentation engineering work post launch](https://gitlab.com/gitlab-com/localization/docs-site-localization/-/issues/?sort=relative_position&state=opened&label_name%5B%5D=L10n-docs-engineering%3A%3Apost-launch&first_page_size=100)| `~"l10n-docs-engineering::post-launch"`  |

#### Iteration Board #9140637 

Board: https://gitlab.com/groups/gitlab-com/localization/-/boards/9140637

Displays all issues with ~"L10n::engineering" label assigned to current [Localization engineering iterations](https://gitlab.com/groups/gitlab-com/localization/-/cadences/)  

#### Docs Engineering (Stream) Boards #7828627

Board: https://gitlab.com/groups/gitlab-com/localization/-/boards/7828627

Tracks all documentation-related engineering tasks in the Localization project. This board displays all issues with both ~"L10n-docs" and ~"L10n::engineering" labels.

## Internationalized Documentation - docs.gitlab.com

The GitLab docs site is beeing enabled for internationalization, with initial support for Japanese translations.
https://docs.gitlab.com/ja-jp/

### Translation content sources

Translated content for https://docs.gitlab.com is pulled from separate `/doc-locale/` directories in the following repositories:

* [GitLab](https://gitlab.com/gitlab-org/gitlab/-/tree/master/doc-locale/) 
* [Operator](https://gitlab.com/gitlab-org/cloud-native/gitlab-operator/) 
* [Omnibus](https://gitlab.com/gitlab-org/omnibus-gitlab/-/tree/master/doc-locale/)  
* Runner  
* [Charts](https://gitlab.com/gitlab-org/charts/gitlab/-/tree/master/doc-locale/)

### Translation environments

We maintain two separate environments that contain all projects used to compile docs.gitlab.com. These contain forks of the upstream projects.

**Production environment**: [localization/tech-docs-forked-projects/prod/](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/prod/)

**Test environment**: [localization/tech-docs-forked-projects/test/](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/)

### Branch structure

#### Overview

Each project within these environments maintains the following branch structure:

1. **main** Used exclusively for pulling upstream changes into our fork. Do not contribute to this branch.
2. **main-translation** Used for delivering translations from our Translation Management System (TMS). Do not contribute to this branch.
3. **main-development** This is our development workspace for i18n features.
4. **live-preview** A stable live preview branch for the internationalized GitLab documentation. [See MR for more details](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs/-/merge_requests/17).

#### Branch maintenance

##### How to Update Localization Forks with Upstream Changes**

###### Steps

1. **Update the fork's main branch**  
   * Update your fork's default branch (`main` or `master`) to match the production project's default branch
   * Use the "Update Fork" button in the UI
2. **Create a merge request (MR)**
   * Create an MR that merges the default branch to `main-translation`
   * This MR will contain all documentation changes since the last update
3. **Review changed files**
   * **Pipelines**: If pipelines fail, this is typically due to upstream configuration issues
     * In most cases, you can force the merge and ignore pipeline issues
     * Attempting to fix these issues often consumes engineering resources unnecessarily
   * **Merge conflicts**: Review these case by case
     * May need to be relayed to the localization team
     * Conflicts occur because of upstream changes
     * Ignoring conflicts on target files will cause future translations to overwrite upstream changes
4. **Merge the MR to `main-translation`**
   * This updates the translation branch with the default branch
   * Triggers Argo-GitLab integration to check for source language file updates

[See example MR](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/prod/omnibus-gitlab/-/merge_requests/11) for updating the `main-translation` branch with content from the Omnibus Production fork.

### i18n Development Environments

#### Main Development Branch

The `main-development` branch is our dedicated environment for i18n feature development. It builds localized routes and enables review apps using translations from production forks' `main-translation` branches.
This [merge request](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs/-/merge_requests/27) documents the changes to enable i18n feature development. 

##### Working with the i18n environment

1. Always create feature branches from `main-development`
2. Target merge requests to `main-development`
3. Test with translations from all projects' `main-translation` branches
4. After approval, open a separate MR to contribute upstream

It is helpful to set up a dedicated directory on your machine for this environment, since it also requires external projects from our production fork, specically the  `main-translation` branch. 

```plain
cd htdocs
mkdir main-devevelopment
git clone git@gitlab.com:gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs.git
cd gitlab-docs
mise trust
make setup
USE_SSH=true make clone-docs-projects
```

Your resulting directory structure should look like this:

```plain
main-development
├── charts-gitlab/ (main-translation)
├── gitlab/ (main-translation)
├── gitlab-docs/ (main-development)
├── gitlab-runner/ (main-translation)
├── gitlab-operator/ (main-translation)
└── omnibus-gitlab/ (main-translation)
```

Refer to documentation here for setting up your workstation further: https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs/-/blob/main/doc/setup.md?ref_type=heads#set-up-your-workstation 

##### Updating `main-development`

* Use the "Update fork" button at [our forked repository](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs/-/tree/main-development)  
* If conflicts occur, update locally:

```plain
cd /htdocs/localization/main-development/gitlab-docs ## cd into your gitlab-docs directory using the main-development branch
git fetch
git checkout main-development
git merge origin/main
git push origin main-development 
```

#### Review App

The review app enables our team to review internationalized documentation and features before production deployment. It consolidates translated content from all five repositories (GitLab, Operator, Omnibus, Runner, Charts), maintains production-identical build pipelines, and utilizes the i18n features built for Hugo.

While the latest `main-development` branch contents are visible, it won't automatically update when there are changes to the `main-translation` forks. Run a new pipeline to pull those in.

First visit https://gitlab-docs-hugo-19c275.gitlab.io/ to oauth yourself to the server, then visit https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ to see the latest `main-development` branch contents.

| Repository | Live Preview URL |
| ----- | ----- |
| GitLab | [https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/ci/yaml/](https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/ci/yaml/) |
| Operator | [https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/operator/backup\_and\_restore/](https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/operator/backup_and_restore/) |
| Omnibus | [https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/omnibus/build/build\_docker\_image/](https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/omnibus/build/build_docker_image/) |
| Runner | [https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/runner/register/](https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/runner/register/) |
| Charts | [https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/charts/installation/](https://gitlab-docs-hugo-19c275.gitlab.io/review-mr-27/ja-jp/charts/installation/) |

This implementation follows the architecture detailed in [tech-docs-forked-projects/test/gitlab-docs/-/merge_requests/27](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs/-/merge_requests/27).

##### How to build a quick Review app for a product documentation Translation MR

Building a review app means pointing the Hugo application to the correct branch which contains those changes. 
Here's a step by step process on how you can achieve this:

1. Go into [main-development products.yaml](https://gitlab.com/gitlab-com/localization/tech-docs-forked-projects/test/gitlab-docs/-/blob/main-development/data/products.yaml)
2. Find the project and edit the `default_branch` field to match the Translation MR’s branch
3. Save the edits to a new branch and create a new MR titled “Draft: Review of <Translation MR Name>”
4. Update MR’s description to specify what the MR is for and why. Link any related issues, merge requests, or external resources such as an Argo request URL
5. Add a list of URLs to check in the review app
6. Once the pipeline completes, you can access the review app through the "View App" button

## Localization engineering by partnership with Spartan Software

The Localization team partners with [Spartan Software, Inc.](https://gitlab.com/gitlab-com/localization/localization-team/-/issues/41) to develop and maintain the [localization request management system](https://gitlab.com/groups/gitlab-com/localization/-/epics/35) and a suite of microserices and integrations. Spartan Software engineers and architects provide specialized expertise in language technology platforms and integrations.

The suite of various integrations, components and microservcies is referred to by the overarching term of **Argo**. See high level architecture [here](https://gitlab.com/groups/gitlab-com/localization/-/epics/35#note_1963781412), and the GitLab-specific architecture [here](https://gitlab.com/groups/gitlab-com/localization/-/epics/35#note_2526391642).

### Engineering labels and workflow related to Argo

We use the following scoped labels to track Argo engineering work performed by Spartan Software:

| Label | Purpose | Usage |
| ------ | ------------ | ------ |
| `Argo-Engineering` | Core Argo enhancements requiring engineering work from Spartan Software | Applied to all Argo development work |
| `Argo-Engineering::Complete` | Enhancement completed and deployed to production | Applied when Spartan delivers finished work |
| `Argo-Engineering::In Progress` | Active development work being performed by Spartan | Applied when development starts on an enhancement |
| `Argo-Engineering::Ready for Deployment` | Development complete, enhancement ready for review and deployment | Applied when Spartan completes development and testing |

### Argo system components

Argo serves as GitLab's centralized localization technology and management infrastructure, encompassing:

* **Request Management System**: centralized intake and tracking of localization requests across all GitLab content types, both manual or automatic via integrations
* **Translation Management System integrations**: automated connections between GitLab systems and commercial TMS platforms (Phrase, TranslationOS, Contentful, etc.)
* **[Argo GitLab Agent](https://gitlab.com/gitlab-com/localization/argo-gitlab-agent)**: a purpose-built microservice / component of the Argo ecosystenm for specialized localization-related tasks, such as translatable file pre- / post-processing, etc.
* **[Argo-GitLab Integration](https://gitlab.com/gitlab-com/localization/argo-gitlab-integration) aka [GitLab Translation Service](/handbook/engineering/architecture/design-documents/gitlab_translation_service/)**: direct integrations with GitLab projects, merge request workflows, and CI/CD pipelines

### Argo engineering board

The [Argo Development board](https://gitlab.com/groups/gitlab-com/localization/-/boards/9354744?label_name[]=Argo-Engineering) board displays all issues with `Argo-Engineering` labels and provides visibility into:

* Current development work in progress by Spartan Software
* Completed enhancements ready for deployment via relevant [milestones](https://gitlab.com/groups/gitlab-com/localization/-/milestones)
* Planned Argo system improvements and integrations

### Communication channels

`#spartan-software`: Direct Slack communication channel with Spartan Software engineering team

Technical coordination occurs through GitLab issues tagged with appropriate Argo-Engineering labels

This partnership enables the Localization team to maintain sophisticated translation infrastructure while focusing internal engineering team on core localizability, feature development and enhancements for marketing website, GitLab product documentation, and GitLab product.
