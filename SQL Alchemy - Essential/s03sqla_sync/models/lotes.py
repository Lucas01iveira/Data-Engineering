import sqlalchemy as sa 
import sqlalchemy.orm as orm

from datetime import datetime 

from models.model_base import ModelBase
from models.tipos_picole import TipoPicole

class Lote(ModelBase):
    __table_name__ = 'lotes'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, index=True, default=datetime.now, nullable=False)

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id')) # foreign_key -> tabela.campo (que esteja dentro da classe importada)
    tipo_picole: TipoPicole = orm.relationship('TipoPicole', lazy='joined') # configuração interna do SqlAlchemy (orm utilizado para mapeamento de objetos relacionais)
    quantidade: int = sa.Column(sa.Integer, nullable=False)

    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'
    