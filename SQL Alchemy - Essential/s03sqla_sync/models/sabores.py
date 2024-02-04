import sqlalchemy as sa 

from datetime import datetime 

from models.model_base import ModelBase 

class Sabor(ModelBase):
    __table_name__ = 'sabores'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self):
        return f'<Sabor: {self.nome}>'