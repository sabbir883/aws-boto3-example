# Create a single t2.micro instance using boto3 SDK. This uses Amazon Linux AMI 2016.03.1. 
#
#


import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
	
    DryRun=False,
    ImageId='ami-f5f41398',
    MinCount=1,
    MaxCount=1,
    KeyName='test_key_pair', # Use your configured_key_pair
    SecurityGroupIds=[ 'sg-7fbf7e04'], # use your configured security group's Id. 
    UserData='yum install httpd; chkconfig httpd on;/etc/init.d/httpd start',  # This will install httpd and start the httpd process
    InstanceType='t2.micro',
    BlockDeviceMappings=[
        {
	    'DeviceName': '/dev/xvda',	    
            'Ebs': {
                'SnapshotId': 'snap-a9b8c94e',
                'VolumeSize': 8,
                'DeleteOnTermination': True,
                'VolumeType': 'gp2'

            }
            
        }
    ],
  
    
    InstanceInitiatedShutdownBehavior='stop',
	IamInstanceProfile={
        'Arn': 'arn:aws:iam::590487556930:instance-profile/S3_Access'
    }
   
)


