import boto3

ec2 = boto3.client("ec2")

INSTANCE_ID = "i-0c25a36f07d16b5e5"

def lambda_handler(event, context):
    ec2.create_tags(
        Resources=[INSTANCE_ID],
        Tags=[
            {
                "Key": "Environment",
                "Value": "Development"
            }
        ]
    )

    print("Tag added successfully!")

    return {
        "statusCode": 200,
        "body": "Tag added successfully!"
    }
