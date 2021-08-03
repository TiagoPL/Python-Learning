my_dict = {}
my_list = []
age = 0
average = 0
womans = []

while True:
    my_dict["Name"] = input('Name: ').capitalize().strip()
    while not my_dict["Name"].isalpha():
        print('\33[0;31mError! Please, type only letters.\33[m')
        my_dict["Name"] = input('Name: ').capitalize().strip()
    my_dict["Gender"] = input('Gender: [M/F] ').upper().strip()
    while my_dict["Gender"] != 'M' and my_dict["Gender"] != 'F':
        print('\33[0;31mError! Please type only [M] or [F]: \33[m')
        my_dict["Gender"] = input('Gender: ').upper().strip()
    if my_dict["Gender"] == 'F':
        womans.append(my_dict["Name"])
    my_dict["Age"] = input('Age: ').strip()
    while not my_dict["Age"].isnumeric():
        print('\33[0;31mError! Please, type only the age number: \33[m')
        my_dict["Age"] = input('Age: ').strip()

    age = age + int(my_dict["Age"])
    my_list.append(my_dict.copy())
    my_dict.clear()

    resp = input('Want to cotinue? [Y/N]: ').upper().strip()
    while resp != 'Y' and resp != 'N':
        print('\33[0;31mError! Please, type only [Y] or [N]: \33[m')
        resp = input('Want to continue? [Y/N]: ').upper().strip()
    if resp == 'N':
        break

average = (age / len(my_list))

print('=' * 50)
print(f'A) Overall, we have {len(my_list)} people.')
print(f'B) The average age is of {average:.0f} years old.')
if len(womans) > 0:
    print(f'C) The womans were: {womans}')
print(f'D) People above the average age:')
for pessoa in my_list:
    if int((pessoa["Age"])) > average:
        print(f'Name: {pessoa["Name"]}; Gender: {pessoa["Gender"]}; Age: {pessoa["Age"]}')
print('=' * 50)
