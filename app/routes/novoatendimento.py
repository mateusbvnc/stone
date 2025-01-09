from flask import Blueprint, request
from ..database import CadastrarAtendimento, Atendimento

novoatendimento_bp = Blueprint("novoatendimento_bp",__name__) 

@novoatendimento_bp.route("/novoatendimento")
def CriarAtendimento():
    atendimento= request.args

    id_atendimento = int(atendimento['id_atendimento'])
    id_cliente = int(atendimento['id_cliente'])
    angel = atendimento['angel']
    polo = atendimento['polo']
    data_de_atendimento = None
    data_limite = atendimento['data_limite']
    if 'data_de_atendimento' in atendimento:
        data_de_atendimento = atendimento['data_de_atendimento']

    novo_atendimento = Atendimento(id_atendimento = id_atendimento,
                                   id_cliente = id_cliente,
                                   angel = angel,
                                   polo = polo,
                                   data_limite = data_limite,
                                   data_de_atendimento = data_de_atendimento)   

    CadastrarAtendimento('postgres','password',novo_atendimento)  

    return 'Sucesso'   
