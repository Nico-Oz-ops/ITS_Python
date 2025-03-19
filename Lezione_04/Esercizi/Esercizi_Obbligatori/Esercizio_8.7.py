# 8.7 - Album

def make_album(artista, album, song=None) -> dict[str]:
    return{"Nome_Artista": artista, "Album": album, "Canzoni": song}

print(make_album("Red Hot Chili Peppers", "Blood Sugar Sex Magik"))
print(make_album("Red Hot Chili Peppers", "One Hot Minute"))
print(make_album("Red Hot Chili Peppers", "Mother's Milk", 10))

