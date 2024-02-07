from conf.db_session import create_session
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabores import Sabor
from models.tipos_embalagem import TipoEmbalagem
from models.tipos_picole import TipoPicole

# Insert -> Aditivo Nutritivo
def insert_aditivo_nutritivo() -> None:
    print('Cadastrando aditivo nutritivo...')

    nome: str = input('Informe o nome do aditivo nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')

    an: AditivoNutritivo = AditivoNutritivo(
        nome= nome
        , formula_quimica= formula_quimica
    )

    with create_session() as session:
        session.add(an)
        session.commit()
    
    print('Aditivo Nutritivo cadastrado com sucesso!')
    print(f'ID: {an.id}')
    print(f'Data: {an.data_criacao}')
    print(f'Nome: {an.nome}')
    print(f'Formula Química: {an.formula_quimica}')

# Insert -> Novo Sabor
def insert_sabor() -> None:

    nome: str = input('Informe o sabor do picolé: ')

    novo_sabor: Sabor = Sabor(nome= nome)

    with create_session() as session:
        session.add(novo_sabor)
        session.commit()

    print('Novo sabor cadastrado com sucesso!')
    print('ID: {}'.format(novo_sabor.id))
    print('Data: {}'.format(novo_sabor.data_criacao))
    print('Nome: {}'.format(novo_sabor.nome))

# Insert -> Tipo Embalagem
def insert_tipo_embalagem():

    nome_embalagem: str = input('Informe o nome da embalagem: ')

    te: TipoEmbalagem = TipoEmbalagem(nome=nome_embalagem)

    new_session = create_session()
    with new_session as ns:
        ns.add(te)
        ns.commit()

    print(f'ID: {te.id}')
    print(f'Data: {te.data_criacao}')
    print(f'Nome: {te.nome}')

# Insert Tipo Picole
def insert_tipo_picole() -> None:

    nome_tipo_picole: str = input('Informe o nome do tipo de picolé: ')

    tp: TipoPicole = TipoPicole(nome= nome_tipo_picole)

    with create_session() as s:
        s.add(tp)
        s.commit()

    print(f'ID: {tp.id}')
    print(f'Data: {tp.data_criacao}')
    print(f'Nome: {tp.nome}')


if __name__ == '__main__':
    #insert_aditivo_nutritivo()
    #insert_sabor()
    #insert_tipo_embalagem()
    insert_tipo_picole()