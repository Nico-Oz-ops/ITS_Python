'''
Esercizio 10 – Sistema di notifiche (avanzato)

Tema: Polimorfismo avanzato + astrazione
Obiettivo: Creare un sistema estensibile di notifiche.
Traccia:
Crea una classe astratta Notifica con metodo invia(messaggio).
Sottoclassi:

Email (stampa: “Invio email: …”)

SMS (stampa: “Invio SMS: …”)

Push (stampa: “Invio notifica push: …”)

Crea una funzione invia_notifiche(lista_notifiche, messaggio) che, 
con un unico ciclo, invia lo stesso messaggio su tutti i canali.
'''