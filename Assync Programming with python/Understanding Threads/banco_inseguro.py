import threading 
import random
import time
from typing import List

class Conta:

    def __init__(self, saldo=0) -> None:
        self.saldo = saldo

def servicos(contas, total):
    for _ in range(1, 5_000): # o _ do for representa apenas um índice; poderia ser qualquer caractere
        c1, c2 = pega_duas_contas(contas)
        valor = random.randint(1, 100)
        transferir(c1, c2, valor)
        valida_banco(contas, total)


def criar_contas() -> List[Conta]: # sintaxe que indica o que a função vai retornar (possível devido ao uso do módulo typing)
    return [
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000)),
        Conta(saldo=random.randint(5_000, 10_000))
    ]

def transferir(origem: Conta, destino: Conta, valor: int):
    if origem.saldo < valor:
        return 
    else:
        origem.saldo -= valor
        time.sleep(0.001)
        destino.saldo += valor

def valida_banco(contas: List[Conta], total: int):
    atual = sum(conta.saldo for conta in contas)
    
    if atual != total:
        print('ERRO: Balanço bancário inconsistente. BRLs {:.2f} vs {:.2f}'.format(atual, total))
    else:
        print('Tudo certo! Balanço bancário consistente: BRLs {:.2f}'.format(total))

def pega_duas_contas(contas):
    c1 = random.choice(contas)
    c2 = random.choice(contas)

    # tratamento para evitar pegar contas iguais
    while c1 == c2:
        c2 = random.choice(contas)
    
    return c1, c2

def main():
    contas = criar_contas()
    total = sum(conta.saldo for conta in contas)
    print('Inciando transferências...')

    # quando somente uma thread é executada, não temos problema
    tarefas = [
        threading.Thread(target=servicos, args=(contas, total))
    ]

    # mas quando mais de uma thread atua nos códigos em questão, passamos a ter um problema de 'race condition', em que as threads utilizam as mesmas funções /dados que podem ter sido alterados por outras threads antes de cada execução
    tarefas = [
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total)),
        threading.Thread(target=servicos, args=(contas, total))
    ]

    [tarefa.start() for tarefa in tarefas]
    [tarefa.join() for tarefa in tarefas]

    print('Transferências completas.')
    valida_banco(contas, total)

if __name__ == '__main__':
    main()