'''
4. Progetta una mini API: un’agenzia di viaggi deve gestire destinazioni, clienti e prenotazioni. 
Definisci 5 endpoint REST (metodo + URI + esempio di risposta JSON).
'''
# Endpoint 1: ottenere elenco delle prenotazioni
# Endpoint 2: creazione di un cliente 
# Endpoint 3: modifica di un viaggio(id)
# Endpoint 4: aggiungere una nuova destinazione
# Endpoint 5: modifica totale di una prenotazione

'''
Endpoint 1:
Metodo HTTP: GET
Endpoint: /prenotazioni
Descrizione: Ottiene l'elenco di tutte le prenotazioni.
Codice di stato: 200 OK

GET https://api.agenziaviaggi.it/prenotazioni

Risposta:
HTTP/1.1 200 OK
[
    {
    "id": 1,
    "cliente_id": 1,
    'destinazione_id': 2,
    'data_partenza': '2024-07-15',
    'data_ritorno': '2024-07-25'},
    'prezzo_totale': 250.00
    },
    {
    'id': 2,
    'cliente_id': 2,
    'destinazione_id': 3,
    'data_partenza': '2024-08-11',
    'data_ritorno': '2024-08-20'},
    'prezzo_totale': 300.00
    }
]
'''

'''
Endpoint 2:
Metodo HTTP: POST
Endpoint: /clienti
Descrizione: Crea un nuovo cliente.
Codice di stato: 201 Created

POST https: //api.agenziaviaggi.it/clienti
Content-Type: application/json

{
    'id': 3,
    'nome': 'Luca',
    'cognome': 'Rossi',
    'email': 'luca.rossi@gmail.com',
    'telefono': '123456789'
   }

Risposta:
HTTP/1.1 201 Created
{
    'message': 'Cliente creato con successo',
    'cliente': {
        'id': 3,
        'nome': 'Luca',
        'cognome': 'Rossi',
        'email': 'luca.rossi@gmail.com',
        'telefono': '123456789'
}
'''

'''
Endpoint 3:
Metodo HTTP: PATCH
Endpoint: /viaggi/<viaggio_id>
Descrizione: Modifica parziale di un viaggio specifico.
Codice di stato: 200 OK, 404 Not Found

PATCH https://api.agenziaviaggi.it/viaggi/5
Content-Type: application/json

{
    'data_partenza': '2024-09-01',
    'data_ritorno': '2024-09-10'
    }

Risposta:
HTTP/1.1 200 OK
{
    'message': 'Viaggio aggiornato con successo',
    'viaggio': {
        'id': 5,
        'destinazione_id': 2,
        'data_partenza': '2024-09-01',
        'data_ritorno': '2024-09-10',
        'prezzo_totale': 400.00
        }
}

Risposta in caso di errore:
HTTP/1.1 404 Not Found
{
    'error': 'Viaggio non trovato'
}
'''

'''
Endpoint 4:
Metodo HTTP: POST
Endpoint: /destinazioni
Descrizione: Aggiunge una nuova destinazione.
Codice di stato: 201 Created

POST https://api.agenziaviaggi.it/destinazioni
Content-Type: application/json

{
    'id': 4,
    'nome': 'Bali',
    'paese': 'Indonesia',
    'descrizione': 'Isola tropicale con bellissime spiagge'
    }

Risposta:

HTTP/1.1 201 Created
{
    'message': 'Destinazione aggiunta con successo',
    'destinazione': {
        'id': 4,
        'nome': 'Bali',
        'paese': 'Indonesia',
        'descrizione': 'Isola tropicale con bellissime spiagge'
    }
}
'''

'''
Endpoint 5:
Metodo HTTP: PUT
Endpoint: /prenotazioni/<prenotazione_id>
Descrizione: Modifica totale di una prenotazione specifica.
Codice di Stato: 200 OK, 404 Not Found

PUT https://api.agenziaviaggi.it/prenotazioni/1
Content-Type: application/json

{
    'id': 1,
    'cliente_id': 1,
    'destinazione_id': 3,
    'data_partenza': '2024-10-05',
    'data_ritorno': '2024-10-15',
    'prezzo_totale': 350.00
    }

Risposta:
HTTP/1.1 200 OK
{
    'message': 'Prenotazione aggiornata con successo',
    'prenotazione': {
        'id': 1,
        'cliente_id': 1,
        'destinazione_id': 3,
        'data_partenza': '2024-10-05',
        'data_ritorno': '2024-10-15',
        'prezzo_totale': 350.00
    }
}

Risposta in caso di errore:
HTTP/1.1 404 Not Found
{
    'error': 'Prenotazione non trovata'}
'''