from validate_docbr import CPF

class Cpf:
    def __init__(self, numero_documento):
        numero_documento = str(numero_documento)
        if self.cpf_eh_valido(numero_documento):
            self.cpf = numero_documento
        else: 
            raise ValueError('Cpf inválido')

    def cpf_eh_valido(self, valor):
        if len(valor) == 11:
            validador = CPF()
            return validador.validate(valor)
        else:
            raise ValueError('Quantidade de dígitos inválida')
        
    def formata_cpf(self, valor):
        # cpf_str = str(valor)
        # conta_fatia = 1
        # cpf_formatado = ''
        # for i in range(0,len(cpf_str),3):

        #     if conta_fatia != 3 and conta_fatia != 4:
        #         cpf_formatado += cpf_str[i:i+3]+'.'
        #     elif conta_fatia != 4:
        #         cpf_formatado += cpf_str[i:i+3]+'-'
        #     else:
        #         cpf_formatado += cpf_str[i:i+3]
            
        #     conta_fatia += 1
        
        # return cpf_formatado
        mascara = CPF()
        return mascara.mask(valor)
    
    def __str__(self):
        return 'CPF: {}'.format(self.formata_cpf(self.cpf))