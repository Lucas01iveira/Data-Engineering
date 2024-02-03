import sqlalchemy as sa 

from datetime import datetime 

from models.model_base import ModelBase

class AditivoNutritivo(ModelBase):
    __tablename__: str = 'aditivos_nutritivos'

    # colunas com valores default (preenchidas automaticamente)
    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index= True) # não coloco o parênteses no 'now' pois apenas estou sinalizando o método que deve ser executado quando um novo registro for inserido

    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    formula_quimica: str = sa.Column(sa.String(45), unique=True, nullable=False)

    def __repr__(self) -> str:
        return f'<Aditivo Nutritivo: {self.nome}>'
