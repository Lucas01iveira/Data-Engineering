from codigo.bytebank import Funcionario

class Test_Class:
    # para o framework pytest funcionar corretamente, o padrão de nomenclatura deve ser sempre 'test_<string>'

    # além disso, recomenda-se que os nomes dos métodos de teste sejam os mais explícitos e claros possíveis em relação à funcionalidade que está sendo testada

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
    
    def test_se_1000_eh_igual_a_1001_menos_1(self):
        # Given
        referencia = 1000
        outro_numero = 1001

        # When
        resultado = outro_numero-1

        # Then
        assert referencia == resultado
    
    def test_se_1000_eh_igual_a_2000_menos_500(self):
        # Given
        referencia = 1000
        outro_numero = 2000

        # When
        resultado = outro_numero-500

        # Then
        assert referencia == resultado

class TestAvulso:
    def test_se_A_eh_igual_a_A(self):
        texto1 = 'A'
        texto2 = 'A'

        assert texto1 == texto2