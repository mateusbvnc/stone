from pandas import read_csv
from ..app.database import CadastrarAtendimento,Atendimento
from sqlalchemy.exc import DataError


df = read_csv("C:/Users/Mateus Barbosa/Desktop/Stone/bd_desafio.csv",delimiter=';')

bd_desafio = df.to_dict('records')

for atendimento in bd_desafio:
    id_atendimento = atendimento['id_atendimento']
    id_cliente = atendimento['id_cliente']
    angel = atendimento['angel']
    polo = atendimento['polo']
    data_limite = atendimento['data_limite']
    data_de_atendimento = atendimento['data_de_atendimento']

    novo_atendimento = Atendimento(id_atendimento = id_atendimento,
                                   id_cliente = id_cliente,
                                   angel = angel,
                                   polo = polo,
                                   data_limite = data_limite,
                                   data_de_atendimento = data_de_atendimento)
    try:
        CadastrarAtendimento('postgres','password',novo_atendimento)
    except DataError:
        print(f"Erro ao cadastar o atendimento {id_atendimento}")
    finally:
        pass    