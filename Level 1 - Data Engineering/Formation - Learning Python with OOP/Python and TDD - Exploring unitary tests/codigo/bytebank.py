from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    @property
    def data_nascimento(self):
        return self._data_nascimento

    def idade(self):
        data_nasc_split = self._data_nascimento.split('/')
        ano_nasc = data_nasc_split[-1]
        ano_atual = date.today().year
        return ano_atual - int(ano_nasc)

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor
    
    def sobrenome(self):
        nome_split = self._nome.split(' ')
        return nome_split[-1]

    def _eh_socio(self):
        sobrenomes = [
            'Bragança'
            ,'Windsor'
            ,'Bourbon'
            ,'Yamato'
            ,'Al Saud'
            ,'Khan'
            ,'Tudor'
            ,'Ptolomeu'
        ]

        # if self._salario >= 100000 and (self.sobrenome() in sobrenomes):
        #     return True
        # else:
        #     return False

        # jeito "pythônico" de representar os condicionais anteriores de maneira mais direta e enxuta
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes)

    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = 0.1*self._salario
            self._salario = self._salario - decrescimo

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salário é muito alto para receber um bônus.')
        return valor
    
    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'