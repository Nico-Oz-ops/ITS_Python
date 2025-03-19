x = int(input("Inserire una coordinata X: "))
y = int(input("Inserire una coordinata Y: "))

punto = (x, y)

match punto:
    case (0, 0):
        print("Il punto si trova nell'origine")
    case (x, 0):
        print(f"Il punto si trova sull'asse X: {x}")
    case (0, y):
        print(f"Il punto si trova sull'asse Y: {y}")
    case punto if x > 0 and y > 0:
        print("Il punto si trova nel primo quadrante")
    case punto if x < 0 and y > 0:
        print("Il punto si trova nel secondo quadrante")       
    case punto if x < 0 and y < 0:
        print("Il punto si trova nel terzo quadrante")   
    case punto if x > 0 and y < 0:
        print("Il punto si trova nel quarto quadrante") 




# case _:
# print(f"Punto generico: ({x}, {y})")