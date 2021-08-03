frase = input('Type any phrase: ').lower().strip()
print(f'The letter "a" appears {frase.count("a")} times')
print(f'It appeared the fist time at {frase.find("a")+1}° position')
print(f'And the last time at {frase.rfind("a")+1}°')
