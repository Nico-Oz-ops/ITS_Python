
list_1 = [1, 9, 10]
x = list_1.pop() # Rimuove l'ultimo elemento della lista ma lo restituisce
# print(x)
# print(list_1)

list_2 = [1, 9, 10]
x = list_2.remove(10) # Rimuove l'elemento 10 dalla lista ma non lo restituisce
# print(x) # Stampa "None"
# print(list_2)

l = [1, 2, 3, 4, 5, "a"]
for x in l:
    # print(x) # Stampa tutti gli elementi della lista
    l.remove(x) # Rimuove tutti gli elementi della lista
# print(l) # Stampa una lista vuota


l = [1, 2, 3, 4, 5, "a"]
# for i in range(len(l) -1, -1, -1):
#     print("Sto rimuovendo l'elemento all'indice", i)
#     l.remove(l[i])


while len(l) > 0:
    x = l.pop()
    # print("Ho rimosso", x)


l1 = [1, 2, 3, 4, 5, "a", ["a", "b", "c"]]
print(l1)
l2 = l1.copy()
print(l2)
l1[6].append("d")
print(l1)
print(l2)
l1[-1] = 5
print(l1)
print(l2)