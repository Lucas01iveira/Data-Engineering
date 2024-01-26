from pydantic import BaseModel, validator
from typing import Optional

class Categoria(BaseModel):
    DescricaoCategoria: str
    Cor: str

    @validator('Cor')
    def valida_cor(cls, value):
        if value.strip() == '':
            raise ValueError('Você deve inserir a indicação de uma cor no formato hexadecimal (correspondência css)')
        else:
            return value.strip()
    
    @validator('DescricaoCategoria')
    def valida_descricao(cls, value):
        if value.strip() == '':
            raise ValueError('Você deve inserir uma descrição válida')
        else:
            return value.strip().capitalize()