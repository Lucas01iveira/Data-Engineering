# definição da classe de objetos (receita)
class Conta:
    
    # self = endereçamento do objeto na memória do computador;
    #    é criado automaticamente pelo python quando a classe é instanciada em alguma variável

    # função construtora
    def __init__(self, numero, titular, saldo, limite):
        
        print('Construindo o objeto da classe em.. {}'.format(self))

        # atribuição das características da classe (i.e., dos objetos que serão criados)
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        # uma vez que eu digito "self.<atributo>", já estou informado para o python que o atributo
        # em questão pertence AO OBJETO que acabou de ser criado.
    
    # função relativa aos objetos dessa classe (método): consulta extrato
    def extrato(self):
        print('A conta do titular {} possui {} de saldo'.format(self.titular, self.saldo)) 

    # função relativa aos objetos dessa classe (método): deposita dinheiro
    def deposita(self, valor):
        if (self.saldo + valor <= self.limite):
            self.saldo += valor
        else:
            print('Você não pode depositar a quantia de {}, pois o seu saldo final irá ultrapassar o limite máximo permitido de {}'.format(valor, self.limite))
        
    # função relativa aos objetos dessa classe (método): saca dinheiro
    def saca(self, valor):
        if (self.saldo - valor >= 0):
            self.saldo -= valor
        else:
            print('Você não pode sacar a quantia de {}, pois o seu saldo final ficará negativo'.format(valor))
    
