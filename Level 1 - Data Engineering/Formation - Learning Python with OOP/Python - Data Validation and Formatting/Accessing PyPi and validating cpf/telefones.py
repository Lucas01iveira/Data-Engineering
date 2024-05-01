import re 

class Telefone:
    global pattern_phone
    pattern_phone = r'([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})'

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError('O número informado é inválido! Favor verificar.')
    
    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        
        if re.search(pattern_phone, telefone):
            return True
        else:
            return False

    def format_numero(self):
        busca = re.search(pattern_phone, self.numero)
        # caso não tenha o código de país, insiro o do Brasil como padrão
        if busca.group(1) is None: 
            return '+{} ({}) {}-{}'.format(
                '55'
                ,busca.group(2)
                ,busca.group(3)
                ,busca.group(4)
            )

        # caso tenha, trago o valor inserido:
        else:
            return '+{} ({}) {}-{}'.format(
                busca.group(1)
                ,busca.group(2)
                ,busca.group(3)
                ,busca.group(4)
            )
    