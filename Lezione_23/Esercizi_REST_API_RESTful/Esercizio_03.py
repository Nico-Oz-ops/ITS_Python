'''
3. Analisi JSON: Ecco un oggetto JSON relativo a una prenotazione di campo da tennis: 

Content-Type: application/json
{
   'id': 12,
   'cliente': 'Luca Neri', 
   'campo': 3, 
   'data': '2025-03-20', 
   'ora': '18:00', 
   'durata_ore': 2
}

BASE URL: https://api.esempio.it

Individua la risorsa e utilizza i metodi HTTP per crea una nuova prenotazione con i dati forniti, 
modificare l'intera prenotazione, e creare una nuova prenotazione con dati differenti. 
Indica anche il codice di stato corretto. 
'''



'''
Metodo HTTP: POST
Endpoint: /prenotazioni
Descrizione: Crea una nuova prenotazione con i dati forniti.
Codice di stato: 201 Created

POST https://api.esempio.it/prenotazioni
Content-Type: application/json
{
   'id': 12,
   'cliente': 'Luca Neri',
   'campo': 3,
   'data': '2025-03-20',
   'ora': '18:00',
   'durata_ore': 2
   }

Risposta:
HTTP/1.1 201 Created
{
   'message': 'Prenotazione creata con successo',
   'prenotazione': {
       'id': 12,
       'cliente': 'Luca Neri',
       'campo': 3,
       'data': '2025-03-20',
       'ora': '18:00',
       'durata_ore': 2
   }
}
'''

'''
Metodo HTTP: PUT
Endpoint: /prenotazioni/12
Descrizione: Modifica l'intera prenotazione con i nuovi dati forniti.
Codice di stato: 200 OK

PUT https://api.esempio.it/prenotazioni/12
Content-Type: application/json
{
    'id': 12,
    'cliente': 'Luca Neri',
    'campo': 3,
    'data': '2025-03-21',  # Nuova data
    'ora': '19:00',       # Nuova ora
    'durata_ore': 1       # Nuova durata}

Risposta:
HTTP/1.1 200 OK
{
    'message': 'Prenotazione aggiornata con successo',
    'prenotazione': {
        'id': 12,
        'cliente': 'Luca Neri',
        'campo': 3,
        'data': '2025-03-21',
        'ora': '19:00',
        'durata_ore': 1
    }
}
'''

'''
Metodo HTTP: POST
Endpoint: /prenotazioni
Descrizione: Crea una nuova prenotazione con dati differenti.
Codice di stato: 201 Created

POST https://api.esempio.it/prenotazioni
Content-Type: application/json

{
   'id': 13,
   'cliente': 'Rosamel Fierro Delgado',
   'campo': 2,
   'data': '2025-04-25',
   'ora': '15:30',
   'durata_ore': 1
   }

Risposta:
HTTP/1.1 201 Created
{
    'message': 'Prenotazione creata con successo',
    'prenotazione': {
        'id': 13,
        'cliente': 'Rosamel Fierro Delgado',
        'campo': 2,
        'data': '2025-04-25',
        'ora': '15:30',
        'durata_ore': 1
   }
}
'''

'''
Metodo HTTP: POST
Endpoint: /prenotazioni
Descrizione: Crea una nuova prenotazione con dati differenti.
Codice di stato: 201 Created

POST https://api.esempio.it/prenotazioni
Content-Type: application/json

{
   'id': 13,
   'campo': 2,
   'data': '2025-04-25',
   'ora': '15:30',
   'durata_ore': 1
   }

Risposta:
HTTP/1.1 400 Bad Request
{
    "error": "Bad Request",
    "message": "Il campo 'cliente' è obbligatorio"
}
'''


