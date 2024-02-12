from typing import List 

from sqlalchemy import func # funções de agregação

from conf.helpers import formata_data # retorna data formatada
from conf.db_session import create_session

# Parte 1 -> Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabores import Sabor
from models.revendedores import Revendedor

# Parte 2 -> Selects compostos ou complexos
from models.picoles import Picole

# -- x -- # # -- x -- # # -- x -- # # -- x -- # # -- x -- # 
# Select Simples (select * from dbo.aditivos_nutritivos)
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # forma 1
        # aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)

        # forma 2
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')
        
        # A diferença entre as formas 1 e 2 é que o formato 2 já retorna a lista de aditivos nutritivos, enquanto a forma 1 retorna o objeto aditivo nutritivo por completo;

def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        # forma 1 -- retorna None caso o id informado não exista no banco (gera AttributeError nos prints subsequentes)
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id  == id_sabor).first() 
        
        # forma 2 -- faz a mesma coisa que a forma 1, mas deixa explícito que estamos selecionando o registro já existente ou null
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()

        # forma 3 -- retorna uma exception caso o id não exista no bando
        #sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one() # não recomendado

        # forma 4 -- utilizando where ao invés de filter
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()

        # podemos acrescentar novas condicionais (and) simplesmente acrescentando uma vírgula e incluindo os novos filtros

        if sabor is not None:
            print(sabor)
            print(f'ID: {sabor.id}')
            print(f'Data: {formata_data(sabor.data_criacao)}')
            print(f'Nome: {sabor.nome}')

def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()
        
        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {picole.data_criacao}')
            print(f'Preco: {picole.preco}')

            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')

            print(f'ID Tipo Emvalagem: {picole.id_tipo_embalagem}')
            print(f'Tipo Embalagem: {picole.tipo_embalagem.nome}')

            print(f'ID Tipo Picolé: {picole.id_tipo_picole}')
            print(f'Nome: {picole.tipo_embalagem.nome}')

            # relacionamentos que podem ser avaliados como lista;
            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')

def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.id.desc()).all()

        # também é possível acrescentar novas colunas para ordenamento, simplesmente incluindo uma vírgula e as novas condições de interesse;

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')

if __name__ == '__main__':
    #select_todos_aditivos_nutritivos()
    #select_filtro_sabor(2100)
    #select_complexo_picole()
    select_order_by_sabor()