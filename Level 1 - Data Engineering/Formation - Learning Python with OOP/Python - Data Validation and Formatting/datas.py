from datetime import datetime, timedelta

class Data:
    def __init__(self):
        self.momento_cadastro = datetime.now()

    def mes_cadastro(self):
        meses_do_ano = [
            'Janeiro', 'Fevereiro', 'Março', 'Abril',
            'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
            'Outubro', 'Novembro', 'Dezembro'
        ]
        index_mes_atual = self.momento_cadastro.month-1

        return meses_do_ano[index_mes_atual]

    def dia_cadastro(self):
        dias_da_semana = [
            'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
            'Quinta-Feira', 'Sexta-Feira', 'Sábado', 'Domingo'
        ]
        index_dia_atual = self.momento_cadastro.weekday()
        
        return dias_da_semana[index_dia_atual]