import threading 
import time

def processar():
    print('[', end='', flush=True)
    # o flush não espera toda a execução terminar para efetuar a impressão; quando a flag é True, assim que o comando print é chamado a imporessão na tela é feita

    for _ in range(1,11):
        print('#', end='', flush=True)
        time.sleep(1)

    print(']', end='', flush=True)

if __name__ == '__main__':
    ex = threading.Thread(target=processar)

    ex.start()
    ex.join()