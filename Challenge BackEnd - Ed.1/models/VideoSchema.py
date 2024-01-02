from typing import Optional # typing hints
from pydantic import BaseModel, validator # classe de validacao

class Video(BaseModel):
    Titulo: str
    Descricao: Optional[str]
    Url: str 
