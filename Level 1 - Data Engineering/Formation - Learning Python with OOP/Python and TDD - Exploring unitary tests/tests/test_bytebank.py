from codigo.bytebank import Funcionario
import pytest

class Test_Class:
    # para o framework pytest funcionar corretamente, o padrão de nomenclatura deve ser sempre 'test_<string>'

    # além disso, recomenda-se que os nomes dos métodos de teste sejam os mais explícitos e claros possíveis em relação à funcionalidade que está sendo testada

    @pytest.mark.skip
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given - Contexto
        entrada = '05/11/2001'
        saida_esperada = 23
        funcionaro_test = Funcionario('Teste', entrada, 1111)

        # When - Ação
        # (nesse caso: dadas a entrada e o novo cadastro de funcionário, a ação corresponde à chamada do método de cálculo de idade)
        resultado = funcionaro_test.idade() 

        # Then - Desfecho
        assert resultado == saida_esperada
    
    def test_se_sobrenome_esta_correto(self):
        
        # given (dados os parâmetros...)
        nome_entrada = 'Lucas Oliveira'
        sobrenome = 'Oliveira'

        # when (quando a classe é instanciada...)
        teste = Funcionario(nome_entrada, '05/11/2001', 1000)

        # then (então verifico...)
        assert sobrenome == teste.sobrenome()

    def test_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada = 100000 # given
        esperado = 90000
        entrada_nome = 'Paulo Bragança'

        funcionario_teste = Funcionario(entrada_nome, '11/11/2000', entrada)

        funcionario_teste.decrescimo_salario() #when
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # given
        entrada = 1000 
        esperado = 100
        funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

        # when
        resultado = funcionario_teste.calcular_bonus()

        # then
        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000_deve_retornar_exception(self):

        with pytest.raises(Exception):
            # given
            entrada = 100000 
            funcionario_teste = Funcionario('Teste', '11/11/2000', entrada)

            # when
            resultado = funcionario_teste.calcular_bonus()

            # then
            assert resultado 
            
    @pytest.mark.skip
    def test_se_1000_eh_igual_a_1001_menos_1(self):
        # Given
        referencia = 1000
        outro_numero = 1001

        # When
        resultado = outro_numero-1

        # Then
        assert referencia == resultado
    
    # def test_se_1000_eh_igual_a_2000_menos_500(self):
    #     # Given
    #     referencia = 1000
    #     outro_numero = 2000

    #     # When
    #     resultado = outro_numero-500

    #     # Then
    #     assert referencia == resultado

#@pytest.mark.skip(reason='o bloco abaixo representa apenas uma tentativa de entender o módulo pytest')
@pytest.mark.skipif(condition= 1 == 1, reason='Se 1 for igual a 1, não executo esse teste')
class TestAvulso:
    def test_se_A_eh_igual_a_A(self):
        texto1 = 'A'
        texto2 = 'A'

        assert texto1 == texto2
    
    def test_se_B_eh_igual_a_B(self):
        texto1 = 'B'
        texto2 = 'B'

        assert texto1 == texto2
    
    def test_se_V_eh_igual_a_B(self):
        texto1 = 'V'
        texto2 = 'B'

        assert texto1 == texto2