from datetime import datetime
import math as m 

import threading
import multiprocessing

def main():
    qtd_cores = multiprocessing.cpu_count()
    print('Realizando o processamento matemático cm {} core(s)'.format(qtd_cores))

    inicio = datetime.now()

    threads = []
    for n in range(1, qtd_cores+1):
        pos_inic = 50_000_000 * (n-1)/qtd_cores
        pos_fin = 50_000_000 * n/qtd_cores
        print('Core {} processando de {} até {}'.format(n, pos_inic, pos_fin))
        threads.append(threading.Thread(target=computar, kwargs={'inicio':pos_inic, 'fim':pos_fin},daemon=True))

    [th.start() for th in threads]
    [th.join() for th in threads]

    fim = datetime.now()
    tempo = fim - inicio
    print('Execução terminou em {:.2f} segundos'.format(tempo.total_seconds()))


def computar(fim, inicio= 1):
    pos = inicio 
    fator = 1000 * 1000
    while pos < fim:
        m.sqrt( (pos - fator)*(pos - fator) )
        pos += 1

if __name__ == '__main__':
    main()


# Resultado: Execução terminou em 20.52 segundos 