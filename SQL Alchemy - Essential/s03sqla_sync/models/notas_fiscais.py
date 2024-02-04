import sqlalchemy as sa 
import sqlalchemy.orm as orm

from datetime import datetime 
from typing import List 

from models.model_base import ModelBase
from models.revendedores import Revendedor
from models.lotes import Lote

# Uma dada nota fiscal pode ter vários lotes -> relacionamento n x m entre a entidade de notas fiscais e a entidade de lotes. Dentro da modelagem do banco de dados, isso exige a criação de uma nova entidade, uma entidade do tipo associativa, responsável por agrupar e endereçar corretamente esses cruzamentos
lote_nota_fiscal = sa.Table(
    'lotes_nota_fiscal' # nome da entidade
    ,ModelBase.metadata # metadata do model base
    ,sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id'))
    ,sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'))
)

class NotaFiscal(ModelBase):
    __tablename__ = 'notas_fiscais'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, index=True, default=datetime.now)

    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: str = sa.Column(sa.String(45), nullable=False, unique=True)
    descricao: str = sa.Column(sa.String(200), nullable=False)

    id_revendedor: int = sa.Column(sa.Integer, sa.ForeignKey('revendedores.id'))  #mapped_column(ForeignKey('revendedores.id'))
    revendedor : orm.Mapped[Revendedor] = orm.relationship('Revendedor', lazy='joined')

    # incluindo o relacionamento entre as entidades de lotes e notas fiscais (1 nota fiscal pode ter vários lotes; um lote também pode ter várias notas fiscais, mas para cada nota fiscal dentro de um lote, ela é única)
    lotes: orm.Mapped[List[Lote]] = orm.relationship('Lote', secondary=lote_nota_fiscal, backref='Lote', lazy='dynamic')

    def __repr__(self) -> str:
        return f'Nota Fiscal: {self.numero_serie}'