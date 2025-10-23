'''
1. Definire un route /about 
    * Definire una route /about che ritorni un breve testo HTML 
    con descrizione dell’app o dell’autore.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home() -> str:
    return "Benvenuto nella mia app Flask"

@app.route("/about")
def about() -> str:
    return '''
    <h1>About</h1>
    <p>Questa è una semplice applicazione Flask creata per esercitarmi con le route.</p>
    <p>Autore: Nico</p>
    '''
if __name__=="__main__":
    app.run(debug=True)
