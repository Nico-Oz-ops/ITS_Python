'''
Tema: Ricorsione su stringhe
Obiettivo: Rafforzare l’uso della ricorsione con condizioni personalizzate
'''

# Esercizio 04
# Titolo: "Conta le vocali accentate"

'''
Traccia dell’esercizio:
Scrivi una funzione ricorsiva count_vocali_accentate(s: str) -> int che 
conta quante vocali accentate ci sono in una stringa.

Considera queste vocali accentate:
à, è, é, ì, ò, ù

Suggerimento (facoltativo):
Puoi usare una stringa con tutte le vocali accentate 
da confrontare con il primo carattere minuscolo.
'''

def count_vocali_accentate(s: str) -> int:
    if s == "":
        return 0
    
    primo = s[0].lower()
    resto = s[1:]

    if primo in "àèéìòù":
        return 1 + count_vocali_accentate(resto)
    else:
        return count_vocali_accentate(resto)

print(count_vocali_accentate("perché è così com'è"))     
print(count_vocali_accentate("là dove l'accento c’è"))    
print(count_vocali_accentate("nessun accento"))           
print(count_vocali_accentate(""))              