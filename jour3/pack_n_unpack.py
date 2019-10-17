# -*- coding: utf-8 -*-

def dire_bonjour(*args):
    for name in args:
        print(f"Bonjour {name}")
        
dire_bonjour("Toto", "Tata", 4)


def affichage_options(**kwargs):
    print(kwargs)
    
affichage_options(name="Toto", url="http://google.com")


def affichage_options(*args, **kwargs):
    print(args)
    print(kwargs)
    
affichage_options(4,8,7, name="Toto", url="http://google.com")


def multiplication(a, b):
    return a*b

args = [2,4]
print(multiplication(*args))