from flask import Flask
from .routes import atendimentos_bp, atualizaratendimento_bp, novoatendimento_bp

app = Flask(__name__)

@app.route('/')
def index():
    return "olá mundo"

app.register_blueprint(atendimentos_bp)
app.register_blueprint(atualizaratendimento_bp)
app.register_blueprint(novoatendimento_bp)

if __name__ == '__main__':
    app.run(debug=True)