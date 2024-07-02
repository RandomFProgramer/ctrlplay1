#Esse foi o desafio para descobrir quanto um carro gastou de gasolina
class carro ():  # gq = Gasolina queimada e kmr = Km rodados e lpkm = Litros por km
    def __init__(self, gasolinaGasta, kmRodados, litrosporkm) :
        self.gasolinaGasta = gasolinaGasta
        self.kmRodados = kmRodados
        self.litrosporkm = litrosporkm      


gq = float (input("Quantos litros de gasolina foram gastos?"))
kmr = float (input("Quantos Kilometros foram rodados?"))

lpkm = gq/kmr

carro1 = carro( gasolinaGasta = gq, kmRodados = kmr, litrosporkm = lpkm )
print(carro1.litrosporkm, "km/l") #assim temos a resposta final
