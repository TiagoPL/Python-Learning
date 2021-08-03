name = input('What is the students name?')
average = float(input('What is the students average score?'))
if average > 5:
    situation = 'Approved'
else:
    situation = 'Fail'

student = {'Name': name, 'Media': average, 'Situation': situation}

print('=' * 40)
print(f'''Student name: {student["Name"]}
Student Average: {student["Media"]}
Status: {student["Situation"]}''')
