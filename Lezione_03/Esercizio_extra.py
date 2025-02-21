'''Data una stringa contenente solo i caratteri '(' e ')'
restituire True se le parentesi sono "bilanciate, e False altrimenti.
Ad esempio:
bilanciate("((()))") -> True
bilanciate("(()") -> False
bilanciate("()()()") -> True
bilanciate("))((") -> False
bilanciate("(()())") -> True'''

count = 0
bilanciate = True
stringa = input("Inserire una stringa di parentesi:")

for carattere in stringa:
    if carattere == "(":
        count += 1
    elif carattere == ")":
        count -= 1
    if count < 0:
        bilanciate = False
        break

if count != 0:
    bilanciate = False

print(bilanciate)
