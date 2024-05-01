class BuscaEndereco:
    def __init__(self, cep):
        cep_str = str(cep)
        if self.cep_eh_valido(cep_str):
            self.cep = cep_str
        else:
            raise ValueError('Cep inválido! Favor verificar.')

    def cep_eh_valido(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False
    