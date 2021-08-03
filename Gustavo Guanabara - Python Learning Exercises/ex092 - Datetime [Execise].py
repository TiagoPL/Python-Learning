import datetime

year = datetime.date.today().year
my_dict = {}

my_dict['Name'] = input('Enter your name: ')
my_dict['Age'] = year - (int(input('Enter your year of birth: ')))
my_dict['Social'] = int(input('Enter your social number ([0] if you dont have): '))
if my_dict['Social'] != 0:
    my_dict['Year of Hire'] = int(input('Enter the year that you were hired: '))
    my_dict['Salary'] = float(input('Enter your salary: '))
    my_dict['Retirement Year'] = year + (35 - (year - my_dict['Year of Hire']))

print('=' * 50)
for k, v in my_dict.items():
    print(f'{k} of the person: {v}')
