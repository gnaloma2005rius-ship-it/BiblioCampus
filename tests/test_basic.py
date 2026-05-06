import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from books import ajouter_livre
from loans import emprunter_livre, rendre_livre
from stats import afficher_stats

def test_emprunter_livre():
    donnees = {"livres": [], "emprunts": []}
    ajouter_livre(donnees, "Python avancé", "Dupont")
    msg = emprunter_livre(donnees, "Python avancé")
    assert "emprunté avec succès" in msg
    print("✅ test_emprunter_livre OK")

def test_rendre_livre():
    donnees = {"livres": [], "emprunts": []}
    ajouter_livre(donnees, "Python avancé", "Dupont")
    emprunter_livre(donnees, "Python avancé")
    msg = rendre_livre(donnees, "Python avancé")
    assert "rendu avec succès" in msg
    print("✅ test_rendre_livre OK")

def test_livre_deja_emprunte():
    donnees = {"livres": [], "emprunts": []}
    ajouter_livre(donnees, "Git pour tous", "Martin")
    emprunter_livre(donnees, "Git pour tous")
    msg = emprunter_livre(donnees, "Git pour tous")
    assert "déjà emprunté" in msg
    print("✅ test_livre_deja_emprunte OK")

def test_stats():
    donnees = {"livres": [], "emprunts": []}
    ajouter_livre(donnees, "Python avancé", "Dupont")
    ajouter_livre(donnees, "Git pour tous", "Martin")
    emprunter_livre(donnees, "Python avancé")
    afficher_stats(donnees)
    print("✅ test_stats OK")

if __name__ == "__main__":
    test_emprunter_livre()
    test_rendre_livre()
    test_livre_deja_emprunte()
    test_stats()
    print("\n✅ Tous les tests C passent !")

