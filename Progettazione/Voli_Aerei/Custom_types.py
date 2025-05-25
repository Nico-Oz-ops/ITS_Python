import re
from typing import Self
from datetime import date

class CodiceFiscale(str):

    def __new__(cls, cf: str | Self) -> Self:

        cff: str = cf.upper().strip()
        
        if re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", cf):
            return super().__new__(cls, cff)
        raise ValueError(f"{cff} non è un codice fiscale italiano valido")

class DataGE1895(date):
    # Tipo di dato specializzato Data 

    def __new__(cls, year, month, day):
        if year < 1895:
            raise ValueError(f"La data {day}/{month}/{year} deve essere successiva all'1 gennaio 1895")
        
        return super().__new__(cls, year=year, month=month, day=day)

class Telefono(str):

    def __new__(cls, tel: str | Self) -> Self:
        
        if re.fullmatch(r"^\d{10}$", tel):
            return super().__new__(cls, tel)
        raise ValueError(f"{tel} non è un numero di telefono italiano valido")
    
class Email(str):

    def __new__(cls, email: str | Self) -> Self:
        
        if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
            return super().__new__(cls, email)
        raise ValueError(f"{email} non è una email valida")

class IntGZ(int):
    # Tipo di dato specializzato Intero > 0

    def __new__(cls, v: Self | int | float | str | bool):

        value: int = super().__new__(cls, v)

        if value <= 0:
            raise ValueError(f"The value {v} must be greater than zero")
        return value
    
    # Attenzione: in generale la differenza tra interi non dovrebbe essere toccata
    def __sub__(self, other: int | Self) -> Self:
        other_int : int = int(other)
        
        try:
            res: int = int(self) - other_int
            return IntGZ(res)
        except ValueError:
            raise ValueError(f"The difference between {self} and {other} is not an IntGZ")
