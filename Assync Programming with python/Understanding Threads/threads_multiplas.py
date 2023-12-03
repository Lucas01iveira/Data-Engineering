import threading
import time 

def main():


    threads = [
        threading.Thread(target=contar, args=('elefante', 10)),
        threading.Thread(target=contar, args=('moeda', 32)),
        threading.Thread(target=contar, args=('bilhete', 22)),
        threading.Thread(target=contar, args=('caneta', 13))
    ]

    for th in threads:
        th.start() 

    print('\nPodemos fazer outras coisas enquanto a thread é executada')
    print('Teste ' * 2)

    for th in threads:
        th.join() 

    print('Pronto! ') 

def contar(o_que, numero):
    for n in range(1, numero+1):
        print('{} {}(s)'.format(n, o_que))
        time.sleep(1)

if __name__ == '__main__':
    main()
