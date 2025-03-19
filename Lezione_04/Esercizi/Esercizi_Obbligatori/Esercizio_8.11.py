# Esercizio 8.11 - Messaggi archiviati

testo_messaggio = [
    "Hola",
    "Ciao",
    "buenas",
]
testo_messaggio_archiviato = testo_messaggio[:]
sent_messages = []

def send_messages():
    
    while testo_messaggio:
        
        messaggio = testo_messaggio.pop(0)
        print(f"Inviando messaggio: {messaggio}")

        sent_messages.append(messaggio)

send_messages()

print(f"Lista dei messaggi originali: {testo_messaggio}")
print(f"Lista dei messaggi inviati: {sent_messages}")
print(f"Lista dei messaggi archiviati: {testo_messaggio_archiviato}")
