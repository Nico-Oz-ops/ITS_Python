from flask import Flask, url_for 

app = Flask(__name__)

# 1. rotta statica che corrisponde a un URL fisso
# si possono creare tutte le rotte statiche che voglio,
# ognuna con il suo contenuto o comportamento
@app.route('/') 
def home() -> str:
    return "<h1>Hola Hola!!!</h1>"

# 2. rotte dinamiche: si possono creare rotte che accettano variabili
# nell'URL usando una sintassi speciale con angoli < >.
@app.route('/user/<string:username>')
def show_user_profile(username: str) -> str:
    return f"Profilo di {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id: int) -> str:
    return f"Post {post_id}"

# 3. Url_for()
with app.test_request_context():
    print(url_for('home')) # stampa: /
    print(url_for('show_user_profile', username = 'John Doe')) # stampa: /user/John%20Doe
    print(url_for('show_post', post_id = 42)) # stampa: /post/42

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)

'''
* <string:username> significa che quella parte dell’URL sarà una stringa e sarà passata come parametro username alla funzione.
* <int:post_id> significa che quella parte dell’URL sarà un intero passato come parametro post_id.

Si possono usare diversi converter per specificare il tipo della variabile nella rotta:

    - string (default): qualsiasi testo senza slash /
    - int: numeri interi
    - float: numeri decimali
    - path: come stringa ma può contenere anche /
    - uuid: un identificatore unico universale

Esempi di URL:
    * /user/mario -> chiama show_user_profile("mario")
    * /post/42 -> chiama show_post(42)

    
A cosa serve url_for()?

    * Costruisce l’URL a partire dal nome della funzione (quella usata nella rotta), senza dover scrivere manualmente la stringa dell’URL.
    * Se cambi la rotta di una funzione, tutte le chiamate a url_for() si aggiornano automaticamente.
    * Genera URL assoluti, così eviti problemi con i percorsi relativi.
    * Gestisce automaticamente caratteri speciali come spazi, convertendoli in codici percentuali (%20).

Perché è utile?

Immagina di dover cambiare il percorso /user/<username> in /utente/<username>. 
Se usi URL scritti a mano, dovresti cambiare ogni riferimento. Con url_for(), 
basta cambiare la rotta nella funzione, e il resto funziona da solo.




app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Home</h1>"

@app.route('/show-urls')
def show_urls():
    home_url = url_for('home')
    user_url = url_for('show_user_profile', username='John Doe')
    post_url = url_for('show_post', post_id=42)
    
    return f"""
    <p>URL home: {home_url}</p>
    <p>URL profilo utente: {user_url}</p>
    <p>URL post: {post_url}</p>
    """

@app.route('/user/<string:username>')
def show_user_profile(username):
    return f"Profilo di {username}"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

if __name__ == '__main__':
    app.run(debug=True)
'''
