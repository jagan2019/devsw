courses = ['AWS','Java','DevOps','Python',456]
course_name = 'AWS'
del courses[0]
if course_name not in courses:
    print('{} is not present'.format(course_name))
else:
    print('{} is present'.format(course_name))
