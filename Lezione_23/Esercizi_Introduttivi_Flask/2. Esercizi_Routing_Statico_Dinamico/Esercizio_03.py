'''
3. Parametri multipli

    * Creare /sum/<int:a>/<int:b> che restituisca la somma dei due numeri.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/sum/<int:a>/<int:b>")
def sum_2_nums(a: int, b: int):
    return f""" <h2>La somma tra {a} e {b} è:</h2>
    <p>{a + b}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)