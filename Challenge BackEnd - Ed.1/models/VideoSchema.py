from typing import Optional # typing hints
from pydantic import BaseModel, validator # classe de validacao
import re

class Video(BaseModel):
    Titulo: str
    Descricao: Optional[str]
    Url: str 

    @validator('Titulo') # precisa estar em formato capitalize
    def valida_titulo(cls, value):
        if not value.istitle():
            raise ValueError('O titulo precisa estar em formato title')
        else:
            return value

    # como estamos desenvolvendo um projeto front ent, vamos impor que os endereçamentos possuam o seguinte formato padrão:
        # videos.com.br/frontend/{endpoint}
    @validator('Url')
    def valida_url(cls, value):
        pattern = re.compile('(http(s)?://)?videos.com(.br)?/frontend/')

        if not pattern.match(value):
            raise ValueError('O padrão de url inserido é inválido. Lembrando: a localização do recurso deve ser \'videos.com\' e o nome do recurso deve ser \'frontend\'')
        else:
            return value