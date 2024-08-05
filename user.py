from dataclasses import dataclass
from typing import ClassVar

"""class User:
    def __int__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
     Avec la méthode dataclasses    
        
        """


@dataclass
class User:
    first_name: str
    last_name: str

    # on peux ajouter des valeurs par default
    # >>>full_name: str = ""
    # >>>si on veut créer un attribut de classe
    # c: ClassVar[int]

    def __post_init__(self):
        self.full_name = f"{self.first_name} {self.last_name}"


patrick = User(first_name="Patrick", last_name="Smith")
print(patrick.full_name)
