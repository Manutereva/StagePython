# -*- coding: utf-8 -*-

def assertStr(f):
    print("décoration")
    def nouvelle_fonction(*args):
        for name in args:
            assert type(name) == str, "error arg should be str"
        return f(*args).upper()
    
    return nouvelle_fonction



@assertStr
def dire_bonjour(name, name2="Tata"):
    return f"Bonjour {name}, {name2}"

@assertStr
def demander_lheure(name):
    return f"Bonjour {name}. Quel heure est-il ?"


print(dire_bonjour("Toto", "Titi"))
#print(dire_bonjour(2))
print(dire_bonjour("Toto"))
print(demander_lheure("Toto"))

