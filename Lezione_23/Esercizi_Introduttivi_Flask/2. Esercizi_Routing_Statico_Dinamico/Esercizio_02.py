'''
2. Route con parametri numerici

    * Definire /square/<int:n> che ritorni il quadrato di n.
'''

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home Page</h1>"

@app.route("/square/<int:n>")
def square_num(n: int) -> int:
    return f'''<h2> Il quadrato di {n} è:</h2>
    <p>{n ** 2}</p>
    '''

if __name__ == "__main__":
    app.run(debug=True)
