# Esercizio 9
'''Magliette grandi: modifica la funzione make_shirt() in modo che le magliette siano grandi di default 
con un messaggio che recita I love Python. Crea una maglietta grande e una maglietta media con il messaggio 
di default e una maglietta di qualsiasi taglia con un messaggio diverso.'''

def make_shirt(taglia="large", frase="I love Python"):
    print(f"Il messaggio della maglietta, di taglia \"{taglia}\", dice: \"{frase}\".")

make_shirt()
make_shirt(taglia="media")
make_shirt(taglia="small", frase="Non mi piace Java...the Hutt")