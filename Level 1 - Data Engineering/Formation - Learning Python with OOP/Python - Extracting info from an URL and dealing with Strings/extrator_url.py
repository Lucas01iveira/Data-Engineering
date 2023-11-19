import re

class ExtratorUrl:

    def __init__(self, url):
        self.__url = self.sanitiza_url(url)
        self.valida_url_melhorada() 

    def sanitiza_url(self, texto_url):
        if type(texto_url) == str:
            return texto_url.strip().replace(' ','')
        else:
            return '' 
        # poderíamos já retornar um ValueError aqui, mas então teríamos dois métodos na mesma classe fazendo um mesmo tipo de verificação de erro; então retornar uma string vazia caso o parâmetro texto_url não seja um objeto str é a melhor maneira de otimizarmos a classe (o método de validação conseguirá efetuar seu trabalho)
        

    def valida_url(self):
        '''    
        if self.__url == '':
            raise ValueError('A url informada está vazia')
        else:
            pass
        '''

        # forma mais 'pythônica' de definir as condições dado que a string vazia '' pode ser interpretada como False pelo python 
        # (i.e., por debaixo dos panos o python aplica um bool() desse elemento quando incluído na condição de if/else)

        if not self.__url: # na minha opinião essa forma 'pythônica' retira um pouco de clareza do código, dificultando sua leitura futura
            raise ValueError('A url informada está vazia')
            

        else:
            # avaliando o caso específico da url do site de cambio
            url_pattern_1 = re.compile('[http://www.]?[bytebank][.com][.br]?[/cambio]')
            url_pattern_2 = re.compile('[https://www.]?[bytebank][.com][.br]?[/cambio]')
            url_pattern_3 = re.compile('[www.]?[bytebank][.com][.br]?[/cambio]')

            patterns_busca = [url_pattern_1, url_pattern_2, url_pattern_3]

            contador_aux = 0

            for pattern in patterns_busca:
                busca = pattern.search(self.__url) # procuro, em self.__url, a sequência pattern

                if not busca:
                    contador_aux +=1
                else:
                    pass
            
            # se eu passar pelos 3 padrões possíveis e não obtiver match com nenhum deles, então retorno o value error
            if contador_aux == 3:
                raise ValueError('A url informada é inválida') 
            else:
                pass

    def valida_url_melhorada(self):
        if not self.__url:
            raise ValueError('A url informada é inválida')

        else:
            url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
            
            # Observações:
                # Os parênteses, ao contrário dos colchetes, servem para indicar que queremos investigar exatamente a sequência de caracteres que informamos (ou seja, caracteres específicos dentro da string de avaliação);
                
                # Quando uma determinada sequência de caracteres é obrigatória, podemos escrever tanto (...){1} quanto, simplesmente, '...', como foi feito para os trechos bytebank.com e /cambio (os quais devem estar sempre presentes)

                # Podemos incluir parênteses/colchetes delimitadores de conjunto dentro de um próprio conjunto, conforme observamos para o caractere 's', dentro do conjunto de caracteres (http(s)?://)

            # No código v1 de validação utilizamos o método search para verficar se o padrão idealizado *estava presente* na url informada. É uma solução válida também, mas quando queremos que um conjunto de strings seja exatamente igual ao padrão definido pelo compile, podemos utilizar o método 'match' (que verifica se o padrão fornecido bate exatamente com o início da string em estudo)

            foi_validado = url_pattern.match(self.__url) # gera um objeto do tipo match que pode ser T/F quando convertido para bool

            if not foi_validado:
                raise ValueError('A url informada é inválida')
            else:
                pass


    def get_url_base(self):
        return self.__url[:self.__url.find('?')]

    def get_url_parametros(self):
        return self.__url[self.__url.find('?')+1:]

    def get_valor_parametro(self, param):

        page_variables = self.get_url_parametros()
        string_base = page_variables[page_variables.find(param):]

        initial_index = 0 
        last_index = string_base.find('&')

        url_variable_value = string_base[initial_index+len(param)+1:last_index if last_index != -1 else 999] 

        return url_variable_value
    
    def __len__(self):
        return len(self.__url) 

        # ou seja, estou definindo o dunder method 'len' como sendo o len do atributo __url 
        # (esse é um atributo da classe str, que já possui naturalmente a função built in 'len', portanto não há o que especificar aqui)

        # o detalhe de definir esse método é que se simplesmente chamássemos a função len para algum objeto, o python não saberia onde aplicar a função; com esse método estamos especificando exatamente o que deve ser feito quando essa função for chamada;

    def __str__(self):
        return 'URL: {} \n URL base: {} Parameros da URL: {}'.format(self.__url, self.get_url_base(), self.get_url_parametros())
    
    def __eq__(self, segundo_objeto):
        if type(segundo_objeto) == ExtratorUrl:
            return self.__url == segundo_objeto.__url
        else:
            print('Você está tentando comparar objetos de classes diferentes ({} x {})'.format(type(self), type(segundo_objeto)))


    # Observações:
        # Se não definíssemos o método __eq__ dessa maneira, estaríamos utilizando a definição default do python sempre que tentássemos comparar dois objetos distintos da classe ExtratorUrl (ou de qualquer outra; não há limitação). O detalhe é que esse método, por padrão, compara sempre o endereço de memória dos objetos quando é chamado (i.e., seus respectivos id's na memória do computador: id(obj1) == id(obj2) ) e isso, é claro, nunca será verdadeiro, porque os objetos são sempre alocados em espaços de memória diferentes (mesmo que sejam da mesma classe e possuam exatamente os mesmos atributos)      

if __name__ == '__main__':
    # Interface de utilização da classe
    
    # (linhas escritas antes de sua construção, para que seja possível visualizarmos o que realmente queremos fazer quando estivermos manipulando seus objetos e, com  isso, possamos ajustar os métodos/atributos da maneira mais adequada)

    #url_teste = ExtratorUrl('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
    #url_teste = ExtratorUrl(' teste _ url')
    #parametro = url_teste.get_valor_parametro('moedaDestino')
    #print(parametro)

    # função built-in para verificar os atributos/métodos de uma determinada classe de objetos: dir
    #dir(str)
    #print('tem o metodo len') if '__len__' in dir(str) else print('nao tem')

    # ! Desafio ! #
    valor_dolar = 5.5 # reais
    url = ExtratorUrl('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')

    moeda_origem = url.get_url_parametros('moedaOrigem')
    moeda_destino = url.get_url_parametros('moedaDestino')
    valor_conversao = float(url.get_valor_parametro('quantidade'))

    if moeda_origem == 'real' and moeda_destino == 'dolar': 
        print('O valor de R$ {:.2f} corresponde a U$ {:.2f}.'.format(valor_conversao, valor_conversao/valor_dolar))

    elif moeda_origem == 'dolar' and moeda_destino == 'real':
        print('O valor de U$ {:.2f} corresponde a R$ {:.2f}.'.format(valor_conversao, valor_conversao*valor_dolar))
    
    else:
        print('Conversão não disponível.')
    
