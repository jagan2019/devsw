import json

# Read file and convert it into string
raw_data = open('data.json').read()

# Convert string into dictionary

data = json.loads(raw_data)

print(data['Name'])
print(data['Age'])

for x in data['Location']:
    print('Location is {} and Pin is {}'.format(x['Name'],x['Pin']))

