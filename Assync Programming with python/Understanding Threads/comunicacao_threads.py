from threading import Thread
from queue import Queue

from time import sleep
import colorama

def gerador_de_dados(queue):
    for i in range(1,11):
        print(colorama.Fore.GREEN + 'Dado {} gerado.'.format(i))
        sleep(1)
        queue.put(i) # insiro o dado na queue de execucao

def consumidor_de_dados(queue):
    while queue.qsize() > 0: # enquanto a quantidade de itens na queue de exeução for maior que 0 (i.e., enquanto houverem elementos lá dentro)
        valor = queue.get() # recupero um dado da queue
        print(colorama.Fore.RED + 'Dado {} processado'.format(valor))
        sleep(1)
        queue.task_done() # uma vez que o dado foi processado, encerro o item de queue
print('teste')
'''
if __name__ == '__main__':
    print(colorama.Fore.WHITE + 'Sistema iniciado')
    queue = Queue() # gerando uma instância da classe Queue (fila de execução)

    # gerando instância das threads com base nas funções de geração/consumo de dados

    th1 = Thread(target=gerador_de_dados, args=(queue,)) 
    # o parâmetro args deve receber uma tupla; devemos nesse caso incluir uma vírgula após a passagem do objeto queue para deixar claro que se trata de uma tupla com um único elemento
    
    th2 = Thread(target=consumidor_de_dados, args=(queue,))
    # o parâmetro args deve receber uma tupla; devemos nesse caso incluir uma vírgula após a passagem do objeto queue para deixar claro que se trata de uma tupla com um único elemento

    # Atenção! Precisamos terminar de gerar todos os dados antes de começar a processá-los, portanto a thread1 deve ser finalizada por completo antes que a thread2 inicie (por isso a inclusão do método join() logo após a disponibilização da thread na pool de execuções)

    # como até o momento só temos a thread principal e a th1, temos certeza de que ela será processada imediatamente, logo a inclusão do join() força o processo a aguardar o encerramento da th1 antes de prosseguir;
    th1.start()
    th1.join()

    # seria incorreto, por exemplo, incluir a thread2 na pool antes de encerrar a th1

    th2.start()
    th2.join()
'''