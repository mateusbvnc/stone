from flask import Blueprint, request, Response
from ..database import AtualizarAtendimento

'''
O modulo atualizaratendimento contem o blueprint responsavel por ataulizar dados de um atendimento
v1.1.0 
'''

atualizaratendimento_bp = Blueprint("atualizaratendimento_bp",__name__)

@atualizaratendimento_bp.route("/atualizaratendimento",methods = ['PATCH'])
def Atualizar():
    id_atendimento = request.args.get('id_atendimento')
    atualizacoes = request.get_json()
    AtualizarAtendimento('postgres','password',id_atendimento,atualizacoes)
    return Response("Atendimento atualizado",200)
