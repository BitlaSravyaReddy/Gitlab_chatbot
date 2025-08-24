---
title: "Backups of GitLab.com"
description: "This policy specifies requirements for backups of GitLab.com"
controlled_document: true
---

## Purpose

This policy outlines how GitLab performs, monitors, and validates backups and restorations of GitLab.com.
These procedures are critical for ensuring data recovery and disaster recovery for customer data.

## Scope

GitLab.com's backup strategy includes both monitoring and restore validation.

Customer data is stored in the following locations:

1. All PostgreSQL databases for GitLab.com
1. Object storage for GitLab.com, including packages, LFS, uploads, and CI data
1. The CustomersDot database, which manages subscriptions and purchases
1. Git repositories

## Not in Scope

1. Customer Data stored in the Redis cache
   1. Data queued for processing
   1. Sessions and other cached data

## Roles & Responsibilities

| Role                      | Responsibility                                                                 |
|---------------------------|--------------------------------------------------------------------------------|
| GitLab Team Members       | Ensure adherence to the requirements outlined in this policy                   |
| Engineering (Code Owners) | Approve significant changes and exceptions to this policy                      |

## Procedure

GitLab defines:

- The services requiring backups
- The frequency of backups, data retention periods, and restoration processes
- The procedures for data restoration for Disaster Recovery scenarios

### Backup and Restore

#### PostgreSQL Databases

GitLab.com database backups are taken every 24 hours, with incremental updates every 60 seconds. The data is securely streamed to [GCS](https://cloud.google.com/storage), encrypted, and retained for 90 days. The CustomersDot database is backed up daily with a retention period of 7 days.

All databases are continuously monitored to ensure successful backups, with alerts triggered for missing backups. Restore processes are validated through regular restoration from disk snapshots and replaying WAL segments.

#### Git Repositories

Repositories are backed up hourly using block-level disk snapshots. These snapshots are stored in multi-region object storage and retained for 14 days. All disks are monitored, with alerts triggered for missing snapshots.

Restore validation is conducted by randomly sampling disks and restoring recent snapshots.

#### Object Storage

Data stored in Object Storage (GCS) benefits from Google's [99.999999999% annual durability](https://cloud.google.com/storage/docs/storage-classes#descriptions) and multi-region bucket redundancy. To enhance data protection, [Object Versioning](https://cloud.google.com/storage/docs/object-versioning) and [Soft Delete](https://cloud.google.com/storage/docs/soft-delete) are enabled.

Automated restore validation is not required for Object Storage due to its inherent protections through versioning and soft delete.

### Disaster Recovery

For disaster recovery, backups are validated through periodic restoration exercises called "Game Days" to ensure compliance with recovery time objective (RTO) and recovery point objective (RPO) targets.
GitLab.com is deployed in the `us-east1` region across multiple GCP availability zones.
For short-term outages affecting a single zone within `us-east1`, unaffected zones will scale to restore service.
For the Gitaly service, recovery from backups will be necessary if data loss occurs.

Disaster recovery operations adhere to the [Disaster Recovery runbooks](https://gitlab.com/gitlab-com/runbooks/-/tree/master/docs/disaster-recovery).
These procedures target specific services to allow parallelized recovery efforts.

Mock disaster recovery (DR) events are conducted quarterly to simulate incidents affecting one or more services.
These exercises validate DR processes and readiness for real incidents.

During these [Game Days](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/gameday.md), RTO and RPO targets are validated by [recording measurements for each procedure](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/recovery-measurements.md).

## Exceptions

Exceptions to this policy will be managed in accordance with the [Information Security Policy Exception Management Process](/handbook/security/controlled-document-procedure/#exceptions).

## References

- [Records Retention & Disposal](/handbook/security/standards/records-retention-deletion/)
- [Disaster Recovery runbooks](https://gitlab.com/gitlab-com/runbooks/-/tree/master/docs/disaster-recovery)
- [GameDays](https://gitlab.com/gitlab-com/runbooks/-/blob/master/docs/disaster-recovery/gameday.md)
