import multiprocessing

def depositar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value+1

def sacar(saldo):
    for _ in range(10_000):
        saldo.value = saldo.value-1

def realizar_transacoes(saldo):
    pc1 = multiprocessing.Process(target=depositar, args=(saldo,))
    pc2 = multiprocessing.Process(target=sacar, args=(saldo,))

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()

if __name__ == '__main__':
    saldo = multiprocessing.Value('i', 100)
    print('Saldo inicial: {}'.format(saldo.value))

    for _ in range(10):
        realizar_transacoes(saldo)
    
    print('Saldo final: {}'.format(saldo.value))