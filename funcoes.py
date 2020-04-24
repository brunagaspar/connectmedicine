import requests
import json 

# Funcoes de texto - informacionais


def maissobre(tema):

    msg=""

    if tema!="" and "A" in tema:
        msg="o ativo mais próximo é o ativo 32545\n"
        msg=msg+"Se for utilizar o ativo, não se esqueça de higienizalo\n"
        msg=msg+"\n"	
        
    if tema!="" and "ativo proximo" in tema:
        msg="o ativo mais próximo é o ativo 32545\n"
        msg=msg+"Se for utilizar o ativo, não se esqueça de higienizalo\n"
        msg=msg+"\n"
        
    if tema!="" and "projeto" in tema:
        msg="Precisa de ajuda para desenvolvimento de projetos? Nosso time virtual Partner Help Line é o canal para\n"
        msg=msg+"ajudá-lo no desenvolvimento do seu projeto, incluindo:\n"
        msg=msg+"-Dúvidas sobre produtos e funcionalidades\n"
        msg=msg+"-Construção da lista de materiais para compra\n"
        msg=msg+"-Apresentações remotas do portifólio Cisco para seus clientes\n"
        msg=msg+"\nComeçe por aqui:http://www.cisco.com/c/en/us/partners/support-help/presales-helpline.html\n"

    if tema!="" and "trein" in tema:
        msg="A Cisco disponibiliza para você Engenheirou ou Vendedor uma plataforma de treinamento on-line.\n"
        msg=msg+"No Partner Academy você encontra treinamentos EAD Cisco para todas as nossas soluções:\n"
        msg=msg+"https://salesconnect.cisco.com/#/program/PAGE-13518\n"

    if tema!="" and "suporte" in tema:
        msg="Desafios no uso dos produtos Cisco instalados? Contate nosso TAC\n"
        msg=msg+"Cisco Technical Assistance Center: http://www.cisco.com/c/pt_br/support/index.html\n"
        
    if tema!="" and "alert" in tema:
        msg="Nosso serviço de alertas avisa você diariamente sobre produtos entrando em Fim de Linha,\n"
        msg=msg+"Produtos com problemas de software conhecido e as últimas novidade a respeito de segurança\n"
        msg=msg+"dos produtos Cisco. Mantenha-se informado: http://www.cisco.com/cisco/support/notifications.html\n"

    return msg

#########################################################
## FUNCOES de Chamada API

#########################################################


def APICall (url,token):

    # chama API e devolve o conteudo, devolvo erro caso contrario
    try:
        headers = {
        'Authorization': "Bearer "+token,
        }

        response = requests.request("GET", url, headers=headers)

        return response.text

    except:
        return "erro"

#########################################################
## FUNCOES de Leitura de arquivos texto

#########################################################


def searchinfile(expression, file):

    # retorna linhas completas, caso texto seja encontrado

    #normaliza
    expression=expression.lower()

    msg = ""
    
    # Retorna erro se nome da pesquisa for muito pequeno
    if len(expression)<3:
        msg="Minimo 3 caracteres"
        return msg


    # loop de pesquisa  
    with open(file) as fp:  
        line = fp.readline()
        while line:
                  
            # Caso encontrado cria resposta
            if expression in line.lower():
                msg=msg+line
                    
            line = fp.readline()
                    
        # devolva negativa caso nada encontrado
        if msg=="":
            msg="Nenhum resultado encontrado.\n"

    return msg     
