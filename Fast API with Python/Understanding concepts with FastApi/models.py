from typing import Optional # typing hints
from pydantic import BaseModel # classe de validacao

class Curso(BaseModel):
    # classe que adquire muitas das características de BaseModel via herança de classes

    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


