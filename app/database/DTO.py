from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, Date, TIMESTAMP

'''
O modulo DTO contem as classes de transferencia de dados.

classes: 
    Atendimento : classe que contem as informacoes de um atendimento

'''

Base = declarative_base() # classe base sqlalchemy 

class Atendimento(Base):

    '''
    classe que contem as informacoes de um atendimento.

    Atributos:
        id_atendimento (int): Identificador único do atendimento (gerado automaticamente).
        id_cliente (int): Identificador do cliente.
        angel (str): Nome do responsável pelo atendimento.
        polo (str): Local do atendimento.
        data_limite (str | date): Data limite para o atendimento. Pode ser string no formato 'YYYY-MM-DD' ou um objeto date.
        data_de_atendimento (str | datetime): Data e hora do atendimento. Pode ser string no formato 'YYYY-MM-DD HH:MM:SS' ou um objeto datetime.

    '''

    __tablename__ = 'atendimentos'
    __table_args__ = {'schema' : 'lastmile_schema'}
            
    id_atendimento = Column(Integer,primary_key=True,autoincrement=True)
    id_cliente = Column(Integer, nullable=False)
    angel= Column(VARCHAR(100), nullable=False)
    polo = Column(VARCHAR(100), nullable=False)
    data_limite = Column(Date,nullable=False)
    data_de_atendimento = Column(TIMESTAMP)

