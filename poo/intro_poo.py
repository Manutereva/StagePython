# -*- coding: utf-8 -*-

class MinimumAgeError(Exception):
    def __init__(self, ma_personne, autre_personne):
        self.ma_personne = ma_personne
        self.autre_personne = autre_personne


class Personne:
    
    def __init__(self, nom_init, prenom_init, age_init=42):
        assert type(age_init) == int, "L'age doit être un entier"
        assert age_init >= 0, "L'age doit être supérieur à zéro"
        self.nom = nom_init
        self.prenom = prenom_init
        self.age = age_init
    
    def draguer(self, autre_personne):
        if autre_personne.age < 18:
            raise MinimumAgeError(self, autre_personne)
            
        print(f"Hello {autre_personne.prenom}")
        
    def dire_bonjour(self, autre_personne):
        assert type(autre_personne) == Personne, \
            "autre_personne doit être une personne"
        print(f"Bonjour {autre_personne.prenom}. Je m'appelle {self.prenom}")
    
try:
    une_personne = Personne("Parker", "Tony")
    une_autre_personne = Personne("Lavillenie", "Renaud", age_init=17)
    
    print(une_personne.nom)
    print(une_autre_personne.nom)
    
    print(une_personne.age)
    print(une_autre_personne.age)
    
    une_personne.dire_bonjour(une_autre_personne)
    #une_personne.dire_bonjour(42)
    
    une_personne.draguer(une_autre_personne)

    print("Suite")
except MinimumAgeError as e:
    print(f"Trop jeune {e.ma_personne.age}")
except:
    print("Error")

print(une_personne)