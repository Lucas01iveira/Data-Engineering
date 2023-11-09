class Filme:

    # (atributo likes definido como opcional)
    def __init__(self, titulo, ano, duracao, likes= 0):
        self.__titulo = titulo.title() # str
        self.__ano = ano # int
        self.__duracao = duracao # minutos (int) 
        self.__likes = likes #int

    # defino métodos getters para acessar os atributos dos objetos
    @property
    def titulo(self):
        return self.__titulo
    
    @property
    def ano(self):
        return self.__ano

    @property
    def duracao(self):
        return self.__duracao
    
    @property
    def likes(self):
        return self.__likes
    
    # método setter para ajustar a quantidade de likes
    def set_likes(self, qtd):
        self.__likes = qtd
    
class Serie:

    #(atributo 'likes' definido como opcional)
    def __init__(self, titulo, ano, temporadas, likes= 0):
        self.__titulo = titulo # str
        self.__ano = ano # int
        self.__temporadas = temporadas # int 
        self.__likes = likes #int

    # defino métodos getters para acessar os atributos dos objetos
    @property
    def titulo(self):
        return self.__titulo.title()
    
    @property
    def ano(self):
        return self.__ano

    @property
    def temporadas(self):
        return self.__temporadas

    @property
    def likes(self):
        return self.__likes
    
    # método setter para ajustar a quantidade de likes
    @likes.setter
    def likes(self, qtd):
        self.__likes = qtd