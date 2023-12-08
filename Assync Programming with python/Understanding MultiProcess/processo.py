import multiprocessing

def faz_algo(valor):
    print('Fazendo algo com o {}'.format(valor))

def main():
    print('Iniciando o processo com nome: {}'.format(multiprocessing.current_process().name))

    pc = multiprocessing.Process(target= faz_algo, args=('Pássaro',))

    print('Iniciando o processo com nome: {}'.format(pc.name))

    pc.start() # coloca o processo definido numa pool de execução
    pc.join() # sinaliza que o código só pode avançar quando o trecho de código avaliado pelo multiprocess for finalizado

if __name__ == '__main__':
    main()