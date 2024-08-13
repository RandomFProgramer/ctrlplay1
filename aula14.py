#parte 1 da aula
def nomecompleto (nome, sobnome1, sobnome2):
    if (len(sobnome1)> len(sobnome2)):
        return nome +' '+ sobnome1 +' '+ sobnome2
    else:
        return nome +' '+ sobnome2 +' '+ sobnome1
    

nome = input()
sobnome1 = input()
sobnome2 = input()
print(nomecompleto(nome, sobnome1, sobnome2))