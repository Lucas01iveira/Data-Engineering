import multiprocessing 
import time

# from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor

def processar():
    print('[', end='', flush=True)

    for _ in range(1,11):
        print('#', end='', flush=True)
        time.sleep(1)

    print(']', end='', flush=True)

    return 43
if __name__ == '__main__':
    with Executor() as executor: # abrindo um contexto
        future = executor.submit(processar) # enviando a função 'processar' para o executor de processos
    
    print('O retorno foi {}'.format(future.result()))