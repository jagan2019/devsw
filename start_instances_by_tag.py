'''
Start instances by tag
Key = Env
Value = ['Dev']
'''

import boto3

client = boto3.client('ec2')

response = client.describe_regions()
print(response)

# # Filter by instance type
#
# filter =[
#         {
#             'Name': 'tag:Env',
#             'Values': [
#                 'Dev'
#             ]
#         }
#     ]
#
# instances = ec2.instances.filter(Filters=filter)
# for x in instances:
#     print(x)
#     x.start()