from typing import Self
from datetime import date
import re

# Tipi di dato di classe
'''
Durata
Abitanti
Data(Anno)
Codice Aeroporto
Codice Volo
'''

class Durata(int):
    def __new__(cls, minuti: Self | int | float | str | bool) -> Self:
        if minuti < 0:
            raise ValueError(f"La durata deve essere maggiore di zero")
        return super().__new__(cls, minuti)

 
class Abitanti(int):
    def __new__(cls, a: Self | int | float | str | bool) -> Self:
        value: int = super().__new__(cls, a)
        if value < 0:
            raise ValueError(f"Il valore {a} deve essere maggiore di zero.")
        return value 

 
class Data1900(int):
    def __new__(cls, year: int) -> Self:
        if year < 1900 or year > date.time.today():
            raise ValueError(f"L'anno {year} non è valido.")
        return super().__new__(cls, year=year)

 
class CodiceAeroporto(str):
    def __new__(cls, codice_aeroporto: str | Self) -> Self:
        cod_aeroporto: str = codice_aeroporto.upper().strip()
        if not re.fullmatch(r'^[A-Z]{3}$', cod_aeroporto):
            raise ValueError(f"Il codice dell'aeroporto {cod_aeroporto} deve essere composto da 3 lettere maiuscole.")
        return super().__new__(cls, cod_aeroporto)
 

class CodiceVolo(str):
    def __new__(cls, codice_volo: str | Self) -> Self:
        cod_volo: str = codice_volo.upper().strip()
        if not re.fullmatch(r'^\b[A-Z]{2}\d{1,4}\b$', cod_volo):
            raise ValueError(f"Il codice del volo {cod_volo} non è valido.")
        return super().__new__(cls, cod_volo)