stringa = input("Inserire una stringa: ")
invertita = "" #questa variabile conterra la stringa invertita.

for i in range(len(stringa) -1, -1, -1): #uso di ciclo for per scorrere la stringa al contrario.
    invertita += stringa[i] #ad ogni iterazione, il carattere all'indice [i] viene aggiunto alla variabile invertita.
    
print(f"La stringa \"{stringa}\" invertita diventa: \"{invertita}\"")


