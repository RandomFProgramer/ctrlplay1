def animal (classificacao, tipodeanimal, alimentacao ):
    tipos = {
        ('vertebrado', 'mamifero', 'carnivoro'): 'leão',
        ('vertebrado', 'ave', 'carnivoro'): 'águia',
        ('vertebrado', 'mamifero', 'herbivoro'): 'vaca',
        ('vertebrado', 'mamifero', 'carnivoro'): 'onça',
        ('vertebrado', 'ave', 'onivoro'): 'pomba',
        ('vertebrado', 'ave', 'herbivoro'): 'beija-flor',
        ('invertebrado', 'inseto', 'hematofago'): 'pulga',
        ('invertebrado', 'inseto', 'herbivoro'): 'lagarta',
        ('invertebrado', 'anelideo', 'onivoro'): 'minhoca',
        ('invertebrado', 'anelideo', 'hematofago'): 'sanguessuga',
    }
    chave = (classificacao, tipodeanimal, alimentacao)
    return tipos.get(chave, "Animal não encontrado")

classificacao = input("O animal é invertebrado ou vertebrado?")
tipodeanimal = input("Que tipo de grupo ele pertence?")
alimentacao = input("oque ele come?")

resultado = animal(classificacao, tipodeanimal, alimentacao)
print(resultado)