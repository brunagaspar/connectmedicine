from config import *
from funcoes import *
from webexteams import getwebexMsg, webexmsgRoomviaID
import json

def logica(comando,usermail):

    # faz a logica de entender o comando pedido e a devida resposta para o usuario
    # o parametro usermail e' utilizado para identificar o usuario que solicitou o comando
    # O usuario pode ser uzado como filtro para se executar ou negar o comando
    #
    # Retorna mensagem para ser enviada para console ou Webex teams
    
    #Separa o comando por espacos
    #Primeiro item e'o comando em si, os demais sao parametros deste comando
    #
    
    comando = comando.lower()
    box=comando

    while box == "oi" or box == "ola" or box == "hey" or box == "ei" or box == "alo":
        msg=""
        arquivo=""
        msg= "Olá eu sou o Connect Medicine e estou aqui pra ajudar:\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Ativo mais próximo ?\n"  
        msg=msg+ "(2) - Ativos Disnponíveis ?\n"
        msg=msg+ "(3) - Quem está utilizando um ativo?\n"
        return msg,arquivo
    else:
        msg=""
        arquivo=""
        box2 = box
        #condicional para os serviços de ativos proximos
        if box2 == "1":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        elif box2 == "ativo":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        elif box2 == "proximo":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        elif box2 == "ativo proximo":
            msg="o ativo mais próximo é o ativo 32545"
            return msg,arquivo
        #ajudinha antecedendo possíveis erros de digitação de ativos proximos 
        elif box2 == "ativa":
            msg="As palavras que você digitou chegaram perto de 'ativo proximo' e 'proximo', tente elas"
            return msg,arquivo
        elif box2 == "procimo":
            msg="As palavras que você digitou chegaram perto de 'ativo proximo' e 'proximo', tente elas"
            return msg,arquivo
        elif box2 == "acivo":
            msg="As palavras que você digitou chegaram perto de 'ativo proximo' e 'proximo', tente elas"
            return msg,arquivo
        #ativos disponíveis
        elif box2 == "2":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        elif box2 == "disponivel":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        elif box2 == "disponibilidade":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        elif box2 == "ativo disponível":
            msg="Os ativos disponíveis são a maca de serial: 12345 e a cadeira de rodas de serial: 12331"
            return msg,arquivo
        #possíveis erros de digitação em ativos disponíveis
        elif box2 == "disponibel":
            msg="As palavras que você digitou chegaram perto de 'disponivel' , 'disponibilidade', tente elas"
            return msg,arquivo        
        elif box2 == "disponibilidads":
            msg="As palavras que você digitou chegaram perto de 'disponivel' , 'disponibilidade', tente elas"
            return msg,arquivo
        #Quem está utilizando o ativo
        elif box2 == "3" or box2 == "utilizando":
            msg= "Quem esta utilizando o ativo é Fernanda"
            return msg,arquivo
        #Possiveis erros de utilizando o ativo
        elif box2 == "utilandi" or box2 == "utiliza":
            msg: "As palavras que você digitou chegaram perto de 'utilizando', tente elas"
            return msg,arquivo

        
            



    # sp=comando.split(" ")

    # print(sp)
    
    # comando na variavel box, lower deixa em minusculo para normalizar
    
    # Para o caso de nenhum pedido coberto aqui
    mais="\nEscreva 'mais' para saber suas opções"
    
    # 21.11.19
    # variavel arquivo para o caso do bot devolver arquivos anexados
    
    # arquivo=""
    
    # msg=""
	
    # chamadas de acordo com os parametros

    # Funcoes para todos
    
    # Uso da funcao "mais"

    print(comando)
    print(box)

    if box == "oi":
        
        
        if box == "1":
            msg="dancing"

    elif box == "ei":
        msg= "Olá eu sou o Connect Medicine e estou aqui pra ajudar:\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Ativo mais próximo ?\n"  
        msg=msg+ "(2) - Disponibilidade ?\n"
        msg=msg+ "(3) - Quem está utilizando um ativo?\n"

    elif box == "ola":
        msg= "Olá eu sou o Connect Medicine e estou aqui pra ajudar:\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Ativo mais próximo ?\n"  
        msg=msg+ "(2) - Disponibilidade ?\n"
        msg=msg+ "(3) - Quem está utilizando um ativo?\n"

    elif box == "alo":
        msg= "Olá eu sou o Connect Medicine e estou aqui pra ajudar:\n" 
        msg=msg+ "Qual das seguintes opções deseja ?\n"   
        msg=msg+ "(1) - Ativo mais próximo ?\n"  
        msg=msg+ "(2) - Disponibilidade ?\n"
        msg=msg+ "(3) - Quem está utilizando um ativo?\n"

    else:
        msg="Não entendi o que você quis dizer, por favor tente dizer 'Oi' pra mim"


    #  if len(sp)>2:
    #             tema=sp[1]
    #             msg=maissobre(tema)
    #             print(sp)
    
        
    # # Funcoes que usam outras APIs
    # if len(sp)>1 and box=="api":
    #     # URL
    #     site="apitesteexample.com"
    #     # Parametro de autorizacao
    #     token="123456"
    #     msg=APICall(site,token)
        

    # return msg,arquivo


def trataPOST(content):

    # resposta as perguntas via webexteams
    # trata mensagem quando nao e' gerada pelo bot. Se nao e' bot, entao usuario
    try:     
        if content['name']==webhook_name and content['data']['personEmail']!=botmail:
            # identifica id da mensagem
            msg_id=(content['data']['id'])
            # identifica dados da mensagem
            webextalk=getwebexMsg(msg_id)
            usermail=webextalk[2]
            mensagem=webextalk[0]
            sala=webextalk[1]

            # executa a logica
            msg,arquivo=logica(mensagem,usermail)
        
            # Envia resposta na sala apropriada
            webexmsgRoomviaID(sala,msg,arquivo)

    except:
            print("POST nao reconhecido")
            pass