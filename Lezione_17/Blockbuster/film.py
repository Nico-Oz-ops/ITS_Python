from __future__ import annotations

class Film:
    def __init__(self, id_film: int, title: str):
        self.setId(id_film)
        self.setTitle(title)
    
    def getId(self):
        return self.__id_film
    
    def getTitle(self):
        return self.__title
    
    def setId(self, id_film: int):
        if not isinstance(id_film, int) or id_film < 0:
            raise ValueError("ID non valido")
        self.__id_film = id_film
    
    def setTitle(self, title: str):
        if not isinstance(title, str) or title.strip() == "":
            raise ValueError()
        self.__title = title
    
    def isEqual(self, otherfilm):
        if isinstance(otherfilm, Film):
            return self.__id_film == otherfilm.__id_film
        return False
    
