'''
2. Navigazione dinamica

    * Creare una pagina con elenco utenti fittizi e i relativi link ai loro profili generati con url_for.
'''
from flask import Flask, url_for

app = Flask(__name__)

# Lista di utenti fittizi
users = ["Anna", "Bob", "Carlo", "Daniela"]

@app.route("/")
def home():
    return "<h1>Home Page</h1><a href= '/users'>Vai alla lista utenti</a>"

@app.route("/users")
def users_list():
    # genero i link a ogni profilo
    links = ""
    for user in users:
        profile_url = url_for("show_user_profile", username = user)
        links += f"<li><a href='{profile_url}'>{user}</a></li>"
    
    return f"""
    <h2>Lista utenti</h2>
    <ul> 
        {links} 
    </ul>
    """

@app.route("/user/<string:username>")
def show_user_profile(username):
    return f"<h2>Profilo di {username}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
