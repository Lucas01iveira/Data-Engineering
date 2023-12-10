import multiprocessing

# função 1 (recebe uma conexão como parâmetro)
def ping(queue):
    queue.put('Geek')

# função 2 (recebe outra conexão como parâmetro)
def pong(queue):
    msg = queue.get() # recebendo a informação da connection (receiver)
    print(f'{msg} University')

def main():

    queue = multiprocessing.Queue() 
    # True -> ambos os lados do pipe podem enviar e receber informação
    # False -> um lado pode apenas enviar e o outro apenas receber

    p1 = multiprocessing.Process(target=ping, args=(queue,))
    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()