import sqlalchemy as sa 

import datetime 

from models.model_base import ModelBase 

class TipoEmbalagem(ModelBase):
    __table_name__ = 'tipos_embalagem'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self):
        return f'<Tipo Embalagem: {self.nome}>'