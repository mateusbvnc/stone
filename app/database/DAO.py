from .util import Conn
from .DTO import Atendimento
from json import dumps , loads
from typing import Any 
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Query

'''
O modulo DAO contem todas as funcoes de acesso ao banco de dados.
v1.1.0

funcoes:

    ConsultarAtendimento : usada para realizar consultas a tabela de atendimentos

    CadastrarAtendimento : usada para cadastrar um novo atendimento

    AtualizarAtendimento : usada para atualizar informações na tabela de atendimentos

'''


def ConsultarAtendimento(usuario : str , 
                         senha : str,
                         filtros :dict,
                         json : bool = True ) -> (list[dict] | Query[Atendimento]):

    '''
    A funcao ConsultarAtendimento e responsavel por realizar buscas na tabela de atendimentos do banco de dados 
    pedrapag_db.

    Argumentos:
        usuario (str) : nome de usuario para entrar no banco de dados
        senha (str) : senha do usuario para entrar no banco de dados 
        json (bool) : determina se o retorno ser sera um json ou uma query

        filtros(dict) : dicionario contendo os campos que serao filtrados. Sao eles: 
            id_atendimento (int) : id do atendimento
            id_cliente (int) : id do cliente
            polo (str) : nome do polo do atendimento
            angel (str) : nome do angel
            data_limite (str | datetime.date) : prazo do atendimento
            data_de_atendimento (str | datetime.datetime | None): data e hora do atendimento 

      
    Exemplo de uso:

        from stone.app.database import ConsultarAtendimento

        query = ConsultarAtendimento(meu_usuario, minha_senha)

        print(query)

    '''

    # Funcao auxiliar
    def  Converter_para_dict(query):
          
            # Pega o resultado de uma query e tranforma para JSON, tornando algo mais legivel
           
            query_list =  [ {   'id_atendimento' : resultado.id_atendimento, 
                                'id_cliente' : resultado.id_cliente,
                                'angel' : resultado.angel,
                                'polo' : resultado.polo,
                                'data_limite' : str(resultado.data_limite),
                                'data_de_atendimento' : str(resultado.data_de_atendimento)
                            } for resultado in query]
            
            return query_list     
    



    try:
        conn = Conn(usuario,senha)
        session = conn.create_session()
    
        query = session.query(Atendimento)

        if filtros:
            for campo,valor in filtros.items():
                if hasattr(Atendimento,campo): 
                    query=query.filter(getattr(Atendimento,campo)==valor)

        query = query.all()

        if json:
            return  Converter_para_dict(query)
        
        return query
        
    except (UnicodeDecodeError,OperationalError) as e:
        print("A senha ou o usuario errado")  

    except TypeError as e:
        print("Argumento inesperado")   
                                   
    finally:
        if session :
            session.close()    









def CadastrarAtendimento(usuario : str,
                         senha : str,
                         atendimento : Atendimento) -> None:
    '''
    A funcao CadastrarAtendimento é usada para cadastrar um novo atendimento no banco de dados

    Argumentos:
    usuario (str) : nome de usuario para entrar no banco de dados
    senha (str) : senha do usuario 
    atendimento (Atendimento) : atendimento que sera cadastrado

    Exemplo de uso:

        from stone.app.database import CadastrarAtendimento, Atendimento

        id_atendimento = 15824
        id_cliente =  281009
        angel = 'Joao da Silva'
        polo = 'centro'
        data_limite = 01/03/2025'

        atendimento = Atendimento(id_atendimento = id_atendimento,
                                  id_cliente = id_cliente,
                                  angel = angel,
                                  polo = polo,
                                  data_limite = data_limite)

        CadastrarAtendimento('usuario_do_db',
                             'senha_do_usuario',
                              atendimento)    

    '''

    conn = Conn(usuario,senha)
    session = conn.create_session()
    session.add(atendimento)
    session.commit()
    session.close()

def AtualizarAtendimento(usuario : str,
                         senha : str,
                         id_atendimento : int,
                         atualizacoes : dict) -> None:
    
    '''
    A funcao AtualizarAtendimento é responsavel por atualizar dados de um atendimento.

    Argumentos:

        usuario (str): nome de usuario para entrar no banco de dados

        senha (str): senha do usuario do banco de dados

        id_atendimento (int): id do atendimento que sera atualizado

        atualizacoes (dict): campos que serao atualizados com seus respectivos novos valores

    Exemplo de uso:

        from stone.app.database import AtualizarAtendimento

        id_atendimento = 14903
        atualizacoes = {data_de_atendimento : '2025-01-01 13:28:13'}

        AtualizarAtendimento("usuario",
                             "senha",
                             id_atendimento,
                             atualizacoes)     
    '''

    try:

        conn = Conn(usuario,senha)
        session = conn.create_session()

        id = {'id_atendimento': id_atendimento}
        atendimento = ConsultarAtendimento(usuario,senha,id,False)[0]

        print(atendimento)

        for campo,novo_valor in atualizacoes.items():
            setattr(atendimento,campo,novo_valor)

    except Exception:
        print("Eu penso numa mensagem disso depois")
        session.rollback()

    else:
        session.merge(atendimento)
        session.commit()
        print('Sucesso')

    finally:
        if session :
            session.close()    
               
     


