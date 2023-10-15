from random import randint, random
from time import sleep

def inicializar_jogo():
    # Cabeçalho de apresentação do mini-game
    sleep(1)
    print('-'*35)
    print('Bem vindo(a) ao jogo de advinhação!')
    print('-'*35)
    print()
    #numero_secreto = 42
    numero_secreto = randint(1,100)
    #numero_secreto = round(random()*100)
    sleep(2)

    # -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x --  
    # Tip: you can type "Ctrl+L" to clean the Vs Code python terminal.
    # -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- -- x -- 

    # Cabeçalho de apresentação dos níveis de dificuldade
    print('- x - x '*4,end='')
    print('-')
    sleep(1)
    print('! DIFICULDADES !'.center(30))
    sleep(1)
    print('1 - Fácil   (   até acertar   )'.center(30))
    sleep(1)
    print('2 - Médio   (   7 tentativas  )'.center(28))
    sleep(1)
    print('3 - Difícil (   3 tentativas  )'.center(28))
    sleep(1)
    print('- x - x '*4,end='')
    print('-')

    sleep(1)
    print()

    # Obtém a dificuldade cadastrada pelo jogador e efetua um tratamento caso seja fornecido um valor inválido
    dificuldade = input('Informe a dificuldade desejada: ')
    if (dificuldade not in ['1','2','3']):
        while (dificuldade not in ['1','2','3']):
            dificuldade = input('Você digitou uma dificuldade inválida. Por favor, insira corretamente: ')
    sleep(1)

    # Emite uma mensagem de feedback de acordo com o input do jogador
    if (int(dificuldade) == 1):
        print(f'Muito bem! Você poderá testar as respostas até acertar.')
    elif (int(dificuldade) == 2):
        total_tentativas = 7
        print(f'Muito bem! Você terá {total_tentativas} tentativas.')
    elif (int(dificuldade) == 3):
        total_tentativas = 3
        print(f'Muito bem! Você terá {total_tentativas} tentativas.')

    # Emite uma mensagem de feedback indicando que o jogo está para começar
    sleep(1)
    print('Iniciando',end='')
    for i in range(3):
        if (i == 2):
            print('.')
        else:
            print('.',end='')
        sleep(1)
    print()
    print('-'*30)


    # define uma variável de controle da pontuação do jogador 
    # (por padrão todo jogador começa com 100 pontos, e a cada erro essa pontuação vai diminuindo 
    # de acordo com a distância dos chutes efetuados em relação ao valor verdadeiro)
    pontuacao = 100

    # exemplo: valor verdadeiro = 50 // chute da rodada = 30 => -20 pontos são aplicados, e assim por diante.

    # Caso a dificuldade seja "Fácil"
    if (int(dificuldade) == 1):
        controle_rodada = 1 # define uma variável de controle de rodadas
        
        # Começa um loop de execução infinita do game...
        while True:
            chute = int(input('Digite um numero entre 1 e 100: ')) # obtém o chute do jogador
            sleep(1)
            print()

            # verifica se esse chute é válido e emite um aviso de feedback
            if (chute < 1) or (chute > 100):
                print('Voce deve digitar um número entre 1 e 100!')
                continue # força o código a prosseguir para o próximo passo do loop sem executar os códigos seguintes

            # logo após o chute efetuado, efetuo um ajuste na pontuação do jogador
            pontuacao -= abs(chute - numero_secreto)

            # caso a pontuação passe a apresentar valores negativos..
            if (pontuacao < 0):
                pontuacao = 0 # reajusto a variável para o valor 0 (não existem pontos negativos)

            # variaveis do tipo boolean
            acertou = chute == numero_secreto 
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto

            if acertou: # em caso de acerto da resposta..
                print('Correto! O número secreto era {}.'.format(numero_secreto))
                sleep(1)
                print('Voce acertou a resposta em {} tentativas!'.format(controle_rodada))
                sleep(1)
                print('Pontuação final: {} pontos. Obrigado por jogar!'.format(pontuacao))
                sleep(1)
                print('Fim de jogo.')
                break # o jogo se encerra

            else: # em caso de erro da resposta..

                # é emitida uma mensagem de feedback para o jogador de acordo com a relação com respeito ao número secreto.
                if maior:
                    print('Voce digitou o numero: {}! Esse chute é maior do que o número secreto.'.format(chute))
                elif menor:
                    print('Voce digitou o numero: {}! Esse chute é menor do que o número secreto.'.format(chute))

            print('-'*30)
            controle_rodada += 1 # atualiza a variável de controle de rodadas para
            sleep(1)

    # Caso a dificuldade seja "Médio" ou "Difícil"..
    else:

        # define um loop para que o jogador tente acertar a resposta de acordo com o número de tentativas da dificuldade
        for controle_rodada in range(total_tentativas): 
            print(f'Rodada {controle_rodada+1} de {total_tentativas}')
            chute = int(input('Digite um numero entre 1 e 100: '))
            sleep(1)
            print()

            # verifica se esse chute é menor que 1 ou menor que 100 e emite um aviso de feedback
            if (chute < 1) or (chute > 100):
                print('Voce deve digitar um número entre 1 e 100!')
                continue # força o código a prosseguir para o próximo passo do loop sem executar os códigos seguintes

            # logo após o chute efetuado, efetuo um ajuste na pontuação do jogador
            pontuacao -= abs(chute - numero_secreto)
            
            # caso a pontuação passe a apresentar valores negativos..
            if (pontuacao < 0):
                pontuacao = 0 # reajusto a variável para o valor 0 (não existem pontos negativos)

            # variaveis do tipo boolean
            acertou = chute == numero_secreto 
            maior   = chute > numero_secreto
            menor   = chute < numero_secreto

            if acertou: # em caso de acerto da resposta..
                print('Correto!!')
                sleep(1)
                print('Voce acertou a resposta em {} tentativas!'.format(controle_rodada))
                sleep(1)
                print('Pontuação final: {} pontos. Obrigado por jogar!'.format(pontuacao))
                sleep(1)
                print('Fim de jogo.')
                break # o jogo se encerra (sem que haja necessidade de concluir todas as rodadas de tentativa)

            else: # em caso de erro da resposta..

                # é emitida uma mensagem de feedback para o jogador de acordo com a relação com respeito ao número secreto.
                if maior:
                    print('Voce digitou o numero: {}. Esse chute é maior do que o número secreto.'.format(chute))
                elif menor:
                    print('Voce digitou o numero: {}. Esse chute é menor do que o número secreto.'.format(chute))
            sleep(1)
        
            # verifica se a quantidade de tentativas do jogador se esgotou..
            if (controle_rodada+1 == total_tentativas):

                pontuacao = 0 # se o jogo for finalizado por encerramento da quantidade de tentativas, então a pontuação deve ser 0 (o número gerado não foi alcançado)

                # em caso positivo, emite um feedback de finalização do aplicativo
                print('Você esgotou todas as tentativas! O número secreto era {}.'.format(numero_secreto))
                sleep(1)
                print('Pontuação final: {} pontos. Obrigado por jogar!'.format(pontuacao))
                sleep(1)
                print('Fim de jogo.') 
            print('-'*30)

# A variável __name__ é definida sempre que um arquivo é executado;
# se esse arquivo é executado diretamente pelo prompt de comando (como um arquivo python "principal),
# então queremos que o código dentro dele seja executado automaticamente. Daí a relevância do if abaixo
if (__name__ == '__main__'):
    inicializar_jogo()