#from codigo.bytebank import Funcionario
from bytebank import Funcionario

# lucas = Funcionario(nome= 'Lucas', data_nascimento= 2000, salario= 1000)
# print(lucas.idade())

def teste_idade():
    funcionario_teste = Funcionario(nome= 'Lucas', data_nascimento= '05/11/2001', salario= 1200)
    print('Teste: {}'.format(funcionario_teste.idade()))

teste_idade()