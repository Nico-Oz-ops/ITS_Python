# Esercizio 01
'''
'''
import re

# versione RegEx
def is_integer(s:str):
    if not isinstance(s, str):
        return False

    s = s.strip()   
    return re.fullmatch(r"[+-]?\d+", s) is not None


print(is_integer("-456"))
print(is_integer("   12 "))
print(is_integer("abc"))
print(is_integer("+789"))
print(is_integer("15"))

print("-" * 50)

def is_integer(s):
    return bool(re.match(r"[+-]?\d+", s))

print(is_integer("123"))
print(is_integer("-456"))
print(is_integer("12.3"))

print("-" * 50)

# versione funzione
def is_integer1(s:str):
    if not isinstance(s, str):
        return False
    
    s = s.strip()

    if s.startswith("-") or s.startswith("+"):
        s = s[1:]
    return s.isdigit()

print(is_integer1("-456"))
print(is_integer1("   12 "))
print(is_integer1("abc"))
print(is_integer1("+789"))
print(is_integer1("15"))