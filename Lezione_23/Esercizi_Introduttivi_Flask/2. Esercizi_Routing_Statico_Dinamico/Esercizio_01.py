'''
1. Route dinamica per profilo utente

    * Creare un percorso /user/<nome> che restituisca “Benvenuto, <nome>!”.
    * Testare con nomi diversi nell’URL.
'''
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home page</h1>"

@app.route("/user/<string:nome>")
def show_username_profile(nome: str) -> str:
    return f"<h2>Benvenuto, {nome}!</h2>"

if __name__=="__main__":
    app.run(debug=True)