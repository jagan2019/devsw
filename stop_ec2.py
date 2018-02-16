import boto3

x = boto3.client('ec2')

result = x.stop_instances(InstanceIds=['i-04d5ccb3f8f76f956',
                              'i-04184a2f978f5cd91'])

for instance in result['StoppingInstances']:
    instance_id = instance['InstanceId']
    previous_state = instance['PreviousState']['Name']
    print('{} stopped and its previous state is {}'.format(instance_id,previous_state))
