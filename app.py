# APP
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Marcelo 05/04/2023 - Pipeline DevOps Local - v1"

if __name__ == '__main__':
    app.run()