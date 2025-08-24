---

title: Customer Success Plans
description: >-
  Customer Success Plans bridge pre-sales and post-sales activities by documenting technical evaluation criteria, implementation roadmaps, and success metrics. These plans serve as the foundation for customer engagements, ensuring alignment between GitLab and customer objectives while providing clear documentation that guides both evaluation and implementation phases.
---

**Important Note:** This page represents an initial step in reorganisation of the SA Handbook to make it easier to use; as such, this page talks about Customer Success Plans from a data perspective. It should be noted that there is [another page focussing on Customer Success Plans from a content and planning perspective](/handbook/solutions-architects/sa-practices/customer-success-plan).

## Overview

A Customer Success Plan (CSP) documents the expected value and plan to realize that value for a GitLab customer.  It is generated from our centralized account planning dataset (plan.yaml) and includes customer context, technical requirements, success criteria, and implementation roadmap. This plan starts during pre-sales and serves multiple key purposes:

1. For the **Customer**: Provides a prescriptive, phased approach to achieve business objectives via the adoption of GitLab, including architecture recommendations, deployment strategy, migration plans, integration approach, and user onboarding at scale.

2. For the **Customer Success Team**: Creates a foundation for the post-sales relationship by documenting value objectives, success criteria, and milestones for the next 30, 60, 90 days and beyond.

3. For the **Professional Services Team**: Delivers context for scoping Statements of Work (SOW) based on outlined initiatives.

4. For the **Go-To-Market Team**: Serves as a source of truth when executives or customer support needs context about customer objectives, interactions and plans.

## When is a Success Plan required

A Customer Success Plan should be initiated when:

1. An opportunity has completed Stage-3 Technical Evaluation with a technical win
2. First Order opportunities for accounts with LAM over $2M in Proposal stage (Stage-4) and beyond
3. All New or Growth Opportunities over $300k net ARR, in Proposal stage (Stage-4) and beyond
4. All existing customers with upcoming Renewals, over $300k in ARR basis

*Note: SA Managers have discretion for additional opportunities to be included or excluded.*

## Best practices to create and present the Success Plan

1. **End of Scoping Stage**: The CSP is created and captures information from the discovery (tech stack, current architecture diagram) and the main business objectives. 
2. **Technical Evaluation Stage**: The activity plan lists the actions that will validate how GitLab responds to the key business objectives (demo, POC, etc.). The activity plan is updated over the course of the evaluation. 
3. **Technical Evaluation ends and move to Negotiating stage**: The CSP is presented to the customer to confirm the action plan for achieving each objective, the proposed activities post-acquisition (migration, implementation, enablements, etc.). This can be used as a handover to the post-sales teams and introduce the roles of the CSM/CSE, renewal, PS, and support departments.   

## Documentation Structure

The SA organization maintains a standard schema for Customer Success Plans to ensure consistency and completeness. The schema can be found in the [AccountPlan.schema.json](https://gitlab.com/gl-demo-ultimate-ryappleby/technical-close-plans/generators/-/blob/main/plan-schemas/accountPlan.schema.json) file, which details all required and optional fields along with their descriptions.

## Tracking in Salesforce

The following fields must be maintained in Salesforce:

1. **Customer Success Plan**: URL to the plan
2. **CSM Ready**: Checked when plan is ready for CSM review
3. **Customer Accepted**: Checked after customer review and approval

## Transition to Post-Sales

At the point of sale, the CSP transitions into post-sales execution. This transition varies based on the customer type:

### New Customer Transition

1. CSP is converted into a Mutual Success Plan (MSP)
2. MSP is implemented as GitLab Issues and Epics in a customer-facing GitLab project
3. Ownership transfers to the assigned Customer Success team member:
   - Customer Success Manager (CSM)
   - Customer Success Architect (CSA)
   - Customer Success Engineer (CSE)

### Existing Customer Growth

1. CSP content is evaluated against existing MSP
2. Relevant elements are merged into the existing MSP structure
3. New Epics/Issues are created to track additional objectives
4. Existing Customer Success team maintains ownership

### Implementation Details

The CSP content is transformed into actionable GitLab items:

- Success criteria become Epic success metrics
- Technical requirements translate to specific Issues
- Timeline milestones become Epic due dates
- Implementation phases are organized as Epic groups
- Customer stakeholders are added as project members

For details about post-sales plan management and CSM responsibilities, see the [CSM Success Plans documentation](/handbook/customer-success/csm/success-plans/).

## Resources

- [Mutual Customer Success Plan Information](https://gitlab.com/gitlab-sales-continuous-planning/gitlab-profile/-/blob/main/README.md)
- [Account Planning Data Schema](https://gitlab.com/gl-demo-ultimate-ryappleby/technical-close-plans/generators/-/blob/main/plan-schemas/accountPlan.schema.json)
- [Example Success Plans](https://gitlab.com/gl-demo-ultimate-ryappleby/customer-collab/customers)
