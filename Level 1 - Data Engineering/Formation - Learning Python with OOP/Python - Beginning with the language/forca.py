from time import sleep
import string
import random as r 

def inicializar_jogo():

    sleep(1)
    apresenta_cabecalho()

    arquivo_fonte_palavras = r'Level 1 - Data Engineering\Formation - Learning Python with OOP\Python - Beginning with the language\palavras.txt'
    palavra_secreta = seleciona_palavra_secreta(arquivo_fonte_palavras)
    auxiliar_interface_jogo = ['_' for letra in palavra_secreta]

    enforcou = False
    acertou = False 

    total_tentativas = 7
    erros = 0 

    while (not enforcou) and (not acertou):
        
        loop_printa_lista(auxiliar_interface_jogo)
        print(end=' ')

        chute = valida_chute_efetuado(input('Digite uma letra SEM ACENTOS: ').strip().lower(), auxiliar_interface_jogo)

        if (chute not in palavra_secreta):
            erros += 1
            sinaliza_tentativas_restantes(total_tentativas, erros)            
        else:
            contabiliza_acerto(chute ,auxiliar_interface_jogo, palavra_secreta)
            
        acertou, enforcou = verifica_encerramento(auxiliar_interface_jogo, acertou, enforcou, total_tentativas, erros, palavra_secreta)

        if acertou:
            imprime_mensagem_vencedor(auxiliar_interface_jogo)
        elif enforcou:
            imprime_mensagem_perdedor(palavra_secreta)

        print('-'*45)
        print()


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor(lista_auxiliar):
    print('-'*55)
    loop_printa_lista(lista_auxiliar)
    print()
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def loop_printa_lista(texto):
    for index in range(len(texto)):
        print(texto[index],end=' ')

def apresenta_cabecalho():
    print('-'*35)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*35)
    print()

def seleciona_palavra_secreta(arquivo_fonte):
    lista_palavras = []

    with open(arquivo_fonte, 'r') as palavras:
        for palavra in palavras:
            lista_palavras.append(palavra.strip())

    return r.choice(lista_palavras).lower()

def valida_chute_efetuado(letra, lista_auxiliar_jogo):
    if (letra in string.punctuation) or (letra in ('~~','^^')):
            while letra in string.punctuation:
                letra = input('Caracteres especiais não são permitidos. Por favor, digite novamente: ').strip().lower()
    
    elif(letra in lista_auxiliar_jogo): 
            while letra in lista_auxiliar_jogo:
                letra = input('Esse caractere já foi identificado. Por favor, insira uma nova letra: ').strip().lower()

    return letra

def sinaliza_tentativas_restantes(total_tentativas, erros):
    print('Você errou! Restam apenas {} tentativas.'.format(total_tentativas-erros))
    desenha_forca(erros)

def contabiliza_acerto(letra, lista_auxiliar, palavra):
    for index in range(len(palavra)):
                if (letra == palavra[index]):
                    lista_auxiliar[index] = letra

def verifica_encerramento(lista_auxiliar, bool_sucesso, bool_fracasso, total_tentativas, erros, palavra):
    if ('_' not in lista_auxiliar): 
        bool_sucesso = True

    elif (erros == total_tentativas):
        bool_fracasso = True
    
    return bool_sucesso, bool_fracasso

if (__name__ == '__main__'):
    inicializar_jogo()