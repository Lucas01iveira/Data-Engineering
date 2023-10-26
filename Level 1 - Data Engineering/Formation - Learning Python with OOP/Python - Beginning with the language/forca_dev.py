from time import sleep
import string
import random as r 

# função auxiliar responsável por apresentar a interface do jogo
def loop_printa_lista(texto):
    for index in range(len(texto)):
        #if (index == len(texto)-1):
        #    print(texto[index])
        #else:
        #    print(texto[index]+' ', end='')
        print(texto[index],end=' ')

def apresenta_cabecalho():
    print('-'*35)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*35)
    print()

def inicializar_jogo():
    # Cabeçalho de apresentação do mini-game
    sleep(1)
    apresenta_cabecalho()

    lista_palavras = [] # defino uma lista para armazenar as palavras do arquivo

    # definição da palavra secreta do jogo 
    with open(r'Level 1 - Data Engineering\Formation - Learning Python with OOP\Python - Beginning with the language\palavras.txt', 'r') as palavras:
        # alimento a lista gerada com as palavras do arquivo
        for palavra in palavras:
            lista_palavras.append(palavra.strip())

    # o codigo abaixo não é necessário com a utilização da sintaxe "with open"
    #palavras.close() # fechamento do arquivo em aberto (boa prática)

    # seleciono uma palavra aleatória da lista alimentada a partir do arquivo
    palavra_secreta = r.choice(lista_palavras).lower()

    # defino uma lista para nos auxiliar na emissão e atualização da interface do jogo
    #auxiliar_interface_jogo = []
    #for letra in palavra_secreta:
    #    auxiliar_interface_jogo.append('_')

    # outra maneira de fazer:
    auxiliar_interface_jogo = ['_' for letra in palavra_secreta] # funcionalidade de "list comprehension"

    # outra maneira de fazer:
    #auxiliar_interface_jogo = ['_']*len(palavra_secreta)

    # definição de duas variáveis auxiliares para controlar o andamento do fluxo do jogo
    enforcou = False # armazena a informação se o jogador foi enforcado ou não (início False: o jogador não começa enforcado)
    acertou = False # armazena a informação se o jogador ganhou ou não (início False: o jogador não começa já vencendo)

    total_tentativas = len(palavra_secreta) # defino um número máximo de tentativas para o jogador com base na quantidade de caracteres
    erros = 0 # variável auxiliar para contar a quantidade de erros do jogador

    # outra maneira de escrever a lógica abaixo: while (enforcou == False) and (acertou == False):
    while (not enforcou) and (not acertou):
        
        loop_printa_lista(auxiliar_interface_jogo)
        print(end=' ')
        # obtém uma letra inserida pelo usuário
        chute = input('Digite uma letra SEM ACENTOS: ').strip().lower()

        # efetua uma validação do chute inserido a fim de evitar caracteres especiais
        if (chute in string.punctuation) or (chute in ('~~','^^')):
            while chute in string.punctuation:
                chute = input('Caracteres especiais não são permitidos. Por favor, digite novamente: ').strip().lower()
        
        # verifico se a letra chutada já foi chutada antes
        if (chute in auxiliar_interface_jogo): # ou seja, se a letra chutada já foi atualizada na variável auxiliar
            while chute in auxiliar_interface_jogo:
                chute = input('Esse caractere já foi identificado. Por favor, insira uma nova letra: ').strip().lower()
        
        # verifico se a letra chutada está presente na palavra secreta
        if (chute not in palavra_secreta):
            erros += 1
            print('Você errou! Restam apenas {} tentativas.'.format(total_tentativas-erros))
        else:
            for index in range(len(palavra_secreta)):
                if (chute == palavra_secreta[index]):
                    auxiliar_interface_jogo[index] = chute
        
        # condições de finalização do loop!
        # 1) verifico se a minha lista auxiliar já está completamente preenchida
        if ('_' not in auxiliar_interface_jogo): # se não houverem mais '_' significa que a pessoa preencheu todas as letras da palavra oculta
            print('-'*55)
            loop_printa_lista(auxiliar_interface_jogo)
            print()
            print('Parabéns! Você venceu o jogo da forca.')
            acertou = True
        
        # 2) verifico se o jogador já esgotou todas as suas tentativas
        elif (erros == total_tentativas):
            print('-'*45)
            print('Que pena! Você perdeu.\nA palavra secreta era {}'.format(palavra_secreta))
            print('Obrigado por jogar!')
            enforcou = True

        print('-'*45)
        print()


# A variável __name__ é definida sempre que um arquivo python é executado;
# se esse arquivo é executado diretamente pelo prompt de comando (como um arquivo python "principal),
# então queremos que o código dentro dele seja executado automaticamente. Daí a relevância do if abaixo
if (__name__ == '__main__'):
    inicializar_jogo()