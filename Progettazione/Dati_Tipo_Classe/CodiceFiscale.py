import re
from typing import Self

class CodiceFiscale(str):

    def __new__(cls, cf: str | Self) -> Self:

        cff: str = cf.upper().strip()
        
        if re.fullmatch(r"[A-Z]{6}[0-9]{2}[A-Z]{1}[0-9]{2}[A-Z]{1}[0-9]{3}[A-Z]{1}", cf):
            return super().__new__(cls, cff)
        raise ValueError(f"{cff} non è un codice fiscale italiano valido")