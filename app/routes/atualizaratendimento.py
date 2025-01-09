from flask import Blueprint, request
from ..database import AtualizarAtendimento

atualizaratendimento_bp = Blueprint("atualizaratendimento_bp",__name__)

@atualizaratendimento_bp.route("/atualizaratendimento")
def Atualizar():
    parametros = request.args
    filtros = {}
    atualizacoes = {}
    for key, value in parametros.items():
        if key.startswith('new_'):
            key = key[4:]
            atualizacoes[key] = value
        else:
            filtros[key] = value

    AtualizarAtendimento('postgres','password',filtros,atualizacoes)
    return 'SUCESSO'