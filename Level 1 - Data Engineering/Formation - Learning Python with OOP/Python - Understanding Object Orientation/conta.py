# definição da classe de objetos (receita)
class Conta:
    
    # self = endereçamento do objeto na memória do computador;
    #    é criado automaticamente pelo python quando a classe é instanciada em alguma variável

    # __init__ = função construtora
    def __init__(self, numero, titular, saldo, limite):
        
        # atribuição das características da classe (i.e., dos objetos que serão criados)
        
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

        # uma vez que eu digito "self.<atributo>", já estou informado para o python que o atributo
        # em questão pertence AO OBJETO que acabou de ser criado.