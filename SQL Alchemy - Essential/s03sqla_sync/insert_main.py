from conf.db_session import create_session

# Inserts / Parte 1 (entidades sem relacionamento)
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabores import Sabor
from models.tipos_embalagem import TipoEmbalagem
from models.tipos_picole import TipoPicole
from models.conservantes import Conservante
from models.revendedores import Revendedor

# Inserts / Parte 2 (entidades com vínculo estrangeiro)
from models.lotes import Lote
from models.notas_fiscais import NotaFiscal

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

# Insert -> Conservantes
def insert_conservantes() -> None:

    nome: str = input('Informe o nome do conservante: ')
    descricao: str = input('Informe a descrição do conservante: ')

    conserv: Conservante = Conservante(nome=nome, descricao=descricao)

    with create_session() as session:
        session.add(conserv)
        session.commit()
    
    print(f'ID: {conserv.id}')
    print(f'Data: {conserv.data_criacao}')
    print(f'Nome: {conserv.nome}')
    print(f'DEscricao: {conserv.descricao}')

# Insert -> Revendedores
def insert_revendedores() -> None: # -> Revendedor:

    cnpj: str = input('Informe o cnpj do revendedor: ')
    razao_social: str = input('Informe a razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')

    r: Revendedor = Revendedor(cnpj=cnpj, razao_social=razao_social, contato=contato)

    with create_session() as session:
        session.add(r)
        session.commit()
    
    print(f'ID: {r.id}')
    print(f'Data: {r.data_criacao}')
    print(f'Cnpj: {r.cnpj}')
    print(f'Razao Social: {r.razao_social}')
    print(f'Contato: {r.contato}')

    # return r

# Insert -> Lotes
def insert_lote() -> None:

    id_tipo_picole: int = input('Informe o Id do tipo picole: ')
    quantidade: int = input('Informe a quantidade de picolés: ')

    lote = Lote(id_tipo_picole=id_tipo_picole, quantidade=quantidade)

    with create_session() as session:
        session.add(lote)
        session.commit()

    print(f'ID: {lote.id}')
    print(f'Data: {lote.data_criacao}')
    print(f'Id Tipo Picole: {lote.id_tipo_picole}')
    print(f'Quantidade: {lote.quantidade}')

# Insert -> Nota Fiscal
def insert_nota_fiscal() -> None:

    valor: float = float(input('Informe o valor do produto: '))
    numero_serie: str = input('Informe o número de série do produto: ')
    descricao: str = input('Informe a descrição do produto: ')
    id_revendedor: int = int(input('Informe o Id do revendedor: '))

    nf: NotaFiscal = NotaFiscal(
        valor= valor
        ,numero_serie= numero_serie
        ,descricao= descricao
        ,id_revendedor= id_revendedor
    )     

    with create_session() as session:
        session.add(nf)
        session.commit()
    
    print('ID: {}'.format(nf.id))
    print('Data: {}'.format(nf.data_criacao))
    print('Valor: {}'.format(nf.valor))
    print('Numero Serie: {}'.format(nf.numero_serie))
    print('Descricao: {}'.format(nf.descricao))
    print('ID Revendedor: {}'.format(nf.id_revendedor))

if __name__ == '__main__':
    #insert_aditivo_nutritivo()
    #insert_sabor()
    #insert_tipo_embalagem()
    #insert_tipo_picole()
    #insert_conservantes()
    #insert_revendedores()
    insert_lote()
    #insert_nota_fiscal()