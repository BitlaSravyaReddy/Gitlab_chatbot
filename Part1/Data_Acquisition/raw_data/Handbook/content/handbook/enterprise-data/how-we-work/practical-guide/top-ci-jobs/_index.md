---
title: "CI Jobs You Should Know About on Any MR"
description: "This handbook page will help you understand what CI jobs you need to know when getting started with using dbt in the GitLab web IDE."
---
## What is a CI Job (and Why Should You Care?)

Here is a complete list of all of our CI jobs at GitLab https://handbook.gitlab.com/handbook/enterprise-data/platform/ci-jobs/ . This section is a work in progress.

The two main jobs you will need to know when working in MRs is the Build Changes job, and the Grant Clones job. These will be used in almost every MR you submit!

### Build Changes

To understand the build changes job, you need to understand what happens when you submit a merge request (MR). At GitLab, because we use our own product and have built out a suite of helpful CI/CD jobs in our pipelines, every time you submit an MR a 'new' database is created with your changes.

Initially, all that happens is that the code is copied over, and a blank database is created. The pipeline will scan your code for vulnerabilities, but it will not actually create any tables. However, you have the ability to ask GitLab to create a new merge request database - which specifically contains the code changes you are looking to merge.

For example, if you switch up the code in a table to add a new column and change how "Revenue" is calculated, you will likely want to test that code to make sure it is working as expected. You can do this in SQL, but what if you are changing a series of tables and they all rely on the changes to one another to test the new changes?

In your merge request database, GitLab can build the changes to every table which you have changed in your merge request (because you can make changes to more than one table at once), and any tables in between those tables. A "build" essentially means running the full query of the entire table and populating it with the full dataset.

Let's say you make a change to `mart_charges`, and `rpt_charges_weekly`. But in between those two tables is the table `mart_charges_weekly`. The MR database will copy what is in production upstream of `mart_charges`, and then it will build all three `'mart_charges`, `mart_charges_weekly`, and `rpt_charges_weekly` with your new changes - for example the new column you added, and the change to how revenue is calculated that you made in `mart_charges`.

In order to trigger this "build" action, you can use the pipeline which is accessible right from the MR. Look for the pipeline (the following picture) and find the "Build Changes" job. All you need to do here is click the play button, and wait. It will then build the changes in the MR database to all of the tables which you have made changes to in your MR.

![Build Changes](/images/handbook/enterprise-data/platform/tableau/build-changes.png)

### Grant Clones

Once you have built your changes, this means that there is a new database which you can access that contains the MR's data which you have just created. Any code changes you have made are reflected, and any table which you have made changes to are available to query!

In order to access this, however, you need to grant yourself clones. If the table already exists (it is not a new table), then you can do this in the MR. You will find your pipeline, and use the "Grant Clones" job in the first step.
Unlike when you "build changes", you cannot just press the play button to the right of the name of the job. Instead, click on the green check mark that is the first in the line, and it will open all of the available jobs at that step. Look for "Grant Clones" and click on the text (not the play button).

![Grant Clones](/images/handbook/enterprise-data/platform/tableau/grant-clones.png)

This will bring you to a screen where you can easily add your key/value pair - which is how you tell the pipeline that you want it to grant _you_ access to the MR database. Here you use `GRANT_TO_ROLE` as the key. The value is your Snowflake role name, which is often your email. So if your name is John Smith, and your role is JSMITH, then you would put `JSMITH` as your value. You can grant access to yourself, or to others. You can only grant one clone at a time, even though there is the option to add more than one in the interface.

![Grant Clones](/images/handbook/enterprise-data/platform/tableau/grant-clones1.png)

Once this finishes running, you can find the name of the branch you created for your MR in the list of databases which you have access to in Snowflake, and Tableau! This lets you test the impacts of your code changes.

#### Granting Clones to Net New Tables

If you are creating a net new table which has not existed yet, you will need to ask the Data Engineers to grant you access to the database/table. You can ask for permission for yourself and others, and you can ask for access to more than one table at once.

You need to specify the branch name, database, schema, and table. Most of the time you will be asking for access to tables in the PROD schema, so the general syntax is: `“branch_name_prod”.schema.table`

Here is an example message that you could copy and paste in the #data-engineering Slack channel to ask for access to your table. If it is your first time and you are nervous to get it wrong, feel free to let them know in the message you are new and might make a mistake.

```text
Hello @data-engineers, could you grant JSMITH and JDOE access to:

"2-create-report-tables-for-pushed-sql_PROD".restricted_safe_common_mart_sales.rpt_pushed_pipe_starting_fourth_day
"2-create-report-tables-for-pushed-sql_PROD".restricted_safe_common_mart_sales.rpt_pushed_pipe_starting_scaffold
"2-create-report-tables-for-pushed-sql_PROD".restricted_safe_common_mart_sales.rpt_pushed_pipe_starting_daily

```

_Note_: Before you ask the data engineers for access to your table, make sure you build the changes to your pipeline, and the build succeeds. If you have not yet built the changes (sucessfully), they will respond and tell you that they tried to grant you access, but that schema was empty. They won't be able to grant you access to the table until it exists (which happens when it builds successfully).

### Custom Build Changes

Sometimes you may want to test MR changes that are not included in the scope of what gets built when you "Build Changes". This is most common when you make an adjustment to columns in an upstream table (such as a mart or prep table), but you actually want to test the impacts to those changes on your downstream report table.

If the report table does not have any changes involved in it, the MR database will not "build" that table, and you will not be able to query and test that table, by default. However, there is a way around this! You can set custom variables to your build changes job, or even use a similar job - custom invocation- to build your changes.

The easiest way to figure out how to do this is to use GitLab Duo. If you work for GitLab, GitLab Duo is available to you automatically when you are working in the GitLab WebIDE.

What you can do is go to [this page](/handbook/enterprise-data/platform/ci-jobs/#build_changes) of the handbook and copy the entire "Build Changes" and "Custom Invocation" sections. Then go back to your merge request, and open up GitLab Duo. Paste the entire contents of these jobs into the chat, hold shift and press enter to go to a new line, and write your prompt.

You can say, for example, "I have made a change to prod.restricted_safe_common_mart_sales.mart_crm_opportunity in my MR. However, I want to test the impact that this would have on a table downstream - it is called prod.restricted_safe_common_mart_sales.rpt_new_charges. The normal build changes job did not build this table, because it is downstream and not involved in the MR directly. I want to build the mart table, and then also one table in between and then just my report table. How can I get this table to build?"

It will likely instruct you to go into the Build Changes job - so instead of clicking the play button as you did before, you click the actual text/ whitespace of the job, to the left of the play button. If you have not yet built your changes the screen for the custom variables will appear at this point, and you can input KEY: `SELECTION` ; VARIABLE: `+prod.restricted_safe_common_mart_sales.mart_crm_opportunity+prod.restricted_safe_common_mart_sales.rpt_new_charges`.

If you have already run the build changes job, when you click on the build changes job in the pipeline, it will bring you to a page with a black box with colorful test detailing the job it has already run. You can specify your custom instructions by looking in the top right corner of the page, and finding the blue "reset" button. Click that, and select "Update CI/CD variables".

![Build Again](/images/handbook/enterprise-data/platform/tableau/build-again.png)
