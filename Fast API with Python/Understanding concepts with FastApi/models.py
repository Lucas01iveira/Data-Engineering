from typing import Optional # typing hints
from pydantic import BaseModel, validator # classe de validacao

class Curso(BaseModel):
    # classe que adquire muitas das características de BaseModel via herança de classes

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int

    # incluindo uma função de validação nos campos que serão inseridos pelo usuário
    @validator('titulo') # (referência ao campo que deve ser validado)
    def validar_titulo(cls, value: str): # def da função a ser executada para validação

        # parâmetro 'cls' refere-se à classe de objetos (nesse caso, Curso), e value é o valor do campo
        
        if len(value.split(' ')) < 3:
            raise ValueError('O titulo a ser inserido deve ter pelo menos 3 palavras')

        for word in value.split(' '):
            if word.isupper() or word.islower():
                raise ValueError('O titulo deve estar em formato capitalize')

        return value
    
    @validator('horas')
    def validar_horas(cls, value: int):
        if value < 10:
            raise ValueError('O curso deve ter pelo menos 10h de duração')

        return value
    
    @validator('aulas')
    def validar_aulas(cls, value: int):
        if value < 15:
            raise ValueError('O curso deve ter pelo menos 15 aulas')
        
        return value