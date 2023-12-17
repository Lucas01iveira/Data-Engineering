from datetime import datetime
import math as m 

import cProfile
import pstats
import io
from pstats import SortKey

def main():
    inicio = datetime.now()
    computar(50*10E6)
    fim = datetime.now()

    tempo = fim - inicio
    print('Execução terminou em {:.2f} segundos'.format(tempo.total_seconds()))


def computar(fim):
    pos = 1 
    fator = 1000 * 1000
    while pos < fim:
        m.sqrt( (pos - fator)*(pos - fator) )
        pos += 1

if __name__ == '__main__':
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    profiler.dumpstats

# Resultado: Execução terminou em 189.12 segundos 