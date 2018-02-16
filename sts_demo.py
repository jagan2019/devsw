import boto3

client = boto3.client('sts')

response = client.assume_role(
    RoleArn='arn:aws:iam::807570218647:role/HariRole',
    RoleSessionName='hari'
)

creds = response['Credentials']
access_key_id = creds['AccessKeyId']
secret_key = creds['SecretAccessKey']
session_token = creds['SessionToken']
creds = {}
creds['aws_access_key_id'] = access_key_id
creds['aws_secret_access_key'] = secret_key
creds['aws_session_token'] = session_token

botosession = boto3.session.Session(**creds)

ec2 = botosession.resource('ec2')
resp = ec2.instances.filter()
print(resp)