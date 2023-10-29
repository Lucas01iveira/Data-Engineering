# Desafio extra lançado durante o treinamento para prática dos novos conceitos

# inicializo a construção da classe
class Data:

    # efetuo a chamada da função construtura do objeto e defino os atributos correspondentes
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    # defino o método de formatação da data
    def formatada(self):

        # faço verificações de dia / mês para checar se o número informado possui apenas um dígito e, nesses casos, aplico uma formatação na string de saída para que a saída fique no padrão usual

        if ( len( str(self.dia) ) == 1 ):
            if ( len( str(self.mes) ) == 1 ):
                print(f'{'0'+str(self.dia)}/{'0'+str(self.mes)}/{self.ano}')
            else:
                print(f'{'0'+str(self.dia)}/{self.mes}/{self.ano}')

        else:
            
            if ( len( str(self.mes) ) == 1 ):
                print(f'{self.dia}/{'0'+str(self.mes)}/{self.ano}')
            else:
                print(f'{self.dia}/{self.mes}/{self.ano}')


