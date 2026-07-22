import boto3
from datetime import datetime, timedelta

# AWS Clients
ce = boto3.client("ce", region_name="us-east-1")
sns = boto3.client("sns")

# SNS Topic ARN
SNS_TOPIC_ARN = "arn:aws:sns:us-east-1:084032333279:DailyCostAlert"

# Threshold (Use 0.01 for testing, change to 50.0 for production)
THRESHOLD = 0.01


def lambda_handler(event, context):
    # Month-to-date date range
    today = datetime.utcnow().date()
    start_date = today.replace(day=1).strftime("%Y-%m-%d")
    end_date = (today + timedelta(days=1)).strftime("%Y-%m-%d")

    # Get current month's AWS cost
    response = ce.get_cost_and_usage(
        TimePeriod={
            "Start": start_date,
            "End": end_date
        },
        Granularity="MONTHLY",
        Metrics=["UnblendedCost"]
    )

    current_cost = float(
        response["ResultsByTime"][0]["Total"]["UnblendedCost"]["Amount"]
    )

    print(f"Current Month Cost: ${current_cost:.2f}")
    print(f"Threshold: ${THRESHOLD:.2f}")

    # Send SNS alert if threshold is exceeded
    if current_cost > THRESHOLD:

        message = (
            f"AWS Daily Cost Alert\n\n"
            f"Current Month-to-Date Cost: ${current_cost:.2f}\n"
            f"Configured Threshold: ${THRESHOLD:.2f}\n\n"
            f"The current AWS cost has exceeded the configured threshold."
        )

        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="AWS Daily Cost Alert",
            Message=message
        )

        print("SNS alert sent successfully.")

    else:
        print("Threshold not reached. No alert sent.")

    return {
        "statusCode": 200,
        "CurrentCost": current_cost,
        "Threshold": THRESHOLD,
        "Message": "Function executed successfully."
    }
