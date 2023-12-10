import multiprocessing
import time

# script criado com o propósito de provar que, realmente, a não ser que nada seja 'forçado' de maneira direta, dois processos/threads distintos nunca compartilham recursos entre si

def funcao1(val, stat):
    if stat:
        res = val+10
        stat = False
    else:
        res = val+20
        val = 200
        stat = True

    print('O resultado da funcao 1 é {}'.format(res))
    time.sleep(0.001)

def funcao2(val, stat):
    if stat:
        res = val+30
        stat = False
    else:
        res = val+40
        val = 400
        stat = True 
    
    print('O resultado da funcao 2 é {}'.format(res))
    time.sleep(0.001)

def main():
    status = False
    valor = 100

    # da maneira que estamos definindo, status e valor são variáveis dispostas em um local fixo da memória, de modo que o processo 1 executa a função 1 com os valores inicializados e o processo 2 executa a função 2 também com os mesmos valores inicializados
    
    # do ponto de vista de implementação da função, é isso o que acontece: as variáveis status e valor não estão sendo modificadas por cada processo

    p1 = multiprocessing.Process(target= funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target= funcao2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()