original_number = int(input('Choose a number to see its factorial: '))
current_number = original_number
final_number = original_number
while original_number != 1:
    current_number = current_number * (original_number - 1)
    original_number = original_number - 1
print(f'The factorial of "{final_number}" is "{current_number}".')
