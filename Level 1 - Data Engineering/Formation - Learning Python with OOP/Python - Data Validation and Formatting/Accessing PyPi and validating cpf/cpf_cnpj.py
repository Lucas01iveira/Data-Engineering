from validate_docbr import CPF, CNPJ
class Documento:

    @staticmethod
    def cria(documento):
        if len(documento) == 11:
            return Cpf(documento)
        elif len(documento) == 14:
            return Cnpj(documento)
        else:
            raise ValueError('Quantidade de dígitos inválida! Favor verificar.')
    
class Cpf:
    def __init__(self, documento):
        if self.valida_cpf(documento):
            self.cpf = documento
        else:
            raise ValueError('Cpf inválido! Favor verificar.')

    def valida_cpf(self, documento):
        validador = CPF()
        return validador.validate(documento)
    
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    
    def __str__(self):
        return 'CPF: {}'.format(self.formata_cpf())

class Cnpj:
    def __init__(self, documento):
        if self.valida_cnpj(documento):
            self.cnpj = documento
        else:
            raise ValueError('Cnpj inválido! Favor verificar.')

    def valida_cnpj(self, documento):
        validador = CNPJ()
        return validador.validate(documento)
    
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
    
    def __str__(self):
        return 'CNPJ: {}'.format(self.formata_cnpj())