# Um chatbot de piadas, talvez ofensivas.
def saudacoes(ZéG):
        import random
        frases = ["Bom dia!, procura por piadas? você veio ao lugar certo!","Oi,preparado para dar umas risadas?", "Boa tarde!, preparado para umas piadocas?","Boa Noite, você gostaria de umas piadas de ninar?"]
        print (frases[random.randint(0,3)])

def recebeTexto():
        texto = "Usuário: "  +  input ("Usuário: ")
        palavrasofensivas = ['fdp', 'vtnc', 'filha da puta','vai tomar no cu','Se fode','desgraçado','se mata','chupa','cabeça de pica','imbecil','idiota','mula sem cabeça']
        for p in palavrasofensivas:
                if p in texto :
                        print ("primeiro aviso!, se você não gostou da piada vá a outro lugar ou peça por outra.")
                        return recebeTexto

def buscaResposta (nome, texto):
     with open("BaseDeConhecimento.txt", "a+") as conhecimento: 
        conhecimento.seek(0) 
        while True: 
            viu = conhecimento.readline() 
            if viu != "": 
                if texto.replace("Cliente: ","") == "Tchau":
                    print(nome+": volte sempre!")
                    return "fim" 
                elif viu.strip() == texto.strip():
                    proximalinha = conhecimento.readline() 
                    if "Chatbot: " in proximalinha:
                        return proximalinha
                    else: 
                        print("Me desculpe, não sei o que falar") 
                        conhecimento.write("\n" + texto) 
                        resposta_user = input("O que esperava?\n") 
                        conhecimento.write("\n" +"Chatbot: "+resposta_user)
                        return "Hum..."
                    
def exibeResposta (resposta, nome): 
     print(resposta.replace("Chatbot", nome))  
     if resposta == "fim": 
        return "fim" 
     return "continua"