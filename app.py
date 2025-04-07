import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2', region_name='us-west-2')  # Specify your desired region

# Create a new EC2 instance
response = ec2.run_instances(
    ImageId='ami-0abcdef1234567890',  # Replace with your AMI ID (Amazon Machine Image)
    InstanceType='t2.micro',  # Choose the instance type
    MinCount=1,  # Minimum number of instances to launch
    MaxCount=1,  # Maximum number of instances to launch
    KeyName='your-key-pair',  # Replace with your SSH key pair name
    SecurityGroupIds=['sg-0a1b2c3d4e5f67890'],  # Replace with your security group ID
    SubnetId='subnet-678f1234',  # Replace with your subnet ID
    TagSpecifications=[  # Optional: add tags to your instance
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name', 'Value': 'MyEC2Instance'}
            ]
        }
    ]
)

# Output the instance ID of the newly created EC2 instance
print("New EC2 Instance created with ID:", response['Instances'][0]['InstanceId'])

