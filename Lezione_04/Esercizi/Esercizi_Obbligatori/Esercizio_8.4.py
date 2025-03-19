# 8.4 - Large Shirts

def make_shirt(size="large", text="I love Python"):
    return f"La maglia di taglia {size} ha il messaggio \"{text}\""

print(make_shirt())
print(make_shirt("large e medium"))
print(make_shirt("large e medium"))
print(make_shirt("small", "BOOM!"))