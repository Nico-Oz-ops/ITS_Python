'''
1. Generazione link interni

    * Usare url_for per creare automaticamente i link alle route definite, 
    ed esporli in una pagina principale (homepage con link a /about, /user/..., ecc.).
    app = Flask(__name__)
'''

from flask import Flask, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Home page</h1>"

@app.route("/show_urls")
def show_urls():
    about_url = url_for('about')
    user_url = url_for('show_user_profile', username='John Doe')
    square_url = url_for('show_post', post_id=42)

    # restituire una pagina con i link
    return f"""
    <h2>Link generati con url_for:</h2>
    <ul>
        <li><a href="{home_url}">Home</a></li>
        <li><a href="{user_url}">Profilo utente (John Doe)</a></li>
        <li><a href="{post_url}">Post 42</a></li>
    </ul>"""

@app.route('/user/<string:username>')
def square_num(username):
    return f"Profilo di {username}"

@app.route('/square/<int:n>')
def show_post(post_id):
    return f"Post {post_id}"

if __name__ == '__main__':
    app.run(debug=True)

