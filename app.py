from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Marcelo Moraes 05/10/2022"

if __name__ == '__main__':
    app.run()