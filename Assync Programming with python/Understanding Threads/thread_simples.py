import threading
import time 

def main():

    # gerando uma instância de thread (i.e., um objeto da classe Thread)

    th = threading.Thread(target=contar, args=('elefante', 10))
    # parâmetro target -> função que será executada
    # parâmetro args -> tupla de parâmetros que a função targer precisa para funcionar

    th.start() # inclui a instância criada na pool de threads do processo em execução (NÃO CONFUNDIR COM A CHAMADA DE EXECUÇÃO DESSA THREAD; o próprio python define quando ela será inicializada)

    print('\nPodemos fazer outras coisas enquanto a thread é executada')
    print('Teste ' * 2)

    th.join() # impõe que o processo de execução do programa não deve continuar até que a execução dessa thread seja finalizada

    print('Pronto! ') 

def contar(o_que, numero):
    for n in range(1, numero+1):
        print('{} {}(s)'.format(n, o_que))
        time.sleep(1)

if __name__ == '__main__':
    main()

'''
Obs.:

- No caso desse programa em particular, como temos 2 threads simples apenas (a principal, vinculada ao processo de execução do código fonte, e auxiliar, definida manualmente por nós), o pytho julga que não há porque esperar e já coloca a thread auxiliar para ser executada assim que o programa começa. É por isso que vemos o primeiro print da função 'contar' aparecendo rapidamente em conjunto com os prints incluídos após a inicialização.

- Somente quando o processo de execução (vinculado à thread principal) chega à especificação do método join() é que ele para a execução principal e segura o processo até que a thread auxiliar seja finalizada.
'''