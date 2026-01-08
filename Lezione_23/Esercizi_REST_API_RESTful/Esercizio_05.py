'''
5. Livelli di Maturità REST: ti vengono mostrati esempi di API. 
Indica per ciascuno il livello di maturità (0-3) secondo il modello di Richardson.
'''

# Esempio 1
'''
POST 
https://api.esempio.it/api
Content-Type: application/json
{
  "action": "crea_prenotazione",
  "payload": {
   "cliente": "Sara Bianchi",
   "campo": 1,
   "data": "2025-04-05",
   "ora": "07:30",
   "durata_ore": 1.5
   }
}

POST 
https://api.esempio.it/api
Content-Type: application/json
{
  "action": "recupera_prenotazione",
  "payload": {
   "cliente_id": 4
   }
}

Livello di maturità: 0
'''

# Esempio 2
'''
POST 
https://api.esempio.it/prenotazioni
Content-Type: application/json
{
    "cliente": "Sara Bianchi",
    "campo": 1,
    "data": "2025-04-05",
    "ora": "07:30",
    "durata_ore": 1.5
}

GET 
https://api.esempio.it/utenti
Content-Type: application/json
{
    "cliente_id": 4
}
Livello di maturita: 1
'''

# Esempio 3
'''
POST 
https://api.esempio.it/prenotazioni
Content-Type: application/json
{
    "cliente": "Sara Bianchi",
    "campo": 1,
    "data": "2025-04-05",
    "ora": "07:30",
    "durata_ore": 1.5
}

HTTP/1.1 201 Created
Content-Type: application/json
{
  "id": 57,
  "cliente": "Sara Bianchi",
  "campo": 1,
  "data": "2025-04-05",
  "ora": "07:30",
  "durata_ore": 1.5,
  "stato": "prenotata",
  "_links": {
    "self": { "href": "/prenotazioni/57", "method": "GET" },
    "update": { "href": "/prenotazioni/57", "method": "PATCH" },
    "cancel": { "href": "/prenotazioni/57", "method": "DELETE" },
    "list": { "href": "/prenotazioni?data=2025-04-05", "method": "GET" },
    "payment": { "rel": "capture", "href": "/pagamenti", "method": "POST",
                 "body_schema": { "prenotazione_id": "number", "importo": "number" } }
  }
}
Livello di maturità: 3
'''

# Esempio 4
'''
POST 
https://api.esempio.it/prenotazioni
Content-Type: application/json
{
  "action": "crea_prenotazione",
  "payload": {
   "cliente": "Sara Bianchi",
   "campo": 1,
   "data": "2025-04-05",
   "ora": "07:30",
   "durata_ore": 1.5
   }
}

POST 
https://api.esempio.it/utenti
Content-Type: application/json
{
  "action": "recupera_prenotazione",
  "payload": {
   "cliente_id": 4
   }
}
Livelo di maturità: 0
'''