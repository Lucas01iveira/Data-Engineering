'''
Jogo da velha interativo

Autor: Lucas de Paula Oliveira
'''

# Funções importantes para a execução do código main:
# 1) cria_tabuleiro
# 2) apresenta_tabuleiro
# 3) atualiza_tabuleiro
# 4) verifica_conclusao

# -- x -- x -- x-- x -- x -- x-- x -- x -- x-- x -- x -- x-- x -- x -- x-- x -- x -- x-- x -- x -- x-- x -- x -- x-- x -- x -- x
import random as r 
from time import sleep
from sre_compile import isstring
import os

# Defino uma função que cria uma matriz 3x3 e atribui valores ordenados de 1 a 9 em cada posição,
# para posterior desenvolvimento do jogo e orientação dos jogadores

def tabuleiro():
    # Parâmetros de entrada:
        
    # Parâmetros de saída:
        # - Matriz 3x3 enumerada

    # -------------------------------------------------------------
    M = [] # defino uma matriz 
    Msize = 3 # (tamanho 3x3) 

    cont = 1 # variável contadora
    for i in range(Msize): # para cada linha i
        linha = [] # defino um vetor auxiliar de preenchimento das linhas

        for j in range(Msize): # para cada coluna j
            linha.append(cont) # acrescento a variável contadora 
            cont += 1 # atualizo a variável contadora
        
        M.append(linha) # acrescento a linha na matriz M
            
    return M


# Defino uma função que apresenta o tabuleiro criado no formato matricial usual
def apresenta_tabuleiro(A):
    # Parâmetros de entrada
        # - Matriz do tabuleiro (A)
    
    # Parâmetros de saída
        # 

    
    # obs.: a sequência de códigos contida nessa função é meramente ilustrativa
    # (não há nenhuma lógica muito profunda; as escolhas de script
    # foram escolhidas simplesmente de maneira que resultassem 
    # numa apresentação confortável do tabuleiro do jogo)
    # -------------------------------------------------------------
    Asize = len(A) # tamanho da matriz

    print('{:^138}'.format('-'*79))
    for i in range(Asize): # para cada linha i
        print('{:>30}'.format('|'), end='') # no início de cada linha, incluo uma barra

        for j in range(Asize): # para cada linha j

            if j != Asize-1: # se o índice j é um índice 'interno'
                # faz um print formatado
                #print('  ' + str(A[i][j]) + '  ', end = '|') 
                print('{:^25}'.format(A[i][j]), end = '|')

            else: # senão (ou seja, se for o índice do último elemento de cada linha)
                # faz um print formatado (com ajustes)
                #print('  ' + str(A[i][j]) + '  ') 
                print('{:^25}'.format(A[i][j]), end='') 
                print('|')
                print('{:^138}'.format('-'*79))


# Defino uma função de 'cadastro' dos jogadores
def cadastra_jogadores_multiplayer():
    # Parâmetros de entrada:
        #
        
    # Parâmetros de saída:
        # - simbolo_jogador1: 'X' ou 'O'
        # - simbolo_jogador2: 'X' ou 'O'

    # -------------------------------------------------------------

    # Cadastra o símbolo do primeiro jogador
    print('Jogador 1, qual símbolo você escolhe? [X | O]')
    simbolo_jogador1 = str(input('Resposta: '))

    # Faz um tratamento de escolha
    if simbolo_jogador1 != 'X' or simbolo_jogador1 != 'O':
        while simbolo_jogador1 != 'X' and simbolo_jogador1 != 'O':
            simbolo_jogador1 = str(input('Escolha inválida. Por favor, digite novamente: '))

    # Atribui o símbolo do jogador 2 de acordo com a escolha do jogador 1
    if simbolo_jogador1 == 'X':
        simbolo_jogador2 = 'O'
    else:
        simbolo_jogador2 = 'X'
    
    sleep(1) # espera 1s
    print('Jogador 2, o seu símbolo será {}'.format(simbolo_jogador2))

    sleep(1) # espera 1s
    print('O jogo irá começar...') 
    sleep(1) # espera 1s
    for i in range(3):
        print('.')
        sleep(1) # espera 1s
    
    return simbolo_jogador1, simbolo_jogador2


# Defino uma função de 'cadastro' do jogador (no caso de game contra o próprio computador)
def cadastra_jogador_singleplayer():
# Parâmetros de entrada:
        #
        
    # Parâmetros de saída:
        # - simbolo_jogador: 'X' ou 'O'

    # -------------------------------------------------------------

    # Cadastra o símbolo do primeiro jogador
    print('Jogador, qual símbolo você escolhe? [X | O]')
    simbolo_jogador = str(input('Resposta: '))

    # Faz um tratamento de escolha
    if simbolo_jogador != 'X' or simbolo_jogador != 'O':
        while simbolo_jogador != 'X' and simbolo_jogador != 'O':
            simbolo_jogador = str(input('Escolha inválida. Por favor, digite novamente: '))

    # Atribui o símbolo da máquina de acordo com a escolha do jogador 1
    if simbolo_jogador == 'X':
        simbolo_maquina = 'O'
    else:
        simbolo_maquina = 'X'
    
    sleep(1) # espera 1s
    print('Muito bem. O computador jogará com {}'.format(simbolo_maquina))

    sleep(1) # espera 1s
    print('O jogo irá começar...') 
    sleep(1) # espera 1s
    for i in range(3):
        print('.')
        sleep(1) # espera 1s
    
    return simbolo_jogador, simbolo_maquina


# Defino uma função de atualização do tabuleiro
def atualiza_tabuleiro(A, p, simbolo_jogador):
    # Parâmetros de entrada
        # - A: Matriz do tabuleiro
        # - p: valor numérico da posição de 'alteração'
        # - simbolo_jogador : variável de tipo string contendo 'X' ou 'O' 
            # ( depende de cada escolha )
    
    # Parâmetros de saída
        # A função não retorna nenhum valor, apenas atualiza a matriz
        # 'A' do tabuleiro, substituindo a posição p por 'X' ou 'O' 
        # de acordo com a variável 'simbolo_jogador'
    # -------------------------------------------------------------

    # Nesse ponto não há segredo: basta atualizar a matriz A
    # de acordo com o mapeamento padrão de seus elementos
    if p == 1:
        A[0][0] = simbolo_jogador

    elif p == 2:
        A[0][1] = simbolo_jogador

    elif p == 3:
        A[0][2] = simbolo_jogador

    elif p == 4:
        A[1][0] = simbolo_jogador
    
    elif p == 5:
        A[1][1] = simbolo_jogador

    elif p == 6:
        A[1][2] = simbolo_jogador
    
    elif p == 7:
        A[2][0] = simbolo_jogador
    
    elif p == 8:
        A[2][1] = simbolo_jogador
    
    elif p == 9:
        A[2][2] = simbolo_jogador


# Defino uma função de verificação da condição de fechamento do jogo
def verifica_conclusao(A):
    # Parâmetros de entrada
        # - A: matriz do tabuleiro
        # - simbolo_jogador1: simbolo do jogador 1 ('X' ou 'O')
    
    # Valores de saída
        # x_completo: variável booleana auxiliar (True / False)
        # o_compelto: variável booleana auxiliar (True / False)
    # -------------------------------------------------------------
    Asize = len(A) # tamanho da matriz A
    x_completo = False # variável auxiliar
    o_completo = False # variável auxiliar

    # 1) Verifica preenchimento total de alguma linha
    for i in range(Asize): # para cada linha i
        cont_x = 0 # variável contadora
        cont_o = 0 # variável contadora

        # (ps.: essas variáveis auxiliares devem ser zeradas a cada coluna, pois para cada uma é um check diferente)

        for j in range(Asize): # para cada coluna j
            if A[i][j] == 'X': # verifica se o elemento é 'X'
                cont_x += 1 # incrementa a variável contadora

            elif A[i][j] == 'O': # verifica se o elemento é 'O'
                cont_o += 1 # incrementa a variável contadora
    
        # após a contagem DA LINHA I; verifica se 'X' ou 'O' contam 3 posições 
        if cont_x == 3:
            x_completo = True
            return x_completo, o_completo
    
        elif cont_o == 3:
            o_completo = True
            return x_completo, o_completo

    # 2) Preenchimento total de alguma coluna
    for j in range(Asize): # para cada coluna j
        cont_x = 0 # variável contadora
        cont_o = 0 # variável contadora

        # (ps.: essas variáveis auxiliares devem ser zeradas a cada coluna, pois para cada uma é um check diferente)

        for i in range(Asize): # para cada linha i
            if A[i][j] == 'X': # verifica se o elemento é 'X'
                cont_x += 1 # incrementa a variável contadora

            elif A[i][j] == 'O': # verifica se o elemento é 'O'
                cont_o += 1 # incrementa a variável contadora
    
        # após a contagem DA LINHA J, verifica se o 'X' ou o 'O' fechou 3 posições
        if cont_x == 3:
            x_completo = True
            return x_completo, o_completo

        elif cont_o == 3:
            o_completo = True
            return x_completo, o_completo


    # 3) Preenchimento total da diagonal principal
    cont_x = 0 # variável contadora
    cont_o = 0 # variável contadora
    for i in range(Asize):
        if A[i][i] == 'X': # verifica se o elemento é 'X'
            cont_x += 1 # incrementa a variável contadora

        elif A[i][i] == 'O': # verifica se o elemento é 'O'
            cont_o += 1 # incrementa a variável contadora
    
    # após a contagemm DA DIAGONAL PRINCIPAL, verifica se o 'X' ou o 'O' fechou 3 posições
    if cont_x == 3:
        x_completo = True 
        return x_completo, o_completo

    elif cont_o == 3:
        o_completo = True
        return x_completo, o_completo

    # 4) Preenchimento total da diagonal secundária
    cont_x = 0 # variável contadora
    cont_o = 0 # variável contadora
    for i in range(Asize):
        if A[i][(Asize-i)-1] == 'X':
            cont_x += 1

        elif A[i][(Asize-i)-1] == 'O':
            cont_o += 1

    # após a contagem DA DIAGONAL SECUNDÁRIA, verifica se o 'X' ou o 'O' fechou 3 posições
    if cont_x == 3:
        x_completo = True

    elif cont_o == 3:
        o_completo = True 

    # (não há um return dentro dos dois ifs acima, porque se as variáveis não forem retornadas em nenhuma das verificações anteriores,
    # elas obrigatoriamente têm que ser retornadas após a última verificação, feita pela diagonal secundária)
    return x_completo, o_completo


# Crio uma função que verifica se a escolha feita pelo jogador
# é válida
def verifica_escolha(p, A):
    # Parâmetros de entrada
        # - p: número de alguma das casas do tabuleiro mapeado
        # - A: matriz do tabuleiro do jogo

    # Valores de saída
        # - string 'vazia', se a casa não foi escolhida anteriormente
        # - string 'xxxxx', se a casa já foi escolhida anteriormente

    # ---------------------------------------------------

    if p == 1:
        if isstring(A[0][0]) == False:
            return 'vazia'
        else:
            return 'xxxxx'

    elif p == 2:
        if isstring(A[0][1]) == False:
            return 'vazia'
        else:
            return 'xxxxx'

    elif p == 3:
        if isstring(A[0][2]) == False:
            return 'vazia'
        else:
            return 'xxxxx'

    elif p == 4:
        if isstring(A[1][0]) == False:
            return 'vazia'
        else:
            return 'xxxxx'
    
    elif p == 5:
        if isstring(A[1][1]) == False:
            return 'vazia'
        else:
            return 'xxxxx'

    elif p == 6:
        if isstring(A[1][2]) == False:
            return 'vazia'
        else:
            return 'xxxxx'
    
    elif p == 7:
        if isstring(A[2][0]) == False:
            return 'vazia'
        else:
            return 'xxxxx'
    
    elif p == 8:
        if isstring(A[2][1]) == False:
            return 'vazia'
        else:
            return 'xxxxx'
    
    elif p == 9:
        if isstring(A[2][2]) == False:
            return 'vazia'
        else:
            return 'xxxxx'
    
    # trecho pensado especificamente para inclusão da gameplay contra o computador
    else:
        return 'xxxx'

# Defino uma função 'main secundária' (nenhuma entrada e nenhuma saída)
# que controla o game entre duas pessoas (multiplayer)
def jogo_vs_pessoa():
    # início do jogo
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
    simbolo_jogador1, simbolo_jogador2 = cadastra_jogadores_multiplayer() # cadastro de símbolos dos jogadores
    A = tabuleiro() # criação do tabuleiro do jogo
    jogador = 1 # variável auxiliar de controle de rodadas
    cont_rodadas = 0 # variável auxiliar contadora de rodadas
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 


    # loop de controle de turnos
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
    while cont_rodadas != 9:
        os.system('cls') # limpa o terminal
        cont_rodadas += 1 # incremento da variável contadora de rodadas


        # controle da jogada efetuada no turno
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x --
        apresenta_tabuleiro(A)
        if jogador == 1: # o jogador 1 joga
            p = int(input('Jogador 1, em qual casa você deseja inserir o {}: '.format(simbolo_jogador1))) # pega a posição da jogada
            if verifica_escolha(p, A) == 'vazia': # se não houver nenhum simbolo, faz a atualização
                atualiza_tabuleiro(A, p, simbolo_jogador1)

            else: # caso a posição escolhida ja tenha símbolo,
                while verifica_escolha(p, A) != 'vazia': # pausa o game até que seja feita uma escolha viável
                    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                atualiza_tabuleiro(A, p, simbolo_jogador1) 

                # loop alternativo de tratamento do valor p (mesma funcionalidade, mas com uma lógica diferente)
                #while True:
                #    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                #    if verifica_escolha(p, A) == 'vazia':
                #        atualiza_tabuleiro(A, p, simbolo_jogador1)
                #        break


        else: #elif jogador == -1: # o jogador 2 joga
            p = int(input('Jogador 2, em qual casa você deseja inserir o {}: '.format(simbolo_jogador2))) # pega a posição da jogada
            if verifica_escolha(p, A) == 'vazia': # se não houver nenhum simbolo, faz a atualização
                atualiza_tabuleiro(A, p, simbolo_jogador2)

            else: # caso a posição escolhida já tenha símbolo
                while verifica_escolha(p, A) != 'vazia': # pausa o game até que seja feita uma escolha viável
                    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                atualiza_tabuleiro(A, p, simbolo_jogador2) 

                # loop alternativo de tratamento do valor p (mesma funcionalidade, mas com uma lógica diferente)
                #while True: # pausa o game até que seja feita uma escolha viável
                #    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                #    if verifica_escolha(p, A) == 'vazia':
                #        atualiza_tabuleiro(A, p, simbolo_jogador2) 
                #        break
                    

        print('Turno finalizado!') # mensagem de finalização do turno
        sleep(2) # espera 2s
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x --


        # verifica se o jogo termina ou não
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
        x_completo, o_completo = verifica_conclusao(A) # verificação da condição de fechamento do jogo
        
        if x_completo == True: # verifica vitória do x
            os.system('cls')
            if simbolo_jogador1 == 'X':
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O JOGADOR 1 VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
            else:
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O JOGADOR 2 VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
                
        elif o_completo == True: # verifica vitória do o
            os.system('cls')
            if simbolo_jogador1 == 'O':
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O JOGADOR 1 VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
            else:
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O JOGADOR 2 VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 


        # atualiza o jogador para o turno seguinte
        jogador = jogador*(-1)
        
        #print('Turno finalizado!') # mensagem de finalização do turno
        #sleep(2) # espera 2s
    

    # atualização do jogo em caso de empate
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
    sleep(1) # espera 1s
    if cont_rodadas == 9: # se a quantidade de rodadas é 9
        os.system('cls') # limpa o terminal
        apresenta_tabuleiro(A)
        print('{:^138}'.format('!!! DEU VELHA !!! É UM EMPATE !!!')) # mensagem de conclusão do game


# Defino uma função 'main secundária' (nenhuma entrada e nenhuma saída)
# que controla o game entre pessoa e máquina (single player)
def jogo_vs_maquina():
    # início do jogo
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
    simbolo_jogador, simbolo_maquina = cadastra_jogador_singleplayer() # cadastro de símbolos do jogador e da máquina
    A = tabuleiro() # criação do tabuleiro do jogo
    jogador = 1 # variável auxiliar de controle de rodadas
    cont_rodadas = 0 # variável auxiliar contadora de rodadas
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x --

    # loop de controle de turnos
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
    while cont_rodadas != 9:
        os.system('cls') # limpa o terminal
        cont_rodadas += 1 # incremento da variável contadora de rodadas


        # controle da jogada efetuada no turno
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x --
        apresenta_tabuleiro(A)
        if jogador == 1: # o jogador joga
            p = int(input('Jogador, em qual casa você deseja inserir o {}: '.format(simbolo_jogador))) # pega a posição da jogada
            if verifica_escolha(p, A) == 'vazia': # se não houver nenhum simbolo, faz a atualização
                atualiza_tabuleiro(A, p, simbolo_jogador)

            else: # caso a posição escolhida ja tenha símbolo,
                while verifica_escolha(p, A) != 'vazia': # pausa o game até que seja feita uma escolha viável
                    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                atualiza_tabuleiro(A, p, simbolo_jogador) # atualização do

                # loop alternativo de tratamento do valor p (mesma funcionalidade, mas com uma lógica diferente)
                #while True:
                #    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                #    if verifica_escolha(p, A) == 'vazia':
                #        atualiza_tabuleiro(A, p, simbolo_jogador1)
                #        break


        else: # a máquina joga
            p = r.randint(1,9) # pega a posição da jogada
            if verifica_escolha(p, A) == 'vazia': # se não houver nenhum simbolo, faz a atualização
                atualiza_tabuleiro(A, p, simbolo_maquina)

            else: # caso a posição escolhida já tenha símbolo
                while verifica_escolha(p, A) != 'vazia': # pausa o game até que seja feita uma escolha viável
                    p = r.randint(1,9)
                atualiza_tabuleiro(A, p, simbolo_maquina) 

                # loop alternativo de tratamento do valor p (mesma funcionalidade, mas com uma lógica diferente)
                #while True: # pausa o game até que seja feita uma escolha viável
                #    p = int(input('Essa casa já foi escolhida. Faça uma escolha válida: '))
                #    if verifica_escolha(p, A) == 'vazia':
                #        atualiza_tabuleiro(A, p, simbolo_jogador2) 
                #        break

            print('O computador irá inserir o {} na casa {}'.format(simbolo_maquina, p))
            sleep(4) 

        print('Turno finalizado!') # mensagem de finalização do turno
        sleep(2) # espera 2s
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x --


        # verifica se o jogo termina ou não
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
        x_completo, o_completo = verifica_conclusao(A) # verificação da condição de fechamento do jogo
        
        if x_completo == True: # verifica vitória do x
            os.system('cls')
            if simbolo_jogador == 'X':
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O JOGADOR VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
            else:
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O COMPUTADOR VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
                
        elif o_completo == True: # verifica vitória do o
            os.system('cls')
            if simbolo_jogador == 'O':
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O JOGADOR 1 VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
            else:
                apresenta_tabuleiro(A)
                sleep(1) # espera 1s
                print('{:^138}'.format('!!! O COMPUTADOR VENCEU !!!')) # mensagem de conclusão do game
                break # quebra do loop
        # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 


        # atualiza o jogador para o turno seguinte
        jogador = jogador*(-1)
        
        #print('Turno finalizado!') # mensagem de finalização do turno
        #sleep(2) # espera 2s
    

    # atualização do jogo em caso de empate
    # -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- -- x -- x -- 
    sleep(1) # espera 1s
    if cont_rodadas == 9: # se a quantidade de rodadas é 9
        os.system('cls') # limpa o terminal
        print('{:^138}'.format('DEU VELHA !!! É UM EMPATE !!!')) # mensagem de conclusão do game


# Script principal de execução
def main():
    os.system('cls') # limpa o terminal
    print('Você deseja jogar contra um amigo (A) ou contra a máquina (M)? ')
    resp = str(input('Sua resposta [A / M]: ')) # escolha do tipo de game

    # tratamento resposta
    while resp != 'A' and resp != 'M':
        resp = str(input('Comando desconhecido... Insira sua resposta novamente [A / M]: '))

    sleep(1)
    print('Iniciando ...')
    sleep(1)
    for i in range(3):
        print('.')
        sleep(1)

    os.system('cls')    
    if resp == 'A':
        jogo_vs_pessoa()
    else:
        jogo_vs_maquina()
    
main()    