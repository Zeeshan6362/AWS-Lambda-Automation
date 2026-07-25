# AWS Infrastructure Automation Suite (Lambda & Boto3)

An automated cloud governance and operations suite built using Python 3.12, AWS Lambda, Boto3, Amazon EventBridge, and Amazon SNS. 

This repository contains four completed hands-on serverless automation tasks designed for resource cleanup, backup retention, event-driven tagging, and proactive cost alerting in AWS.

## Reproducible Repository Structure
'''text
AWS-Lambda-Automation/
├── Assignment-1-s3-cleanup/
|   ├── README.md
│   └── lambda_function.py          # Boto3 S3 paginator & deletion logic
├── Assignment-2-EBS-Snapshort/
|   ├── README.md
│   ├── lambda_function.py          # EBS snapshot creation & 30-day retention loop
├── Assignment-3-EC2-AutoTag/
|   ├── README.md
│   ├── lambda_function.py          # Event-driven EC2 auto-tagging script
├── Assignmwnt-4-cost-Alert/
|   ├── README.md
│   └── lambda_function.py          # Cost Explorer MTD query & SNS notification engine
├── screenshots                     
|   ├── README.md                       # Master Documentation
│   └── Screenshot                    
'''

Task 1: Automated S3 Bucket Cleanup
Overview & Objective
Automates the detection and deletion of stale S3 bucket objects older than a specified threshold (e.g., 30 days).

Steps Followed
Paginator Implementation: Utilized boto3.client('s3').get_paginator('list_objects_v2') to safely process buckets containing over 1,000 objects.

Timestamp Evaluation: Used datetime.now(timezone.utc) to perform accurate, timezone-aware comparisons against object LastModified dates.

Execution & Deletion: Identified matching objects and executed delete_object calls.

Verification: Validated object deletion traces directly inside AWS CloudWatch Logs.

Task 2: Automated EBS Snapshot Creation and Lifecycle Retention
Overview & Objective
Executes a dual-action backup workflow: creates a tagged EBS snapshot from a target volume and purges existing snapshots older than 30 days.

Steps Followed
Snapshot Creation: Called ec2.create_snapshot() for a specified VOLUME_ID and attached tracking tags (CreatedBy=Lambda-Backup).

Retention Cleanup Loop: Queried account snapshots using describe_snapshots(OwnerIds=['self']), evaluated creation timestamps, and deleted snapshots exceeding 30 days using delete_snapshot().

EventBridge Automation: Configured a recurring EventBridge schedule (rate(7 days)) to trigger the backup loop automatically.

Task 3: Event-Driven EC2 Auto-Tagging on Launch
Overview & Objective
A reactive automation that captures EC2 state-change events in real time and automatically applies operational metadata tags to newly launched instances.

Steps Followed
Event Pattern Design: Configured an EventBridge Rule targeting aws.ec2 state notifications where state = running.

Payload Extraction: Extracted the dynamic instance-id directly from event['detail']['instance-id'].

Tag Application: Executed ec2.create_tags() to attach LaunchDate and Environment=Production tags automatically upon launch.

Live Verification: Launched a test t3.micro instance and verified that tags appeared on the EC2 Console within seconds of entering the running state.

Task 4: Daily AWS Cost Alert Using Cost Explorer API and SNS
Overview & Objective
Monitors Month-to-Date (MTD) AWS account spending via the Cost Explorer API and sends email alerts via Amazon SNS whenever spend exceeds a configured threshold.

Steps Followed
SNS Topic & Subscription Setup:

Created an Amazon SNS Topic (aws-cost-alerts).

Created an email subscription using zeeshan6362034446@gmail.com.

Confirmed the subscription via the AWS confirmation link delivered to the inbox.

IAM Permissions:

Created a dedicated IAM Execution Role with inline permissions for ce:GetCostAndUsage and sns:Publish.

Lambda Development & Deployment:

Wrote and deployed Python 3.12 code using Boto3 to query ce.get_cost_and_usage() for MTD UnblendedCost.

Configured logic to parse retrieved spend data and check if current_cost > COST_THRESHOLD.

Configured sns.publish() to broadcast an alert email when the threshold is exceeded.

Testing & EventBridge Schedule Setup:

Executed manual Lambda test invocations to verify spend calculation and email delivery.

Configured an EventBridge Schedule (rate(1 day)) to automate daily cost checks.

Verified receipt of automated daily cost alert notification emails in the inbox.

Verification Summary
Task 1: Objects older than the threshold purged; verified via CloudWatch logs.

Task 2: EBS snapshot created and tagged; retention script tested against snapshot timestamps.

Task 3: EC2 launch event intercepted by EventBridge; instance auto-tagged upon reaching running state.

Task 4: Cost Explorer queried; SNS alert email successfully delivered to zeeshan6362034446@gmail.com via manual test and daily EventBridge execution.
