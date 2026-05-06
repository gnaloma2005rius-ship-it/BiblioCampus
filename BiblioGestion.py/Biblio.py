# Application simple de gestion de bibliothèque (console)
# Langage : Python

class Livre:
    def __init__(self, id_livre, titre, auteur):
        self.id = id_livre
        self.titre = titre
        self.auteur = auteur
        self.disponible = True

    def __str__(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        return f"[{self.id}] {self.titre} - {self.auteur} ({statut})"


class Bibliotheque:
    def __init__(self):
        self.livres = {}

    def ajouter_livre(self, livre):
        self.livres[livre.id] = livre
        print("Livre ajouté avec succès.")

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
        for livre in self.livres.values():
            print(livre)

    def emprunter_livre(self, id_livre):
        livre = self.livres.get(id_livre)
        if livre and livre.disponible:
            livre.disponible = False
            print("Livre emprunté.")
        else:
            print("Livre indisponible ou inexistant.")

    def retourner_livre(self, id_livre):
        livre = self.livres.get(id_livre)
        if livre and not livre.disponible:
            livre.disponible = True
            print("Livre retourné.")
        else:
            print("Erreur lors du retour.")

    def supprimer_livre(self, id_livre):
        if id_livre in self.livres:
            del self.livres[id_livre]
            print("Livre supprimé.")
        else:
            print("Livre introuvable.")


def menu():
    biblio = Bibliotheque()

    while True:
        print("\n--- MENU ---")
        print("1. Ajouter un livre")
        print("2. Afficher les livres")
        print("3. Emprunter un livre")
        print("4. Retourner un livre")
        print("5. Supprimer un livre")
        print("6. Quitter")

        choix = input("Choix : ")

        if choix == "1":
            id_livre = input("ID : ")
            titre = input("Titre : ")
            auteur = input("Auteur : ")
            livre = Livre(id_livre, titre, auteur)
            biblio.ajouter_livre(livre)

        elif choix == "2":
            biblio.afficher_livres()

        elif choix == "3":
            id_livre = input("ID du livre : ")
            biblio.emprunter_livre(id_livre)

        elif choix == "4":
            id_livre = input("ID du livre : ")
            biblio.retourner_livre(id_livre)

        elif choix == "5":
            id_livre = input("ID du livre : ")
            biblio.supprimer_livre(id_livre)

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Choix invalide.")


if __name__ == "__main__":
    menu()
