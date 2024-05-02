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

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'