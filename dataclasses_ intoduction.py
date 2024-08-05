"""
Introduction aux Dataclasses
Les dataclasses simplifient la création de classes en fournissant des décorateurs et des
fonctions pour réduire le code boilerplate. Par exemple, elles gèrent automatiquement la
création des méthodes
__init__,
__repr__,
__eq__,
etc.

from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int


La Méthode __post_init__

Parfois, il est nécessaire d'exécuter du code supplémentaire après que
l'initialisation automatique a eu lieu. C'est ici que la méthode __post_init__
entre en jeu. Cette méthode est appelée automatiquement après que le constructeur
__init__ généré par dataclass a été appelé.


def __post_init__(self):
        # Par exemple, nous voulons nous assurer que x et y sont positifs
        if self.x < 0 or self.y < 0:
            raise ValueError("Les coordonnées doivent être positives")

"""
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0:
            raise ValueError("L'âge ne peut pas être négatif")


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = 0

    def __post_init__(self):
        self.area = self.width * self.height


@dataclass
class Circle:
    radius: float
    diameter: float = 0

    def __post_init__(self):
        self.diameter = self.radius * 2
