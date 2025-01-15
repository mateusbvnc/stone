from flask import Blueprint, request, jsonify
from ..database import ConsultarAtendimento

'''
O modulo atendimentos contem o blueprint responsavel por consultar atendimentos no banco de dados
v1.1.0 

'''

atendimentos_bp = Blueprint("atendimentos_bp",__name__)

@atendimentos_bp.route("/atendimento")
def Consultar():
    filtros = request.args
    resultado_da_pesquisa = ConsultarAtendimento('postgres','password',filtros)

    return jsonify(resultado_da_pesquisa)