from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .DTO import Base
from sqlalchemy.exc import NoSuchModuleError,OperationalError

class Conn():

    '''
    A classe Conn é rosponsavel por criar um conexão com o banco de dados.

    Atributos:
        __sgbd : dialeto sql utilizado
        __driver : driver utilizado para conectar com o db
        __database : nome do banco de dados
        __host : servidor do banco de dados
        __username : nome de usuario (passado por argumento no Construtor)
        __password : senha do usuario (passado por argumento no Construtor)

    Metodos:
        create_session() : cria uma sessao no banco de dados com o usuario fornecido para Conn         

    e.g.:

        from app.database import Conn, Atendimento
         

        conn = Conn(usuario,senha)
        session = conn.create_session()  

        novo_atendimento = Atendimento(id_cliente = 5690, angel = 'Joao', polo = 'Centro', data_limite = '2025-03-01')
        session.add(novo_atendimento)
        session.commit() 


    '''

    __sgbd = 'postgresql'
    __driver = 'psycopg2'
    __database = 'pedrapag_db'
    __host = 'localhost'

    def __init__(self,
                 username : str = None,
                 password : str = None) -> None :

        self.__username = username
        self.__password = password

        try:
            if username == None or password == None :
                raise TypeError
            
            self.__engine = create_engine(f'{self.__sgbd}+{self.__driver}://{self.__username}:{self.__password}@{self.__host}/{self.__database}')
     
            Base.metadata.create_all(bind = self.__engine)
            
        except (UnicodeDecodeError,OperationalError) as e:
            message = '''Erro de conexao
Credenciais invalidas. Verifique o usuario e a senha passados.
Caso o problema persista verifique se o banco de dados esta disponivel no servidor '''
            
            print(f'Error : {type(e).__name__}\n{message}')

        except TypeError:
            message = '''Erro de conexao\ninformacoes insuficientes\n'''


    def create_session(self):
        Session = sessionmaker(bind=self.__engine)
        return Session()    

