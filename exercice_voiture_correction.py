class Voiture:
    def __init__(self):
        self.essence = 100

    def afficher_reservoir(self):
        print(f" La voiture contient {self.essence}L d'essence.")

    def roule(self, km):

        if self.essence <= 0:
            print("Vous n'avez plus d'essence, faites le plein !")

        self.essence -= (km * 5) / 100

        if self.essence < 10:
            print("Vous n'avez bientôt plus d'essence !")
            return

        self.afficher_reservoir()

    def faire_le_plein(self):
        self.essence = 100
        print("Vous pouvez repartir !")


if __name__ == '__main__':
    ma_voiture = Voiture()
    print(ma_voiture.roule(25))
