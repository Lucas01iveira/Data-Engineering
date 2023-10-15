from time import sleep

def inicializar_jogo():
    # Cabeçalho de apresentação do mini-game
    sleep(1)
    print('-'*35)
    print('Bem vindo(a) ao jogo da forca!')
    print('-'*35)
    print()

# A variável __name__ é definida sempre que um arquivo python é executado;
# se esse arquivo é executado diretamente pelo prompt de comando (como um arquivo python "principal),
# então queremos que o código dentro dele seja executado automaticamente. Daí a relevância do if abaixo

if (__name__ == '__main__'):
    inicializar_jogo()