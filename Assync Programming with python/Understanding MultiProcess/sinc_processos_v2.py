import multiprocessing

# código criado com o intuito de resolver o problema das race conditions identificado no script anterior

def depositar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value+1

def sacar(saldo, lock):
    for _ in range(10_000):
        with lock:
            saldo.value = saldo.value-1

def realizar_transacoes(saldo, lock):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo,lock))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo,lock))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()

if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)
    print('Saldo inicial: {}'.format(saldo.value))

    lock = multiprocessing.RLock() # sempre o RLock, porque ele não trava o código caso tenhamos algum erro durante a execução de um processo dentro do lock statement

    # não podemos deixar que os processos acessem nossa variável de maneira *dessincronizada*, ou seja, a qualquer momento, então o objeto lock nos ajuda exatamente nesse ponto: sempre que um processo estiver executando alguma modificação no atributo, os demais aguardam

    for _ in range(10):
        realizar_transacoes(saldo, lock)
    
    print('Saldo final: {}'.format(saldo.value))