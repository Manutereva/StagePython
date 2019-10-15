# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:41:26 2019

@author: miguel
"""

def dire_bonjour():
    print("Bonjour")

def say_hello():
    print("Bonjour")

def fala_bom_dia():
    print("Bonjour")

dico = {
        "FR": dire_bonjour,
        "EN": say_hello,
        "PT": fala_bom_dia
}

dico["FR"]()

func = lambda arg : arg * 2

print(func(4))

liste = [4,8,1,3]

l = map(type, liste)
print(list(l))
