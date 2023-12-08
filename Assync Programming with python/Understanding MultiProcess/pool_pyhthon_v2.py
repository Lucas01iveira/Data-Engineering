import multiprocessing

def calcular(dado):
    return dado ** 2

def imprimir_nome_processo():
    print('Iniciando processo com nome {}'.format(multiprocessing.current_process().name))

def main():

    # definindo a pool de processos de acordo com a quantidade de cores do meu cpu
    tamanho_pool = multiprocessing.cpu_count()*2 

    print(f'Tamanho da pool: {tamanho_pool}')

    # definindo o objeto Pool (quantidade de processos a serem gerados) de acordo com a quantidade de cores do nosso processador
    pool = multiprocessing.Pool(processes=tamanho_pool, initializer=imprimir_nome_processo)
    
    # parâmetro initializer define qual função será executada para cada processo que for criado

    entradas = list(range(7))
    saidas = pool.map(calcular, entradas) # qual função será trabalhada pela pool e suas 'entradas' (parâmetros)

    pool.close() # sinaliza que os processos da pool podem ser executados
    pool.join() # sinaliza que o código não deve prosseguir até que os processos em execução sejam finalizados

    print(f'Saídas: {saidas}')

if __name__ == '__main__':
    main()