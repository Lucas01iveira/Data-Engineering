import sqlalchemy as sa 
import sqlalchemy.orm as orm 

from datetime import datetime 
from typing import List, Optional

from models.model_base import ModelBase
from models.sabores import Sabor
from models.tipos_embalagem import TipoEmbalagem
from models.tipos_picole import TipoPicole
from models.aditivo_nutritivo import AditivoNutritivo
from models.ingredientes import Ingrediente
from models.conservantes import Conservante

# Um picolé pode ter vários aditivos nutritivos, da mesma forma que 1 aditivo nutritivo pode estar em vários picolés (relacionamento n x m exige a criação de uma entidade associativa)
aditivos_nutritivos_picole = sa.Table(
    'aditivos_nutritivos_picole' # nome da entidade
    ,ModelBase.metadata # metadata do model base
    ,sa.Column('id_aditivo_nutritivo', sa.Integer, sa.ForeignKey('aditivos_nutritivos.id'))
    ,sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
)

# Um picolé pode ter vários ingredientes, da mesma forma que 1 ingrediente pode estar em vários picolés (relacionamento n x m exige a criação de uma entidade associativa)
ingredientes_picole = sa.Table(
    'ingredientes_picole' # nome da entidade
    ,ModelBase.metadata # metadata do model base
    ,sa.Column('id_ingrediente', sa.Integer, sa.ForeignKey('ingredientes.id'))
    ,sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
)

# Um picolé pode ter vários conservantes, da mesma forma que 1 conservante pode estar em vários picolés (relacionamento n x m exige a criação de uma entidade associativa)
conservantes_picole = sa.Table(
    'conservantes_picole' # nome da entidade
    ,ModelBase.metadata # metadata do model base
    ,sa.Column('id_conservante', sa.Integer, sa.ForeignKey('conservantes.id'))
    ,sa.Column('id_picole', sa.Integer, sa.ForeignKey('picoles.id'))
)

class Picole(ModelBase):
    __tablename__ = 'picoles'

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True, nullable=False)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)

    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)

    id_sabor: int = sa.Column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: orm.Mapped[Sabor] = orm.relationship('Sabor', lazy='joined') # trazendo a referência do objeto para esse código (não é coluna nem nada; apenas uma config a mais)

    id_tipo_embalagem: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: orm.Mapped[TipoEmbalagem] = orm.relationship('TipoEmbalagem', lazy='joined') # trazendo a referência do objeto para esse código (não é coluna nem nada; apenas uma config a mais)

    id_tipo_picole: int = sa.Column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: orm.Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined') # trazendo a referência do objeto para esse código (não é coluna nem nada; apenas uma config a mais)

    # Incluindo o relacionamento entre a entidade de picolés e a entidade de aditivos_nutritivos com base na entidade associativa aditivos_nutritivos_picole. Lembrando que um picolé pode não ter nenhum conservante;
    aditivos_nutritivos: orm.Mapped[Optional[List[AditivoNutritivo]]] = orm.relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='AditivoNutritivo', lazy='joined')

    # Incluindo o relacionamento entre a entidade de picolés e a entidade de ingredientes com base na entidade associativa ingredientes_picole
    ingredientes: orm.Mapped[List[Ingrediente]] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='Ingrediente', lazy='joined')

    # Incluindo o relacionamento entre a entidade de picolés e a entidade de conservantes com base na entidade associativa conservantes_picole. Lembrando que um picolé pode não ter nenhum conservante;
    conservantes: orm.Mapped[Optional[List[Conservante]]] = orm.relationship('Conservante', secondary=conservantes_picole, backref='Conservante', lazy='joined')

    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preco {self.preco}>'