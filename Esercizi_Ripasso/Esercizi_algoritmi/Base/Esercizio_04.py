# Esercizio 4
'''
Palindromo
Verifica se una parola (es: "radar", "anna") è un palindromo.
'''

def palindromo(my_string: str) -> str:
    
    my_string = my_string.lower()
    return my_string == my_string[::-1]

   

print(palindromo("anna"))
print(palindromo("radar"))
print(palindromo("TOPO"))