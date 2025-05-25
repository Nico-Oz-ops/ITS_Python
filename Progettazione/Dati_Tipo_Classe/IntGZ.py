from typing import Self

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