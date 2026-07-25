Task 1: Automated S3 Bucket Cleanup (Objects > 30 Days)
Architectural Overview
Automates the detection and purging of stale S3 objects older than 30 days. Uses the low-level Boto3 client paginator (list_objects_v2) to bypass the standard 1,000-object API limit and handles timezone-aware UTC timestamp comparisons.

Phased Deployment Steps
Phase 1: IAM Role Creation — Provision an execution role using the inline policy defined in task1-s3-cleanup/iam_policy.json (scoped strictly to s3:ListBucket and s3:DeleteObject).

Phase 2: Lambda Deployment — Deploy task1-s3-cleanup/lambda_function.py under the Python 3.12 runtime.

Phase 3: Trigger & Execution — Configure a schedule trigger via EventBridge or execute manual invocation.

Live Deployment & Execution Verification
Initial State: Target S3 bucket contains test files.

Execution: Lambda scans LastModified attributes against datetime.now(timezone.utc) - timedelta(days=30).

Verification: CloudWatch logs confirm affected keys; target stale objects vanish from the bucket console.


Created S3 bucket and added test files:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/df6cf420-b8ab-4a09-9b52-e1bb5acd719c" />

IAM role showing:
Inline policy
AWSLambdaBasicExecutionRole attached
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/9a2fff23-ddfc-4a61-a7fd-afd84c54e75b" />

Creating Lambda function:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/cee41282-1245-4eb2-adbc-bdb2f9be42cc" />

Lambda configuration page:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/d532e965-93d9-4aa6-b11f-a0dfcc854420" />

Lambda code. For testing purpose, creating Age = 5minutes instead of 30 days. 
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/377a3485-fc76-4935-a90e-e76cec78e18a" />

Lambda test
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/9167d839-dcf6-48d8-86dc-ee89db926a6e" />

S3 content deleted by Lambda function:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/7776b4d1-774d-459b-8999-5217332810c0" />

Cloudwatch logs showing the action performed:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/9fa12a6e-5c2b-4fd2-bc56-929ab06d9569" />

Updated the Age = 30 days for assignment submission.
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/5bc5ec20-29c3-4484-b150-10f62916f886" />
