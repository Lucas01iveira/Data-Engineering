import sqlalchemy as sa 

import datetime 

from models.model_base import ModelBase

class Ingrediente(ModelBase):
    __table_name__ = 'ingredientes'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.Datetime, default=datetime.now(), nullable=False, index=True)

    nome: str = sa.Column(sa.String(45), nullable=False, unique=True)

    def __repr__(self):
        return f'<Ingrediente: {self.nome}>'
