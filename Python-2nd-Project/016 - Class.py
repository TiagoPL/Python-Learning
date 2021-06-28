class Kettle(object):                     # Cria um 'tutorial' pra criar Kettles

    power_source = 'Eletricity'

    def __init__(self, make, price):      # Cria um Kettle com nome e preço
        self.make = make
        self.price = price
        self.on = False                   # Kettle é criado desligado

    def switch_on(self):                  # Cria outra função dentro da classe pra ligá-lo
        self.on = True


kenwood = Kettle('Kenwood', 8.99)         # Criamos o primeiro Kettle

hamilton = Kettle('Hamilton', 14.55)      # Criamos o segundo Kettle

####################################################################################

print(hamilton.on)                        # Verificamos se está ligado ou desligado
hamilton.switch_on()                      # Ligando o Kettle direto pela Instance
print(hamilton.on)                        # Verificamos de novo

Kettle.switch_on(kenwood)                 # Ligando o Kettle pela Class
print(kenwood.on)                         # Verificamos de novo

print()
####################################################################################

kenwood.power = 1.5                       # Acrecentando um novo atributo pro objeto
print(kenwood.power)

print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
