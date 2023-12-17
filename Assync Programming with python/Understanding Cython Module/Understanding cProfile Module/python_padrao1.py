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
    profiler.dump_stats(r'C:\Users\LUCAS\Documents\Data Engineering\Data-Engineering\Assync Programming with python\Understanding Cython Module\Understanding cProfile Module\python_padrao1.stats') # geração de arquivo binário com os status

    # geração das estatísticas
    sec = io.StringIO()
    sortBy = SortKey.TIME # ordenamento das estatísticas por tempo de execução

    # apresentando os stats dentro do próprio terminal de execução
    ps = pstats.Stats(profiler, stream=sec).sort_stats(sortBy)
    ps.print_stats()
    print(sec.getvalue())

    # Para visualizar o arquivo .stats gerado, devemos chamar o snakeviz no terminal da seguinte maneira: 
    # python -m snakeviz python_padrao1.stats --server

    # em seguida, basta acessar o link gerado

# Resultado: Execução terminou em 189.12 segundos 