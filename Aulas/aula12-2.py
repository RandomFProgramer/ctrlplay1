class casa(): 
    imobiliaria = "Seu Toinho"
    def __init__(self, rua, bairro, CEP):
        self.rua = rua
        self.bairro = bairro
        self.CEP = CEP
    def enderecoCompleto(self):
        return "Endereço Completo: "+self.rua+","+self.bairro+"-CEP:"+self.CEP+"feita pela imobiliária "+self.imobiliaria
casaA = casa(rua = "yesman", bairro = "Goodsprings" , CEP= "128965238")
casaB = casa(rua = "Prim", bairro = "Casinovile", CEP = "193834657")
print (casaA.enderecoCompleto())
print (casaB.enderecoCompleto())