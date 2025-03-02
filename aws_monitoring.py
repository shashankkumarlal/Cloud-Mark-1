import boto3

# Initialize AWS clients
ec2_client = boto3.client('ec2')
cloudwatch_client = boto3.client('cloudwatch')
iam_client = boto3.client('iam')
ce_client = boto3.client('ce')  # Cost Explorer

# Function to get EC2 instance monitoring data
def get_ec2_metrics():
    instance_id = "i-0c1b8ab17b27de679"  # Your EC2 instance ID
    metrics = cloudwatch_client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}],
        StartTime='2024-02-01T00:00:00Z',
        EndTime='2024-02-29T23:59:59Z',
        Period=86400,
        Statistics=['Average']
    )
    print(f"EC2 Instance {instance_id} CPU Utilization: {metrics.get('Datapoints', [])}")

# Function to fetch AWS Billing Cost Breakdown
def get_billing_details():
    response = ce_client.get_cost_and_usage(
        TimePeriod={'Start': '2024-02-01', 'End': '2024-02-29'},
        Granularity='MONTHLY',
        Metrics=['UnblendedCost']
    )
    print("Billing Cost Breakdown:", response.get('ResultsByTime', []))

# Function to list IAM users and policies
def get_iam_users():
    users = iam_client.list_users()
    print("IAM Users:", [user['UserName'] for user in users.get('Users', [])])

# Call functions
get_ec2_metrics()
get_billing_details()
get_iam_users()
