import sqlalchemy as sa 

import datetime 

from models.model_base import ModelBase

class Revendedor(ModelBase):
    __table_name__ = 'revendedores'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.Datetime, default=datetime.now(), nullable=False, index=True)

    cnpj: str = sa.Column(sa.String(45), nullable=False, unique=True)
    razao_social: str = sa.Column(sa.String(100), nullable=False, unique=True)
    contato: str = sa.Column(sa.String(100), nullable=False, unique=True)


    def __repr__(self):
        return f'<Revendedor - Cnpj: {self.cnpj}, Razao Social: {self.razao_social}, Contato: {self.contato}>'
