from flask import Blueprint, request
from ..database import ConsultarAtendimento

atendimentos_bp = Blueprint("atendimentos_bp",__name__)

@atendimentos_bp.route("/atendimento")
def Consultar():
    filtros = request.args
    resultado_da_pesquisa = ConsultarAtendimento('postgres','password',filtros)
    return resultado_da_pesquisa