Task 2: Automated EBS Snapshot Creation and Lifecycle Retention
Architectural Overview
Performs dual operations: creates a tagged EBS snapshot (CreatedBy=Lambda-Backup) from a target volume, and scans existing account snapshots to purge backups older than 30 days.

Phased Deployment Steps
Phase 1: IAM Configuration — Attach ec2:CreateSnapshot, ec2:DescribeSnapshots, ec2:DeleteSnapshot, and ec2:CreateTags scoped policy to the function role.

Phase 2: Code Deployment — Deploy task2-ebs-snapshot/lambda_function.py. Set environment variable VOLUME_ID.

Phase 3: EventBridge Scheduling — Link an EventBridge rule configured for weekly execution (rate(7 days)).

Live Deployment & Execution Verification
Creation Verification: Inspect EC2 Console -> Snapshots to confirm the newly minted snapshot ID and tags.

Retention Verification: CloudWatch logs confirm deletion of older tagged snapshot IDs exceeding the retention threshold.


Created EC2 Instance with default VPC and t3.micro
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/a64d6f49-a6ed-4cc1-8287-e7700103c341" />

IAM user Role addition:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/b332a164-b00c-4511-9246-8e0e62e4cff3" />

Configuring Lambda function:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/dab5beae-99db-4a1b-88bd-391f47b8fe9f" />

python code added in lambda function:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/e59c62ff-0e87-42db-b77a-fd5fc9e85d0a" />

test event created 
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/386f0be7-c547-41a8-8378-fdb62f34fda8" />

cloud watch
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/4eeed556-b8f5-4d88-9ff2-e5d7b223f6cf" />

ECS snapshot
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/97716f18-bf6d-40e3-b3c6-728a2402f2aa" />

Creating Event Bridge:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/b4b3c54b-7e63-4151-a8f9-aa2a2c42b36c" />
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/887f284f-99d3-41ea-870c-9300552d2c2b" />
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/5a8244a9-5052-4fbe-a485-c81a7e1f93c0" />

Event bridge task:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/af50a5ad-4789-4371-ad3b-681f50c26dac" />

EventBridge Scheduler:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/3e6c8a3e-ac98-4339-a939-c333454774c9" />


