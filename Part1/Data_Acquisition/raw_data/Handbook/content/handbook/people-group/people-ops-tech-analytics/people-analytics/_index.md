---
title: "People Analytics"
description: "GitLab People Analytics Team Handbook Page"
---

## Overview

People Analytics uses data-driven insights to improve talent decisions and workforce processes at GitLab. We're part of the People Strategy team, helping inform People Group decisions at all organizational levels through reporting, data solutions, and statistical analysis.

## People Analytics Team Members

- [Adrian Perez](/handbook/company/team/#aperez349): [Sr. Manager, People Analytics](/job-families/people-group/people-systems-and-analytics/#senior-manager-people-analytics)
- [Shane McCormack](/handbook/company/team/#mccormack514): [Staff Analyst, People Analytics](/job-families/people-group/people-systems-and-analytics/#staff-analyst-people-analytics)

## What We Do

**Our Mission:** Provide data insights to inform People decisions across GitLab by collecting and analyzing organizational, people, and talent data to improve business outcomes.

**Key Objectives:**

- **Reporting Solutions** - Work with stakeholders to develop automated reporting solutions that deliver relevant People metrics efficently and accurately
- **Data Solutions** - Collaborate with the [Data Team](/handbook/enterprise-data/) to build scalable data models to support reporting and analytics
- **Analytical Solutions** - Apply advanced statistical techniques (clustering, regression, survival analysis) to generate actionable insights and data-informed decisions for People Group and leadership throughout GitLab

## Tools & Resources

### Primary Tools

- **Tableau** - Data visualization, dashboards, and ad-hoc analysis
- **RStudio/R** - Statistical modeling and data cleaning. Learn more in our  [Rstudio handbook page](/handbook/enterprise-data/platform/rstudio/)
- **Snowflake** - Data warehouse and SQL exploration
- **Culture Amp** - Employee surveys and assessments
- **Google Sheets** - Stakeholder-specific solutions when needed

### People Analytics Handbook Contents

- [People Analytics Data Guide](data-guide.md) - Data models and metric definitions
- [People Data Governance](/handbook/people-group/people-ops-tech-analytics/people-analytics/data-governance/) - Data quality and compliance
- [People Analytics Tableau Dashboard Overview](/handbook/people-group/people-ops-tech-analytics/people-analytics/people-tableau/) - Common dashboards and usage
- [People Analytics Survey Support](/handbook/people-group/people-ops-tech-analytics/people-analytics/survey-support/) - Culture Amp survey administration

### External Resources

- [Wharton People Analytics](https://wpa.wharton.upenn.edu/) - Annual conference and research
- [AIHR People Analytics](https://www.aihr.com/blog/people-analytics-resource-library/) - HR and analytics resources
- [HR Predictive Analytics](https://www.koganpage.com/hr-learning-development/predictive-hr-analytics-9781398615656) - Textbook with practical examples
- [Google re:Work](https://rework.withgoogle.com/en/subjects/people-analytics) - Introductory resources
- [Handbook of Regression Modeling in People Analytics](https://peopleanalytics-regression-book.org/index.html) - Keith McNulty's open-source book of regression modeling with examples in R and Python
- [Handbook of Graphs and Networks in People Analytics](https://ona-book.org/index.html) - Keith McNulty's open-source book for Organizational Network Analysis
- [The Fundamentals of People Analytics](https://link.springer.com/content/pdf/10.1007/978-3-031-28674-2.pdf?pdf=button) - Craig Starbuck's open-source book with examples of statistical analyses commonly used by People Analytics teams with examples in R

## Data Governance & Security

GitLab's commitment to transparency and efficiency extends to our data governance framework. The People Analytics team collaborates closely with People and Legal teams to ensure we only access data we are authorized to use. Our process includes access verification and stakeholder approval for all data requests, maintaining strict compliance with applicable laws and regulations.

**Core Governance Principles:**

- **Source System Priority** - People Group daily operations remain in ther source systems to maintain data integrity and workflow efficiency
- **Strategic Data Warehousing** - Our data warehouse, built on technologies like [dbt](/handbook/enterprise-data/platform/dbt-guide/) and [Snowflake](/handbook/enterprise-data/platform/snowflake/) is reserved for "up and out" organizational reporting and analytics
- **Data Minimization** - We only bring in the data needed in reporting and anonymize information whenever possible to protect individual privacy
- **Comprehensive Tracking** - We track data from source system to all downstream systems to understand and mitigate risk throughout the data lifecycle

This governance framework ensures that data remains consistent, reliable, and easy to work with while protecting sensitive information. For detailed information about our data governance processes, see our [Data Governance handbook page](data-governance.md).

## Working With Us

Submit requests and ideas using issue templates in the [People Analytics project](https://gitlab.com/gitlab-com/people-group/people-analytics/general/).
