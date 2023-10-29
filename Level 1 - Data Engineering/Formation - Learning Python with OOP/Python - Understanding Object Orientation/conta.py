# definição da classe de objetos (receita)
class Conta:
    
    # self = endereçamento do objeto na memória do computador;
    #    é criado automaticamente pelo python quando a classe é instanciada em alguma variável

    # função construtora
    def __init__(self, numero, titular, saldo, limite):
        # sempre é possível definir parâmetros opcionais, implementando a sintaxe def __init__ (self, .. , <param_opcional> = <valor_default>)
        # desse modo, caso o parâmetro não seja informado no momento da definição do objeto, o valor default será atribuído.
        
        print('Construindo o objeto da classe em.. {}'.format(self))

        # atribuição das características da classe (i.e., dos objetos que serão criados)
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

        # uma vez que eu digito "self.<atributo>", já estou informado para o python que o atributo em questão pertence AO OBJETO que acabou de ser criado.

        # sempre que o prefixo "__" é incluído antes da chamada do atributo, estamos impondo que esse atributo seja do tipo "privado"; ou seja, mesmo que o programador tente acessá-los a manipulá-los diretamente com auxílio da sintaxe <ref_objeto>._<Classe>__<atributo>, esse padrão de nomenclatura já torna explícito o fato de que esse atributo deve ser alterado / acessado somente através dos métodos da classe

    
    # função relativa aos objetos dessa classe (método): consulta extrato
    def extrato(self):
        print('A conta do titular {} possui {} de saldo'.format(self.__titular, self.__saldo)) 

    # função relativa aos objetos dessa classe (método): deposita dinheiro
    def deposita(self, valor):
        if (self.__saldo + valor <= self.__limite):
            self.__saldo += valor
        else:
            print('Você não pode depositar a quantia de {}, pois o seu saldo final irá ultrapassar o limite máximo permitido de {}'.format(valor, self.__limite))
        
    # função relativa aos objetos dessa classe (método): saca dinheiro
    def saca(self, valor):
        if (self.__saldo - valor >= 0):
            self.__saldo -= valor
        else:
            print('Você não pode sacar a quantia de {}, pois o seu saldo final ficará negativo'.format(valor))
    
    # mfunção relativa aos objetos dessa classe (método): transfere dinheiro
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # método "getter" para consultar o número da conta
    def get_numero(self):
        return self.__numero

    # método "getter" para consultar o limite da conta 
    @property
    def limite(self):
        return self.__limite
    
    # método "getter" para consultar o saldo da conta
    @property
    def saldo(self):
        return self.__saldo

    # método "getter" para consultar o titular da conta
    @property
    def titular(self):
        return self.__titular
    
    # método "setter" para ajustar o limite da conta
    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite
