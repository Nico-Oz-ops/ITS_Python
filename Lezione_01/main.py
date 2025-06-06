import psycopg

conn = psycopg.connect(
    dbname="corso_its",        # deve esistere
    user="postgres",           # utente predefinito
    password="postgres",       # password predefinita
    host="postgresql",         # nome del servizio nel docker-compose.yaml
    port=5432
)

print("Connessione avvenuta con successo!")

conn.close()