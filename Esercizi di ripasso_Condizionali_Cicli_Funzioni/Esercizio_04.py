# Esercizio 4

def integerPower(base:int, esponente:int) -> int:
        
        if esponente <= 0:
            return "Errore"
        
        result = 1
        for i in range(esponente):
            result *= base
            
        return result

print(integerPower(3, 4))
print(integerPower(2, 5))
print(integerPower(2, -5))
print(integerPower(2, 0))
            