---
title: How to do a WIR Podcast
category: References
description: General guide for creating a Support Week-in-Review Podcast
---

### Overview

Use this workflow as a general guide when you want to record and publish a Support Week-in-Review Podcast.

Much of this is done in the [Support Week in Review Project](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review).  For more information about the CI/CD jobs used in this guide and what they do, refer to the project [readme](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review/-/blob/main/README.md).

---

### Workflow

1. Check the Support Team Google calendar for the recording session (near the end of the week).
1. Determine who will be responsible for each of the following roles. One person can be responsible for them all.
   - Editor:
      - Before the Recording:
         - Prepare the SSAT input
            - SSAT is gathered into the SSAT issue in the [SWIR project](https://gitlab.com/gitlab-com/support/readiness/support-week-in-review/-/issues).
            - Some SSAT input will have been provided by managers during the week, but most will need to be ingested using the `populate_ssat` job from the pipeline.
            - Run `populate_ssat` job - this will gather any open positive SSAT into the SSAT issue
            - Review the content (automated or other) and make corrections and remove anything that is not actually positive. If there is a lot of content, consider reducing the number down by removing some that are short and not personalised - use your judgement here.  Remove the line about "automated content". 
         - Prepare the digest issue
            - run the `create_digest_issue` job.
            - Edit the digest issue and add a phrase of the week
            - Work with the Metrics Analyst (below) to ensure the metrics section is populated
      - After the recording
         - [Publish](#publishing-the-podcast) the podcast
         - [Prepare SWIR for the next week](#prepare-swir-for-the-next-week)
   - Metrics analyst:
      - take screenshots of the key metrics from the [MM: Support KPIs](https://gitlab.zendesk.com/explore/studio#/dashboards/3DC60497A02C9E0EDB02ECE9C20153733D4AF220B656C550418FF2E42B7E2329) Zendesk dashboard and insert them into the SWIR digest issue. The following 4 items need to be included:
         - From the SWIR tab: the top row of 4 graphs, from SSAT through to volume
         - From the SWIR tab: scroll to the bottom of `Total FRT SLA achievement - Last 4 Weeks` and capture the current week
         - From the SWIR L&R tab: the top row of 4 graphs, from SSAT through to volume
         - From the SWIR L&R tab: scroll to the bottom of `L&R FRT SLA achievement - Last 4 Weeks` and capture the current week
      - in text, enter key metrics into the appropriate sections of the SWIR digest issue
         - you can use the following for formatting

         ``` markdown
         * **SSAT**: 
         * **FRT**: 
            * **High**: 
            * **Normal**: 
            * **Low**: 
         * **NRT**: 
         ```

      - Copy US Gov stats from this [doc](https://docs.google.com/document/d/1ypFHpm3McUNcUVCgZY1aZMlCOIP1jaEQp8oYUO8G36U/edit?tab=t.0#heading=h.7uk6mblh5p2k) from earlier in the week
      - gather pairing data by observing the number of issues against the current [pairing milestone](https://gitlab.com/groups/gitlab-com/support/-/milestones?search_title=pairing&state=&sort=) and compare to the previous week's digest issue data for the week on week (WoW) metric.
      - read and record this section during the recording call.
   - Narrator(s):
      - analyze the content of the section you'll be narrating: click on each link and understand what is being expressed by the point
      - read and record the content of the point
      - by convention, we verbalize issue and MR links by reading out their project name and number, such as "Support Team Meta 1234", or "Handbook MR 4321". You can see these while narrating by hovering over the link. This is particularly important when the item has a "here-link" such as "see **this issue**".
1. Join the Zoom room
1. Determine speaking order for Narrators. A useful set of conventions is:

- Read in alphabetical order by your first initials.
- If you have an item and it comes up, you will read it which will reset the order.

1. When everyone is ready, begin recording. It's easiest for the Editor to "Record locally", as they'll have the audio on their computer for upload.
1. When finished recording, the Editor will [publish](#publishing-the-podcast) and prepare the project for the next week.

#### Publishing the Podcast

Once you have the compiled audio:

1. Optional: add the theme music to the recording if you have it
1. Upload it to the [Support Week in Review - Audio Edition](https://drive.google.com/drive/search?q=Support%20Week%20in%20Review%20-%20Audio%20Edition) folder
1. Change the Sharing Settings to "Anyone within GitLab can View"
1. Copy/paste the URL into the Digest Issue below the TOC (use the format: `:speaker: [Audio edition](url)`)
1. Share the final mix into Slack (there is a slackbot reminder in #support_team-chat at 23:00 UTC on a Thursday - you can share the audio link as a threaded reply to that conversation)

#### Prepare SWIR for the next week

1. Run the `close_week_and_create_new_milestone` job
1. You're done!

#### Notes on SSAT content

The purpose of including SSAT content in the Support Week in Review is two-fold:

1. To highlight behaviors and ways of interaction that customers value in their own voices.
1. To highlight the excellent work on the part of individuals and groups of individuals that take place in ticket interactions.

We do not include every SSAT review every week, both for brevity and because not every SSAT review fulfills the purposes above.

With the above purposes in mind, SSAT comments in the Support Week in Review should:

- be truly positive! Avoid SSAT ratings that disparage other engineers, GitLab teams or are back-handed compliments that include a mix of praise and negative feedback.
- have significant, thoughtful or interesting comments.
- be from a mix of Engineers. Sometimes a particular engineer may have multiple positive reviews in a week: try to get a cross-section of the team included.
- highlight the accomplishments of new team members when possible: a first positive SSAT in the SWIR should be called out and celebrated!
