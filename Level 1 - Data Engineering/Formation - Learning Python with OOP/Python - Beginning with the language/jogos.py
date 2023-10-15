import os
from time import sleep
import adivinhacao
import forca

# Cabeçalho de apresentação da interface de aplicativos
print('-'*35)
print('Escolha o seu jogo!')
print('-'*35)
print()

# seleciona todos os arquivos de jogos incluídos no path correspondente
games_list = os.listdir(r'C:\Users\LUCAS\Documents\Data Engineering\Data-Engineering\Level 1 - Data Engineering\Formation - Learning Python with OOP\Python - Beginning with the language')
indexes_list = [] # lista auxiliar para armazenar os índices de games (pode mudar de acordo com a criação / exlusão de aplicações)
print('- x - x '*4, end='')
print('-')

for index_game, game in enumerate(games_list):
    if (game != 'jogos.py') and (game != 'teste.py') and (game != '__pycache__'):
        print(f'{index_game} - {game.replace(".py","").upper()}')
        indexes_list.append(str(index_game))
        sleep(1)

print('- x - x '*4, end='')
print('-')

# obtenho a resposta do jogador e incluo um loop de validação
index_resposta = input('Qual jogo você gostaria de jogar? Digite o número correspondente: ')
if index_resposta not in indexes_list:
    while index_resposta not in indexes_list:
        index_resposta = input('Reposta incorreta. Por favor, digite novamente: ')

print()

# de acordo com a resposta fornecida, efetuo um import das aplicações (esse trecho não tem como ser parametrizado)
# sempre que uma nova aplicação chegar, esse trecho do código teria de ser ajustado.
if (index_resposta == '0'): # Jogo da adivinhação
    print('Inicializando o jogo da adivinhacao',end='')
    for i in range(3):
        if (i == 2):
            print('.')
        else:
            print('.',end='')
        sleep(1)
    adivinhacao.inicializar_jogo()

elif (index_resposta == '1'): # Jogo da forca
    print('Inicializando o jogo da forca',end='')
    for i in range(3):
        if (i == 2):
            print('.')
        else:
            print('.',end='')
        sleep(1)

    forca.inicializar_jogo()    
