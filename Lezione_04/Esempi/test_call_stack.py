def alpha():
    print("Executing alpha")

def beta():
    alpha()
    print("Executing beta")

def gamma():
    print("Executing gamma")
    beta()

gamma()

'''
Output:
Executing gamma
Executing alpha
Executing beta


Ordine esecuzione: 
gamma() -> beta() -> alpha()


Ordine rimozione: 
alpha() -> beta() -> gamma()

'''

