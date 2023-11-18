class ExtratorUrl:

    def __init__(self, url):
        self.__url = self.sanitiza_url(url)
        self.valida_url() 

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
        if not self.__url:
            raise ValueError('A url informada está vazia')
        else:
            pass
        # na minha opinião essa forma 'pythônica' retira um pouco de clareza do código, dificultando sua leitura futura

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
    


# Interface de utilização da classe

# (linhas escritas antes de sua construção, para que seja possível visualizarmos o que realmente queremos fazer quando estivermos manipulando seus objetos e, com  isso, possamos ajustar os métodos/atributos da maneira mais adequada)

if __name__ == '__main__':
    #url_teste = ExtratorUrl('https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100')
    url_teste = ExtratorUrl(None)
    parametro = url_teste.get_valor_parametro('moedaDestino')
    print(parametro)
