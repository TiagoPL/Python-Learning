peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
if imc < 18.5:
    print(f'IMC de {imc:.2f}, Abaixo do peso.')
elif imc == 18.5 or imc < 25:
    print(f'IMC {imc:.2f}, peso ideal.')
elif imc == 25 or imc < 30:
    print(f'IMC {imc:.2f}, acima do peso.')
elif imc == 30 or imc < 40:
    print(f'IMC {imc:.2f}, obesidade.')
elif imc > 40:
    print(f'IMC {imc:.2f}, obesidade morbida.')
