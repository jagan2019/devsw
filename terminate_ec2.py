import boto3

x = boto3.client('ec2')

x.terminate(InstanceIds=['i-018691571dfb23f6d',
                              'i-04d5ccb3f8f76f956',
                              'i-08bafd7443b1b75ba'])