from typing import Any
import re

class Indirizzo:
	# campi dati:
	# _via:str
	# _civico:...
	def __init__(self, via:str, civico:str):
		if via is None:
			raise ValueError(f"via cannot be None")
		if civico is None:
			raise ValueError(f"civ cannot be None")
		
		self._via:str = via

		if not re.fullmatch(r"^[0-9]+[a-zA-Z]*$", civico):
			raise ValueError(f"value for civico '{civico}' not allowed")
		self._civico:str = civico
	
	def via(self)->str:
		return self._via
	def civico(self)->str:
		return self._civico

	def __repr__(self)->str:
		return f"Indirizzo(via={self.via()}, civico={self.civico()})"


	# class Indirizzo implementa un tipo di dato: Python deve riconoscere se oggetti diversi rappresentano lo stesso valore
	def __hash__(self)->int:
		return hash( (self.via(), self.civico()) )

	def __eq__(self, other:Any)->bool:
		if other is None or \
				not isinstance(other, type(self)) or \
				hash(self) != hash(other):
			return False
		return (self.via(), self.civico() ) == (other.via(), other.civico())