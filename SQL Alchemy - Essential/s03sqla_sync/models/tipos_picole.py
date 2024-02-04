import sqlalchemy as sa 

from datetime import datetime 

from models.model_base import ModelBase

class TipoPicole(ModelBase):
    __table_name__ = 'tipos_picole'

    id: int = sa.Column(sa.Integer, primary_key=True, nullable=False, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    nome: str = sa.Column(sa.String(45), nullable=False, unique=True)

    def __repr__(self):
        return f'<Tipo Picole: {self.nome}>'