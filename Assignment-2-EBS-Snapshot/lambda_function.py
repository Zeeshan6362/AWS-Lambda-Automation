import boto3
from datetime import datetime, timezone, timedelta

ec2 = boto3.client("ec2")

VOLUME_ID = "vol-00dbf223f6e352b7f"

# Retention period
RETENTION_DAYS = 30

def lambda_handler(event, context):

    # Step 1: Create Snapshot
    response = ec2.create_snapshot(
        VolumeId=VOLUME_ID,
        Description="Automated Lambda Backup"
    )

    snapshot_id = response["SnapshotId"]

    print(f"Snapshot Created: {snapshot_id}")

    # Step 2: Tag Snapshot
    ec2.create_tags(
        Resources=[snapshot_id],
        Tags=[
            {
                "Key": "CreatedBy",
                "Value": "Lambda-Backup"
            }
        ]
    )

    print("Tag Added Successfully")

    # Step 3: Calculate cutoff date
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=RETENTION_DAYS)

    # Step 4: Get snapshots created by Lambda
    snapshots = ec2.describe_snapshots(
        OwnerIds=["self"],
        Filters=[
            {
                "Name": "tag:CreatedBy",
                "Values": ["Lambda-Backup"]
            }
        ]
    )

    deleted_snapshots = []

    # Step 5: Delete old snapshots
    for snapshot in snapshots["Snapshots"]:

        if snapshot["StartTime"] < cutoff_date:

            ec2.delete_snapshot(
                SnapshotId=snapshot["SnapshotId"]
            )

            print(f"Deleted Snapshot: {snapshot['SnapshotId']}")

            deleted_snapshots.append(snapshot["SnapshotId"])

    return {
        "statusCode": 200,
        "CreatedSnapshot": snapshot_id,
        "DeletedSnapshots": deleted_snapshots
    }
