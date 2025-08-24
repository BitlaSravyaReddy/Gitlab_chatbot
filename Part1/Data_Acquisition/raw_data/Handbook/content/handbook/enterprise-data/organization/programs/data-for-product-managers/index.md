---
title: "Data For Product Managers"
---

This page is intended to help Product Managers at GitLab understand what data is available to them and how they can use it to understand how their product is used. This page primarily covers two topics: _how_ to consume data, and _what_ data is available.

## How to Consume Data at GitLab

The user-facing end of GitLab's data stack consists of our BI Tool, Tableau, which is connected to our Snowflake data warehouse. The [Tableau handbook page](/handbook/enterprise-data/platform/tableau/) of the Data team handbook has general information about Tableau aimed for a wider GitLab audience.

### Useful links for Product Managers

Here are some useful links that we recommend for you to bookmark:

- [Data Catalog](https://internal.gitlab.com/handbook/enterprise-data/data-governance/data-catalog/): Helpful guides on how to use our data
- [DBT documentation](https://dbt.gitlabdata.com/#!/overview): Data model documentation
- [Service Ping Metrics Dictionary](https://metrics.gitlab.com/): Service Ping metric definitions and metadata
- [Service Ping documentation](https://docs.gitlab.com/ee/development/internal_analytics/service_ping/)
- [Snowplow Event Dictionary](https://metrics.gitlab.com/events/): Snowplow event definitions and metadata
- [Product Data Insights handbook](/handbook/product/groups/product-analysis/): Information about the Product Data Insights team
- [Tableau documentation](/handbook/enterprise-data/platform/tableau/): Information and guides on how to use Tableau
- [Analytics Instrumentation Quick Links](/handbook/product/product-processes/analytics-instrumentation-guide/#quick-links)
- [Quick Start Guide for Internal Event Tracking](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html): Comprehensive instructions on how to instrument event tracking and context around GitLab's internal tracking system.
- [Usage Data Instrumentation Issue Template](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Usage%20Data%20Instrumentation): Issue template for product managers or engineering teams looking to track usage of their features.

### Getting Tableau Access

In order to gain access to Tableau, you will need to follow the instructions [here](/handbook/enterprise-data/platform/tableau/#access) and open an access request.

- To create your own charts and dashboards, you need to have a Creator or Explorer license. You can read more about the Tableau license types [here](/handbook/enterprise-data/platform/tableau/#capabilities).

### Published Data Sources

Published data Tableau sources are great ways to allow Tableau users to build charts without writing any SQL or modeling. The Data team has created several Published Data Sources in Tableau that have the official "Certified" badge.

![Tableau Certified Data Sources](/images/enterprise-data/programs/data-for-product-managers/tableau_certified_data_sources.png)

For example, `Mart Ping Instance` can be used to look at Service Ping ping-level details.

### How do I know what tables are available?

The Data team uses a tool called [dbt](https://www.getdbt.com/) for our data transformation layer. A nice feature of dbt is dbt docs, which automatically creates documentation for all of the models in our schema. Our dbt docs instance can be found [here](https://dbt.gitlabdata.com/#!/overview).

- Tableau will show a list of all tables available for querying when you form a connection to Snowflake in the Data Source pane.
  - ![Display of tables in Tableau Data Source pane](/images/enterprise-data/programs/data-for-product-managers/tableau_list_of_tables.png)
- Each data source has a distinct naming convention for tables (see more about [Key Data Sources below](#key-data-sources-for-product-managers-at-gitlab)).
  - Service Ping models contain `ping_instance` in the name (ex: `dim_ping_instance`, `mart_ping_instance_metric_monthly`)
  - GitLab.com Postgres db event models start with `fct_event` or `mart_event` (ex: `fct_event_user_daily`, `mart_event_namespace_monthly`)
  - GitLab.com Postgres db table replicas are named after the source table/content (ex: `dim_merge_request`, `dim_namespace`)
  - Snowplow models contain `behavior` in the name (ex: `mart_behavior_structured_event`, `fct_behavior_website_page_view`)

#### How can I update or add more information to the dbt docs?

You will need to locate the file you wish to update or create in the [gitlab-data analytics project](https://gitlab.com/gitlab-data/analytics). Please be sure to read and follow the [SQL style guide](/handbook/enterprise-data/platform/sql-style-guide/) when creating the changes. If you wish to update only the descriptions or information about tables you will be looking for a `schema.yml` file. If you wish to actually change the structure of tables it will be a `*.sql` file.

Next, create a branch and then submit an MR using the `dbt Model Changes` template to the [gitlab-data analytics project](https://gitlab.com/gitlab-data/analytics). When creating your branch and MR please follow the [Data team workflow](/handbook/enterprise-data/how-we-work/#merge-request-workflow) and use the appropriate [Data team labels](/handbook/enterprise-data/how-we-work/#issue-labeling).

### How can I get help?

If you ever get stuck or have a question, please ask for help in the [#data slack channel](https://gitlab.enterprise.slack.com/archives/C8D1LGC23). It is recommended to also cross-post questions in your #g_, #s_, or #product channels because many PMs have data related expertise and can provide you quick assistance for common product data questions.

- Remember, it's helpful for us to know the context behind your question. Don't just say _what_ you want to know but also _why_ so others can point you to a more efficient way to get your answer.
- This document is meant to serve as a guide of best practices. Please add what you learn when you need help with this content.

If needed, you may create an issue in the [Product Data Insights project](https://gitlab.com/gitlab-data/product-analytics/-/issues/new) and assign it to a [product data analyst](/handbook/product/groups/product-analysis/#team-members). You can read more about working with the PDI team [here](/handbook/product/groups/product-analysis/#working-with-us).

## Guidance for Instrumenting Feature Tracking

As a GitLab PM, you're responsible for defining and tracking metrics for your team's features. This guide will walk you through the process, tools, and resources available to help you succeed.

### Quick links for Instrumenting Feature Tracking

- [CLI generator to automatically create event and metric definition files](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html#defining-event-and-metrics): An interactive CLI that gathers your requirements, automatically generates event and metric definition files, and produces ready-to-use instrumentation code for engineers to implement and test
- [Quick Start Guide for Internal Event Tracking](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html): Comprehensive instructions on how to instrument event tracking and context around GitLab's internal tracking system
- [Getting Started Standard Context Fields](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/standard_context_fields.html): Documentation on each standard context field included in Internal Event Tracking and descriptions of their intent
- [Usage Data Instrumentation Issue Template](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Usage%20Data%20Instrumentation): Issue template for product managers or engineering teams looking to track usage of their features
- [Product Data Insights Performance Indicator Chart Issue Template](https://gitlab.com/gitlab-data/product-analytics/-/issues/new?issuable_template=PI%2520Chart%2520Help)
- [Product Data Insights Ad Hoc Analysis Issue Template](https://gitlab.com/gitlab-data/product-analytics/-/issues/new?issuable_template=Ad%2520Hoc%2520Request)

### Self-Service Feature Tracking Dashboards

If your analytics needs for your new or recently modified feature are met by these dashboards, you can skip creating a Product Data Insights (PDI) Issue:

- [PD: Centralized Product Usage Metrics](https://10az.online.tableau.com/#/site/gitlab/views/DRAFTCentralizedGMAUDashboard/MetricReporting)
- [PD: Product Usage Metrics (.com & Service Ping)](https://10az.online.tableau.com/#/site/gitlab/workbooks/2478263/views)
- [PD: Firmographic Product Metric Usage](https://10az.online.tableau.com/#/site/gitlab/workbooks/2137023/views)
- [PD: Subscription Feature Usage Trends](https://10az.online.tableau.com/t/gitlab/views/PDSubscriptionFeatureUsageTrends_17032798065680/ActiveSubscriptionUsageTrends)
- [AI Gateway Reporting](https://10az.online.tableau.com/t/gitlab/views/AIGatewayReporting/Overview)

### Process for Instrumenting Feature Tracking

1. Plan Your Analytics Requirements

   **Owner: Product Manager**
   - Start by determining what you need to measure:
     - What user behaviors indicate feature success?
     - What metrics will help you make product decisions?
     - What data points do you need for your team's KPIs?
   - If existing dashboards don't meet all of your needs, create a Product Data Insights (PDI) Issue to request additional analytics. [Product Data Insights (PDI) Issue](https://gitlab.com/gitlab-data/product-analytics/-/issues/new)

1. Create Instrumentation Issue

   **Owner: Product Manager**

   Option A: Use the CLI Generator to generate requirements for your Instrumentation Issue
   - Use the [CLI generator tool](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html#defining-event-and-metrics)
   - Benefits:
     - Automatically generates event and metric definition files
     - Produces ready-to-use instrumentation code
     - Reduces implementation time for engineers
     - Ensures consistency with GitLab's tracking standards

   Option B: Use Usage Data Instrumentation Issue Template to outline metric requirements
   - Use the [Usage Data Instrumentation Issue Template](https://gitlab.com/gitlab-org/gitlab/-/issues/new?issuable_template=Usage%2520Data%2520Instrumentation)
  
   Tag your [assigned product analyst](/handbook/product/groups/product-analysis/#team-members) to review metric properties

1. Implement Tracking

   **Owner: Engineer**
   - Create an Internal Events Tracking Merge Request (MR)
   - Implement new metrics according to specifications defined in Usage Data Instrumentation Issue 

1. Test and Validate

   **Owner: Engineer**
   - Perform [local testing](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/local_setup_and_debugging.html)
   - Request review from Analytics Instrumentation team member
   - Verify test events match properties defined in the Issue

1. Create Analysis

   **Owner: Product Analyst**
   - For analyses requiring user and event grain GitLab.com data (Snowplow), data collection will be sufficient for analysis 1-2 weeks after MR merge
   - For analyses requiring aggregated SM and Dedicated data (Service Ping), data collection will be sufficient for analysis 6-8 weeks after MR merge due to minimum version adoption requirement for Service Ping metrics
   - Complete requirements specified in PDI Issue (if applicable)

### Special Considerations for AI Gateway Features

When instrumenting features routed through the AI Gateway, follow these guidelines:

1. Represent new features routed through the AI Gateway as unit primitives
   - New distinct features should be represented as a [unit primitive](https://gitlab.com/gitlab-org/cloud-connector/gitlab-cloud-connector/-/tree/main/config/unit_primitives)
   - To add a new unit primitive, reach out to ~"group::cloud connector"

1. Set up tracking for the new unit primitive
   - Contact ~"group::analytics instrumentation" with the necessary fields to be tracked
   - For more information on AI Gateway instrumentation, see the [documentation](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html#internal-events-on-other-systems)
   - Once instrumented, AI Gateway events using the unit primitive framework:
     - Cannot be blocked by users
     - Are tracked at the event grain for all deployment types

1. For more granular reporting
   - If you need more detail than a 'request' of the AI Gateway at the broad feature grain, use [Internal Events Tracking](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html)
   - Internal events can be connected to unit primitive events using a `correlation_id` for behavior funnel or more granular reporting use cases (GitLab.com only)

1. Viewing AI Gateway data
   - [AI Gateway Reporting](https://10az.online.tableau.com/t/gitlab/views/AIGatewayReporting/Overview) automatically displays new unit primitive requests once they have been instrumented by ~"group::analytics instrumentation"
   - Additional analytics can be requested by creating a [Product Data Insights (PDI) Issue](https://gitlab.com/gitlab-data/product-analytics/-/issues/new)

### Key Contacts and Resources

- For questions about the feature tracking process, reach out to #g_monitor_analytics_instrumentation.
- The Analytics Instrumentation team owns our internal product feature tracking system.

By following this process and understanding the roles involved, PMs can effectively instrument and track metrics for their features, enabling data-driven decision-making and product improvement.

## Key Data Sources for Product Managers at GitLab

We have three primary data sources for product usage data:

- **Service Ping** (for Self-Managed, Dedicated, and GitLab.com)
- **GitLab.com Postgres Database** (for GitLab.com)
- **Snowplow** (for GitLab.com and the AI Gateway)

Each data source comes with its own caveats, capabilities, and limitations. The first question we on the Data or PDI teams ask product managers is usually "are you interested in knowing this for Self-Managed or GitLab.com?" Our approach to answering your question and the data source(s) available differ greatly between the two. Although our Self-Managed offering has many more active customers, our GitLab.com offering has much more granular data available to analyze.

### Service Ping (Version App)

[Service Ping](https://docs.gitlab.com/ee/administration/settings/usage_statistics.html) is a custom tool that GitLab built to collect weekly aggregated information from our customers across various deployment options:

- Self-Managed: Customers who host our product on their own hardware.
- GitLab Dedicated: Our fully-managed, single-tenant SaaS offering where each customer gets their own isolated instance of GitLab, hosted and managed by GitLab's team.
- GitLab.com: Our multi-tenant SaaS offering.

#### Key Concepts

- Service Ping collects and reports data at an installation level. For Self-Managed and GitLab Dedicated customers, this means one ping per installation per week. For GitLab.com, which is a single, large-scale installation, Service Ping reporting _still_ occurs as a single ping within our Service Ping framework, representing the entire GitLab.com ecosystem. (In other words, despite the deployment type or installation size, we still receive data at the installation level).
- Service Ping provides pre-aggregated counts of specific events/actions (aka metrics). We are unable to do any analysis at a more granular level (ex: user-level, project-level, etc) since the metrics are already aggregated.
- Sending Service Ping is optional but defaults to being on.
  - You can see the percent of paid subscriptions that successfully send a ping every month on [this chart](https://10az.online.tableau.com/t/gitlab/views/PaidSubscriptionServicePingOpt-InRate/PaidSubscriptionServicePingOpt-InRate). We do not know about the opt-in rate of unlicensed (Core/Free) users but assume the same rate. Here is more [information](https://gitlab.com/gitlab-org/analytics-section/analytics-instrumentation/internal/-/issues/291#note_276741996) on why some installations block data from being sent.
  - Since we do not receive pings from every customer, we apply an estimation in monthly reporting to fill in the gaps. You can read more about the estimation methodology in the internal handbook [here](https://internal.gitlab.com/handbook/enterprise-data/data-governance/data-catalog/xmau-analysis/estimation-xmau-algorithm/).
- Customers must adopt a version of GitLab with a metric instrumented in order to report the metric. For example, if a metric is added in 17.3, only customers on versions >= 17.3 will report the metric. This means that it can take months to have a sufficient number of customers reporting the metric.
  - You can track GitLab version adoption on [this dashboard](https://10az.online.tableau.com/#/site/gitlab/workbooks/2298821/views).
- Pings are added to Snowflake daily. By the 2nd of the month all the data should be available from the previous month.

#### Key Columns

- `ping_deployment_type` is the best column to use in order to differentiate Self-Managed, Dedicated, and GitLab.com usage.
  - If using `ping_delivery_type`, know that both Dedicated and GitLab.com are included in `SaaS`.
- Use the `metrics_path` column to filter to the metric of interest. You can find more metric-level details and metadata in the [Service Ping Metrics Dictionary](https://metrics.gitlab.com/).
- For monthly reporting, we limit to the last ping we receive each month per installation. You can filter your queries to `is_last_ping_of_month = TRUE`
- We often talk about "installations" or refer to the `dim_installation_id` column. An "installation" is the unique combination of `dim_instance_id`/`uuid` and `dim_host_id`.
  - We use "installations" since a single "instance" (`dim_instance_id`/`uuid`) can have multiple hosts.

#### Examples

Here is an example of a query that provides ping-level details, filters out GitLab.com, and limits to the last ping of the month:

{{% details summary="Self-Managed and Dedicated Ping-Level Details"%}}

```sql
SELECT *
FROM common_mart.mart_ping_instance
WHERE ping_created_at >= CURRENT_DATE-30
  AND ping_deployment_type != 'GitLab.com'
  AND is_last_ping_of_month = TRUE
LIMIT 1000
;
```

{{% /details %}}

Here is an example of a query that provides metric-level reporting by month and deployment type:

{{% details summary="Service Ping Metric by Month and Deployment Type"%}}

``` sql
SELECT
  ping_created_date_month,
  ping_deployment_type,
  metrics_path,
  SUM(monthly_metric_value) AS monthly_metric_value,
  COUNT(DISTINCT IFF(monthly_metric_value > 0, dim_installation_id, NULL)) AS installation_count --count of installations reporting usage that month
FROM common_mart.mart_ping_instance_metric_monthly --this model already filters to the last ping of the month
WHERE ping_created_date_month >= '2024-06-01'
  AND metrics_path = 'usage_activity_by_stage_monthly.secure.sast_scans' --arbitrary metric, switch this out for metric of interest
GROUP BY 1,2,3
ORDER BY 1,2
;
```

{{% /details %}}

### GitLab.com Postgres Database

Because GitLab.com is a GitLab instance hosted by GitLab, we have access to the instance's postgres database and can load parts of it into our Snowflake data warehouse. This means we can get a very detailed look into how our product is used on GitLab.com.

- Any part of the product that creates a table on the backend (see the [schema](https://gitlab.com/gitlab-org/gitlab/-/blob/master/db/structure.sql) file) can be added to the ELT job which will sync 3x a day to the warehouse. From there, all we need to do is build a dbt base model to make them accessible in Tableau.

#### What if the table or column I want isn't in the data warehouse?

Our ELT process works by explicitly stating which columns and tables we want to import into the data warehouse. This means we might be missing a column or whole table that you want to have in the data warehouse for analysis. When this is the case, please create a Data issue letting us know what you want us to import using the [New Data Source template](https://gitlab.com/gitlab-data/analytics/-/issues/new?issuable_template=%5BNew%20Request%5D%20New%20Data%20Source). Before doing so, please confirm that the table/column is truly part of the [production schema](https://gitlab.com/gitlab-org/gitlab/-/blob/master/db/structure.sql).

#### Replicating Service Ping using GitLab.com Data

- Because Service Ping only aggregates data at an `installation` level, it is not super useful for GitLab.com since we often want to see information at the `namespace` level. For example, knowing that 40K people used your stage on GitLab.com is somewhat useful, but you'll probably want to know more context (Are they free or paid? What plan are they on? Do I have any power users or is usage equally distributed?)
- But since we have access to the GitLab.com Postgres database, we are capable of replicating many Service Ping metrics at the namespace level or even the user level.
- [This model](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.mart_event_valid) exemplifies how some Service Ping metrics could be replicated for GitLab.com at the namespace level. This model is available as a Published Data Source in Tableau as `Mart Event Valid`.

#### Examples

Here is an example of a query that will generate GitLab.com UMAU by day:

{{% details summary="GitLab.com UMAU by Day"%}}

``` sql
SELECT
  event_date,
  COUNT(DISTINCT dim_user_id) AS umau
FROM common_mart.mart_event_user_daily
WHERE event_date >= CURRENT_DATE-30
  AND is_umau = TRUE
GROUP BY 1
ORDER BY 1
;
```

{{% /details %}}

Here is an example of a query that will generate paid GitLab.com GMAU by month:

{{% details summary="Paid GitLab.com GMAU by Month"%}}

``` sql
SELECT
  event_calendar_month,
  group_name,
  user_count
FROM common_mart_product.rpt_event_xmau_metric_monthly
WHERE event_calendar_month >= '2024-06-01'
  AND is_gmau = TRUE
  AND user_group = 'paid'
ORDER BY 2,1
;
```

{{% /details %}}

### Snowplow

Snowplow Analytics is an open-source enterprise event-level analytics platform that enables data collection from multiple platforms for advanced data analysis.

- We pseudonymize `user_id` on all Snowplow events, meaning that we are unable to connect an event to a specific user (or the GitLab.com Postgres db).
  - We also pseudonymize page URLs to remove any potential PII or RED data.
- Self-Managed and Dedicated installations do not send Snowplow data to GitLab.
  - The one exception is the AI Gateway where we receive events from all deployment types (Self-Managed, Dedicated, and GitLab.com).

#### Key Concepts

- Because Snowplow does not rely on Service Ping, we do not need to wait for a version of GitLab to be adopted to start receiving data. We can collect and visualize data as soon as the instrumentation is deployed.
- Even though the pseudonymization of `user_id` of Snowplow events is a limitation, with the fast feedback, Snowplow is an effective source of data to measure feature adoption and usage.
  - Note: We are still able to count the number of users who engage with a feature, which is sufficient for most use cases. We just do not know who those users are.
- Snowplow events can be blocked by the user.

#### Instrumentation

Analytics Instrumentation has built [Internal Event tracking](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/), which will guide you on how to instrument Snowplow events. To get started, use the [Quick Start Guide to Internal Event Tracking](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/quick_start.html#quick-start-for-internal-event-tracking).

Once your Snowplow events have been instrumented, as part of the validation process, the newly instrumented event should be tested to ensure it is working properly. While you as the PM probably won't be doing the validation yourself every time, it is nice to know how it works. You can learn more about testing Snowplow events in the [Internal Event documentation here](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/local_setup_and_debugging.html).

#### Visualize your events in Tableau

The data you have instrumented is most useful if it can be visualized in a chart. Refer to the [Tableau section](/handbook/enterprise-data/platform/tableau/) of the handbook for information on creating charts.

- First, check if they are correctly stored in Snowflake in the [Snowplow Event Exploration Dashboard](https://10az.online.tableau.com/#/site/gitlab/workbooks/2294309) (note: the data volume is quite large, so please be patient with dashboard load time). You can use the filters to find your events. If you are not sure of the value of the different attributes, they should have been captured in the [event definition](https://docs.gitlab.com/ee/development/internal_analytics/internal_event_instrumentation/event_definition_guide.html). If not, check with your engineering manager.
- Once you have verified that your events are properly stored, you are ready to query and visualize the data! Please be aware that we are collecting several millions of events (page views, structured events) per day, so the whole dataset is quite slow to query. In order to make it easier to explore this data source, we have created several smaller tables:
  - [`common_mart.mart_behavior_structured_event`](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.mart_behavior_structured_event): contains ALL structured events (these are what is instrumented with Internal Event tracking)
  - [`common.fct_behavior_website_page_view`](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.fct_behavior_website_page_view): contains ALL page views
  - [`common.fct_behavior_unstructured_event`](https://dbt.gitlabdata.com/#!/model/model.gitlab_snowflake.fct_behavior_unstructured_event): contains ALL unstructured events (including click events, form submissions, etc)

#### Examples

{{% panel header="**PRO TIP: Optimizing queries**" header-bg="info" %}}

The Snowplow models are quite large and can be slow to query. To make your query faster, use a date (`behavior_at`) filter in your `WHERE` statement.

{{% /panel %}}

Here is an example of a query that will look at the top 100 Snowplow events from the last several days:

{{% details summary="Top 100 Snowplow Events"%}}

``` sql
SELECT
  event_action,
  COUNT(*) AS event_count
FROM common_mart.mart_behavior_structured_event
WHERE behavior_at >= CURRENT_DATE-3
GROUP BY 1
ORDER BY 2 DESC
LIMIT 100
;
```

{{% /details %}}

Here is an example of a query that will look at top 100 pages viewed in the last several days (note how the URLs are pseudonymized):

{{% details summary="Top 100 Pages Viewed"%}}

``` sql
SELECT
  page_url,
  COUNT(*) AS page_view_count
FROM common.fct_behavior_website_page_view
WHERE behavior_at >= CURRENT_DATE-3
GROUP BY 1
ORDER BY 2 DESC
LIMIT 100
;
```

{{% /details %}}

### Other data sources\*\*

- **Zuora**
  - Zuora is our SSOT for subscription information and key metrics like ARR and Seat Count.
- **Customers Dot (CDot) database**
  - CDot is our SSOT for Fulfillment-related data, including trials.
- **Sheetload**
  - You can load your own Google Sheets into the data warehouse. Read more [here](https://internal.gitlab.com/handbook/enterprise-data/platform/pipelines/#sheetload).

## Analytics Instrumentation

[Analytics Instrumentation](https://about.gitlab.com/direction/monitor/analytics-instrumentation/) is part of the product org and is completely separate from the Data and Product Data Insights teams. However, these teams collaborate closely as the Customer Product Adoption pod.

- The Analytics Instrumentation team members are the [DRI](/handbook/people-group/directly-responsible-individuals/)s for data collection across both GitLab.com and Self-Managed. They own Service Ping and Snowplow. They are the ones to go to for questions like:
  - How do I instrument a new metric for Self-Managed?
  - What are the best practices for adding to Service Ping?
  - How can I use Snowplow/Internal Events to track a frontend interaction on GitLab.com?
  - Can I utilize Snowplow/Internal Events to track events on the server-side?
