# -*- coding: utf-8 -*-

class Personne:
    
    def __init__(self, nom_init, prenom_init, age_init=42):
        self.nom = nom_init
        self.prenom = prenom_init
        self.age = age_init
    
    def dire_bonjour(self, autre_personne):
        print(f"Bonjour {autre_personne.prenom}. Je m'appelle {self.prenom}")
    

une_personne = Personne("Parker", "Tony")
une_autre_personne = Personne("Lavillenie", "Renaud", age_init=33)

print(une_personne.nom)
print(une_autre_personne.nom)

print(une_personne.age)
print(une_autre_personne.age)

une_personne.dire_bonjour(une_autre_personne)

print(une_personne)