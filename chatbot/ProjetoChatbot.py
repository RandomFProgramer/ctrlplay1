import Zé as pc 

nome_maquina = "Zé Gargalhadas" 
pc.saudacoes (nome_maquina)  
while True:  
    texto = pc.recebeTexto() 
    resposta = pc.buscaResposta (nome_maquina, texto) 
    if pc.exibeResposta (resposta, nome_maquina) == 'fim': 
        break