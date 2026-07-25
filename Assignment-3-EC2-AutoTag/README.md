Task 3: Event-Driven EC2 Auto-Tagging on Launch
Architectural Overview
A reactive, event-driven pattern that captures state-change events whenever an EC2 instance enters the running state. It extracts the target instance-id from the EventBridge event payload and attaches metadata tags (LaunchDate and Environment).

Phased Deployment Steps
Phase 1: IAM Configuration — Deploy an execution role granting ec2:CreateTags and ec2:DescribeInstances.

Phase 2: Function Setup — Deploy task3-ec2-autotag/lambda_function.py.

Phase 3: EventBridge Rule Setup — Construct an EventBridge Event Pattern filtering for aws.ec2 state-change notifications matching running.

JSON
{
  "source": ["aws.ec2"],
  "detail-type": ["EC2 Instance State-change Notification"],
  "detail": {
    "state": ["running"]
  }
}
Live Deployment & Execution Verification
Launch a t3.micro EC2 instance.

Observe the reactive EventBridge trigger invoke the Lambda within seconds.

Verify tags LaunchDate and Environment=Production are attached on the EC2 Console.



Creating IAM rule and attaching inline policy: 
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/1f35d67b-4743-41e6-bfd9-e64233d17daa" />

Launched EC2 Instance:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/31da9506-a3d5-4448-b35c-2e94082a78e5" />

Creating Lambda function:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/db696531-85e5-4f98-ade7-8ab5d4a42a97" />

Deploying Python code:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/b62db993-b786-4e33-8018-38e3dfb807b5" />

Tested the deployment:
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/44eebef1-6ad7-44dc-8934-eca659e9e3b1" />

Auto tag created successfully
<img width="3274" height="2048" alt="image" src="https://github.com/user-attachments/assets/c1614b87-e3d7-428a-be35-29de3689c6ae" />
