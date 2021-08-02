peso = float(input('Type your weight: '))
altura = float(input('Type your height: '))
bmi = peso / altura ** 2
if bmi < 18.5:
    print(f'BMI {bmi:.2f}, below weight.')
elif bmi == 18.5 or bmi < 25:
    print(f'BMI {bmi:.2f}, ideal weight.')
elif bmi == 25 or bmi < 30:
    print(f'BMI {bmi:.2f}, overweight.')
elif bmi == 30 or bmi < 40:
    print(f'BMI {bmi:.2f}, obesity.')
elif bmi > 40:
    print(f'BMI {bmi:.2f}, morbid obesity.')
