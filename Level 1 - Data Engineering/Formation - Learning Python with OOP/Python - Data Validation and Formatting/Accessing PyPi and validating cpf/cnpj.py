from validate_docbr import CNPJ

class Cnpj:
    def __init__(self, documento):
        if self.valida_doc(documento):
            self.documento = documento
        else:
            raise ValueError('Cnpj inválido! Favor verificar')

    def valida_doc(self, numero):
        numero_str = str(numero)
        if len(numero_str) == 14:
            validador = CNPJ()
            return validador.validate(numero_str)
        else:
            raise ValueError('Quantidade de dígitos inválida! Favor verificar.')
        
    def __str__(self):
        formatador = CNPJ()
        return 'CNPJ: {}'.format(formatador.mask(self.documento))