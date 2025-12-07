'''
3. Mini blog

    * Definire route /post/<int:id> che restituisca un articolo fittizio.
    * Creare una pagine /posts con un elenco di post e i relativi link agli articoli generati tramite url_for.
'''
from flask import Flask, url_for

app = Flask(__name__)

# creazione di dizionario con post fittizi
posts = {
    1: {"title": "Introduzione a Flask", "content": "Flask è un micro framework leggero e potente"},
    2: {"title": "Perché devi usare Python?", "content": "Perché è semplice (tra virgolette...tante virgolette), leggero e molto diffuso"},
    3: {"title": "E allora, cos'è un endpoint?", "content": "Un endpoint è una URL che ti permette di accedere a una risorsa"}
}

# creazione home
@app.route("/")
def home():
    return "<h1>Mini Blog</h1><a href='/posts'>Vai ai post</a>"

# pagina che mostra un singolo articolo
@app.route("/post/<int:id>")
def show_post(id):
    post = posts.get(id)

    if not post:
        return "<h2>Post non trovato</h2>", 404
    
    return f"""
        <h2>{post['title']}</h2>
        <p>{post['content']}</p>
        <a href='{url_for("posts_list")}'>Torna ai post</a>
    """

# pagina con elenco dei post
@app.route("/posts")
def posts_list():
    links = ""

    for id, post in posts.items():
        post_url = url_for("show_post", id=id)
        links += f"<li><a href= '{post_url}'>{post['title']}</a></li>"
    
    return f"""
        <h2>Elenco post</h2>
        <ul>
            {links}
        </ul>
        """

if __name__ == "__main__":
    app.run(debug=True)