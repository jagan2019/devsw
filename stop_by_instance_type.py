'''
Get all the instances whose type is t2.micro, and stop them
'''

import boto3

ec2 = boto3.resource('ec2')

# Filter by instance type

filter =[
        {
            'Name': 'instance-type',
            'Values': [
                't2.micro',
            ]
        }
    ]

instances = ec2.instances.filter(Filters=filter)
for x in instances:
    print(x)
    x.stop()