def exibeResposta_GUI(texto, resposta, nome):
    return resposta.replace("Chatbot",nome)
    
def saudacao_GUI(nome):
    import random
    frases = ["Bom dia!, procura por piadas? você veio ao lugar certo!","Oi,preparado para dar umas risadas?", "Boa tarde!, preparado para umas piadocas?","Boa Noite, você gostaria de umas piadas de ninar?"]
    return (frases[random.randint(0,3)])

def salva_sugestao(sugestao):
    with open("falar.txt","a+",encoding = 'utf-8', errors = 'replace') as conhecimento:
        conhecimento.write("Chatbot: " + sugestao + "\n")
        
def buscaResposta_GUI(texto):
    with open("falar.txt","a+",encoding = 'utf-8', errors = 'replace') as conhecimento:
        conhecimento.seek(0)
        while True:
            viu = conhecimento.readline()
            if viu != "":
                if jaccard(texto,viu) > 0.3:
                    proximalinha = conhecimento.readline()
                    if "Chatbot: " in proximalinha:
                        return proximalinha
            else:
                conhecimento.write('\n' + texto)
                return "Se me desculpe, mas não sei o que falar sobre isso"
            
def jaccard(textoUsuario, textoBase):
    textoUsuario = limpa_frase(textoUsuario)
    textoBase = limpa_frase(textoBase)
    if len(textoBase)<1: return 0
    else:
        palavras_em_comum = 0
        for palavra in textoUsuario.split():
            if palavra in textoBase.split():
                palavras_em_comum += 1
        return palavras_em_comum/(len(textoBase.split()))
    
def limpa_frase(frase):
    tirar = ["?","!","...",".",",","Cliente: ", "\n"]
    for t in tirar:
        frase = frase.replace(t,"")
    frase = frase.upper()
    return frase