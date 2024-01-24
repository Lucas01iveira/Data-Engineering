from pydantic import BaseModel, validator 
from typing import Optional
import re

class Video(BaseModel):
    Titulo: str
    Descricao: Optional[str]
    Url: str

    @validator('Titulo')
    def valida_titulo(cls, value):
        if not value.title():
            raise ValueError('O título precisa estar em formato capitalize')
    
    @validator('Url')
    def valida_url(cls,value):
        pattern = re.compile('(http(s)?://)?(www.)?projetosfrontend.com(.br)?')

        if not pattern.match(value):
            raise ValueError('A Url informada é inválida. Por favor, consulte a documentação')