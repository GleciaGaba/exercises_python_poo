# classe
class Voiture:
    # attribut de classe
    voitures_crees = 0

    # méthode
    def __init__(self, marque):
        Voiture.voitures_crees += 1
        # attribut d'instance
        self.marque = marque

    def afficher_marque(self):
        print(f"La voiture est une {self.marque}")


# instance
voiture_01 = Voiture("Lamborghini")
voiture_02 = Voiture("Porsche")

print(voiture_01.marque)
print(voiture_02.marque)
print(Voiture.voitures_crees)
voiture_01.afficher_marque()
Voiture.afficher_marque(voiture_01)
