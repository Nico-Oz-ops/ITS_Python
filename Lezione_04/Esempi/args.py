# 1 - *args

mylist = [1, 2, 3, 4, 5]
print(mylist)

print(*mylist) # "scompone" gli elementi della lista e li passa come argomenti separati alla funzione print()


# Somma di 5 numeri dati
def somma(*args):
    return sum(args)

print(somma(1, 2, 3, 4, 5))

# 2 

# def add(*args): # accepts multiple numbers in input
    # total = 0
    # for number in args:
    #     total += number
    # return total

# print(add(2, 3))
# print(add(10, 20, 30))

# 3

# def total_price(*args):
#     total:float = sum(args)
#     return total

# print(total_price(2.99, 4.55, 2.99)) # stampa la somma di tutti i prezzi ma non si sa di cosa. Bisgona usare **kwargs

# 4 - uso di **kwargs

# def total_price(**kwargs):
#     total:float = 0
#     for product, price in kwargs.items():
#         print(f"{product}: {price}£")
#         total += price
    # print(f"Total: {round(total, 2)}£") # stampa il totale
    # return round(total, 2) # restituisce il totale, ma non lo stampa

# (total_price(coffee=2.99, cake=4.55, juice=2.99)) # chiamata della funzione

# 5 

# def nome_funzione(*args, **kwargs) -> None:
#     print(args, kwargs)

# nome_funzione()
# nome_funzione("valore1", "valore2", chiave1 = "valore1")

# 6

# def nome_funzione_2(x, y, *args, **kwargs) -> None:
#     for key, value in kwargs.items():
#         if key == "chiave1":
#             print(value)
#         elif key == "chiave2":
#             print(value)
#         else:
#             raise ValueError("Chaive non riconosciuta")
#         print("Parametro non riconosciuto")

# nome_funzione_2("valore1", "valore2", chiave1 = "valore1")

