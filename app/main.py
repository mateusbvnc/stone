from flask import Flask
from .routes import atendimentos_bp, atualizaratendimento_bp, novoatendimento_bp

'''
o modulo main e resposavel por executar a API

rotas: 
    /pedrapagdb/lastmile/atendimento : rota para consultar atendimentos

    /pedrapagdb/lastmile/atualizaratendimento : rota para atualizar dados de um atendimento

    /pedrapagdb/lastmile/novoatendimento : rota para cadastrar um novo atendimento

'''

app = Flask(__name__)


app.register_blueprint(atendimentos_bp, url_prefix = '/pedrapagdb/lastmile')
app.register_blueprint(atualizaratendimento_bp, url_prefix = '/pedrapagdb/lastmile')
app.register_blueprint(novoatendimento_bp, url_prefix = '/pedrapagdb/lastmile')

if __name__ == '__main__':
    app.run(debug=True)