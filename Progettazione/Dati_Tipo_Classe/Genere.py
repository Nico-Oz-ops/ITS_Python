import re
from typing import Self

class Telefono(str):

    def __new__(cls, tel: str | Self) -> Self:
        
        if re.fullmatch(r"^\d{10}$", cf):
            return super().__new__(cls, tel)
        raise ValueError(f"{tel} non è un codice fiscale italiano valido")
    
class Email(str):

    def __new__(cls, email: str | Self) -> Self:
        
        if re.fullmatch(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$", email):
            return super().__new__(cls, email)
        raise ValueError(f"{email} non è una email valida")