import multiprocessing
import time
import ctypes

# esse código, por outro lado, tem o propósito de forçar o compartilhamento de estados (variáveis/atributos/recursos) entre processos e ilustrar o funcionamento do fluxo

def funcao1(val, stat):
    if stat.value:
        res = val.value+10
        stat.value = False
    else:
        res = val.value+20
        val.value = 200
        stat.value = True

    print('O resultado da funcao 1 é {}'.format(res))
    time.sleep(0.001)

def funcao2(val, stat):
    if stat.value:
        res = val.value+30
        stat.value = False
    else:
        res = val.value+40
        val.value = 400
        stat.value = True 
    
    print('O resultado da funcao 2 é {}'.format(res))
    time.sleep(0.001)

def main():
    status = multiprocessing.Value(ctypes.c_bool, False) # defino uma variável value do tipo c_bool (interface com C), inicializado com valor False
    valor = multiprocessing.Value('i', 100) # defino uma variável value do tipo int, inicializada com o valor 100

    # a definição dos objetos Value impõe que, agora, essas variáveis estão sendo armazenadas em um ponto da memória do computador que pode ser acessado/modificado por um processo e, depois disso, outro processo pode acessar essas mesmas variáveis e utilizar seus valores;
    # além dessa definição, para que o compartilhamento aconteça corretamente as funções devem ser modificadas para que os parâmetros de recebimento acessem diretamente o atributo value das variáveis fornecidas (agora vistas como objetos)

    p1 = multiprocessing.Process(target= funcao1, args=(valor, status))
    p2 = multiprocessing.Process(target= funcao2, args=(valor, status))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()