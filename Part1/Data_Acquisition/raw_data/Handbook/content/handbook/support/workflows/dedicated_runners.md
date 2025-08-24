---
title: Hosted runners for GitLab Dedicated
category: GitLab Dedicated
description: "GitLab Dedicated Support - Hosted Runners"
---
## Hosted runners

[Hosted Runners for GitLab Dedicated](https://docs.gitlab.com/administration/dedicated/hosted_runners/) is a product first offered to GitLab Dedicated customers
for beta testing in Q4 FY25, with a general availability target of Q2 FY26.

## Who is using Hosted Runners?

To identify if a customer is using Hosted Runners, use Switchboard.

1. Log in to Switchboard -- all Support Engineers can [access Switchboard](dedicated_switchboard.md#accessing-switchboard)
1. Click **Manage** next to the tenant that you're interested in
1. Look for **Hosted runners** at the top (If you do not see **Hosted runners**, that tenant isn't using Hosted runners for GitLab Dedicated)

## Viewing Logs

`gitlab-runner` and `systemd` logs are available in OpenSearch
alongside the [GitLab Dedicated application logs](dedicated_logs.html).

To view on Runner-related logs only:

1. Filter generally with `fluentd_tag:cloudwatch.*`
2. Obtain the more exact `fluentd_tag:cloudwatch.<name>-fleeting-logs`,
   from the `_source` column of initial results, and apply it.
   The `<name>` is a customer-specific value (attribute of **CommonProperties** on
   [Runner Model](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/runner-model-schema/)),
   but is not yet available in Switchboard.
3. Using that same prefix based on `cloudwatch.<name>` `manager-logs` are available as well.

For job logs reach out to the customer.

## Monitoring

Monitoring Hosted Runners is done in Grafana. Details on how to access Grafana are available in [GitLab Dedicated Observability and Monitoring (Grafana)](dedicated_instance_health).

Once in Grafana, go to **Dashboards** and search the **Hosted Runner(s) Overview** dashboard. This dashboard has plots on different runner metrics.
The dashboard is available for all tenants but is only populated if Hosted Runners are being used by the customer.

## Architecture

GitLab Hosted Runners are created on `ec2` AWS instances.

## Useful References

- [Dedicated team Hosted Runner Model](https://gitlab.com/gitlab-com/gl-infra/gitlab-dedicated/runner-model-schema/-/blob/main/docs/model-examples.md)
- [Dedicated team Hosted Runner technical document](https://gitlab-com.gitlab.io/gl-infra/gitlab-dedicated/team/engineering/projects/dedicated_hosted_runners/index.html)
