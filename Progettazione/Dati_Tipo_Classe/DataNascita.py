from datetime import date
from typing import Self

class DataGE1895(date):
    # Tipo di dato specializzato Data 

    def __new__(cls, year, month, day):
        if year < 1895:
            raise ValueError(f"La data {day}/{month}/{year} deve essere successiva all'1 gennaio 1895")
        
        return super().__new__(cls, year=year, month=month, day=day)

def build_int_ge_v(n: int) -> Type:
    class IntGZV(int):
    # Tipo di dato specializzato Intero > 0

        def __new__(cls, v: Self | int | float | str | bool):

            value: int = super().__new__(cls, v)

            if value <= n:
                raise ValueError(f"The value {v} must be greater than zero")
            return value
    return IntGZV
