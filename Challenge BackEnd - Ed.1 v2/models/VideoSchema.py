from pydantic import BaseModel, validator 
from typing import Optional
import re

class Video(BaseModel):
    Titulo: str
    Descricao: Optional[str]
    Url: str

    @validator('Titulo')
    def valida_titulo(cls, value):
        if not value.istitle():
            raise ValueError('O título precisa estar em formato title')
        else:
            return value
    
    @validator('Url')
    def valida_url(cls,value):
        pattern = re.compile('(http(s)?://)?(www.)?aluraflix.com(.br)?/videos')

        if not pattern.match(value):
            raise ValueError('A Url informada é inválida. Por favor, consulte a documentação')
        else:
            return value