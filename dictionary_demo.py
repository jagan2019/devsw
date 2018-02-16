courses = {'AWS':15000,'DevOps':12000,'data':{'Name':'Prasad'}}
# Print only keys
print('----Keys-----')
for key in courses:
    print(key)

# Print only values
print('-----Values-----')
for values in  courses.values():
    print(values)

# Print keys and values
print('-----Keys & Values-----')
for key in courses:
    print('Course name = {} And its cost = {}'.format(key,courses.get(key)))
