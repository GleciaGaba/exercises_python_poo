from dataclasses import dataclass


@dataclass
class Voiture:
    essence: int = 100

    def afficher_reservoir(self):
        print(f"La voiture contient {self.essence} litres d’essence")
        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")
        if self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")

    def roule(self, km):
        # Calcul de l'essence consommé
        consommation = (km * 5) / 100
        self.essence -= consommation
        self.afficher_reservoir()

    def faire_le_plein(self, essence):
        if essence < 10:
            self.essence = 100
            print("Vous pouvez repartir !")
        else:
            print("Vous avez encore assez d'essence.")


if __name__ == '__main__':
    ma_voiture = Voiture()
    print(ma_voiture.roule(100))
