import Zé as pc

nome_maquina = "Zé Gargalhadas"
pc.saudacao(nome_maquina)
while True:
    texto = pc.recebeTexto()
    resposta = pc.buscaResposta("Cliente: "+texto+"\n")
    if pc.exibeResposta(texto,resposta, nome_maquina) == "fim":
        break