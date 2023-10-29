
class Cliente:

    def __init__(self, nome):
        self.__nome = nome
    
    @property # serve para indicar que estamos lidando com um método do tipo getter, e permite que consultemos diretamente esse atributo da mesma maneira que faríamos se ele não fosse privado: <ref_objeto>.nome

    def nome(self):
        return self.__nome.upper() # (retorna o nome tratado, por exemplo)
    
    @nome.setter # serve para indicar que estamos lidando com um método do tipo setter referente ao atributo nome, e permite que alteremos diretamente o atributo da mesma maneira que faríamos se ele não fosse privado: <ref_objeto>.nome = novo_nome

    def nome(self, novo_nome):
        self.__nome = novo_nome