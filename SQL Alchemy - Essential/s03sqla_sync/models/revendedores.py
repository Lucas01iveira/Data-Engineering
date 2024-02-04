import sqlalchemy as sa 

from datetime import datetime 

from models.model_base import ModelBase

class Revendedor(ModelBase):
    __tablename__ = 'revendedores'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, nullable=False, index=True)

    cnpj: str = sa.Column(sa.String(45), nullable=False, unique=True)
    razao_social: str = sa.Column(sa.String(100), nullable=False, unique=True)
    contato: str = sa.Column(sa.String(100), nullable=False, unique=True)


    def __repr__(self):
        return f'<Revendedor - Cnpj: {self.cnpj}, Razao Social: {self.razao_social}, Contato: {self.contato}>'
