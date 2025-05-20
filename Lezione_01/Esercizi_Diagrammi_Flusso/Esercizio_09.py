# Esercizio 09 - Classifica delle vendite

nome = input("Inserire il nome di un venditore: ").title()
vendita = float(input("Inserire la sua vendita: "))

max_nome = nome
max_vendita = vendita
min_nome = nome
min_vendita = vendita
cont = 0

for cont in range(5):
    new_nome = input("Inserire il nome di un'altro venditore: ").title()
    new_vendita = float(input("Inserire la sua vendita: "))

    if new_vendita > max_vendita:
        max_nome = new_nome
        max_vendita = new_vendita
    else:
        if new_vendita < min_vendita:
            min_nome = new_nome
            min_vendita = new_vendita
    cont += 1

print(f"{max_nome} è il venditore con la vendita più alta, cioè: ${max_vendita: .2f}.")
print(f"{min_nome} è il venditore con la vendita più bassa, cioè: ${min_vendita: .2f}.")
        


