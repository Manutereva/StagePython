#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = 3
a = 3.2
a = True or False
a = None
a = 2j * 1j
print(a)
print(a)
print(type(a))

a = "Bonjour tout le monde"
a = [2, 4, 1, 6]
print(type(a))


# In[20]:


ma_liste = [2, 4, 1, 6]
ma_liste[0]
ma_liste[-1]
ma_liste[-2]

toto = "Tata"
ma_liste = [True, 2, 3.2, [2,1,6]]
ma_liste[3][1]
[0]*10
len(ma_liste)
ma_liste.remove(3.2)
ma_liste.pop(0) # Recherche sur l'indice pour retirer
ma_liste.append(toto)
ma_liste


# In[35]:


ma_liste = [4,1,7,5,12,8,15]
ma_liste[1:4]
ma_liste[:4]
ma_liste[2:]
ma_liste[2:-1]
ma_liste[2::2] # Pas de 2 en 2

ma_liste[::-2] # Pas de 2 en 2 en sens inverse


# In[39]:


ma_liste = [4,1,7,5,12,8,15]
# Récupérer du 3e à l'avant dernier
# Récupérer les 4 premiers éléments
# Récupérer les 5 derniers éléments
# Récupérer 2e, 4e, 6e
# Récupérer de l'avant dernier au 2e (sens inverse)
print(ma_liste[2:-1])
print(ma_liste[:4])
print(ma_liste[-5:])
print(ma_liste[1:6:2])
print(ma_liste[-2:0:-1])


# In[42]:


a = 2

while a < 18:
    print("A = " + str(a))
    a *= -2 # a = a + 1
    print(a)
print("Bonjour")


# In[51]:


for elm in [2,True,None,8]:
    print(elm)
    
# for elm in range(10):
#     print(elm)
    
# for elm in range(4,10):
#     print(elm)

ma_liste = [2,True,1,8]
for i in range(len(ma_liste)):
    print(ma_liste[i])
    


# In[61]:


liste_prenoms = [
    "Martin",
    "Elise",
    "Mathieu"
]
liste_ages = [23, 43, 12, 56]

for prenom, age in zip(liste_prenoms, liste_ages):
    print(f"Prenom : {prenom} et age : {age}")
    
for i, val in enumerate(liste_prenoms):
    print(f"prenom n {i} : {val}") # f-string en python 3 seulement

for i, val in enumerate(liste_prenoms):
    print("prenom n %d : %s"%(i, val)) # old school : Python 2 et 3


# In[56]:


age = 25

if age < 18:
    print("Mineur")
elif age > 18:
    print("Majeur")
else:
    print("Joyeux anniversaire")

    


# In[59]:


age = 6

if age % 2 == 0:
    print("pair")
elif age % 3 == 0:
    print("impair et multiple de 3")

    
# Condition indépendante
if age % 2 == 0:
    print("pair")

if age % 3 == 0:
    print("multiple de 3")


# ## FizzBuzz
# 
# Pour tous les entiers de 0 à 100
# * Afficher fizz si l'entier est multiple de 3
# * Afficher buzz si l'entier est multiple de 5
# * Afficher bazz si l'entier est multiple de 5 et 3
# * Sinon on affiche l'entier
# 
# ### Résulat :
# * bazz
# * 1
# * 2
# * fizz
# * 4
# * buzz
# * fizz
# ...

# In[63]:


for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("bazz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)


# In[64]:


a = range(100)
print(a)


# In[65]:


a = list(range(100))
print(a)


# In[69]:


nom = input("Quel est votre nom ?")
age = int(input("Quel est votre age ?")) # int( ) pour conversion en entier

print(f"votre nom est {nom} et votre age est {age}.")

print(f"L'année prochaine vous aurez {age + 1}.")


# In[67]:


print(nom)


# In[72]:


from random import randint

nb_secret = randint(0,100)
proposition = -1
# !=
# Tant que l'utilisateur n'a pas trouvé le secret
# On lui demande de faire une proposition
# On lui répond si c'est trop petit, trop grand ou égal
while proposition != nb_secret:
    proposition = int(input("Quel est votre proposition ?"))
    if proposition < nb_secret:
        print("Vous êtes trop petit")
    elif proposition > nb_secret:
        print("Vous êtes trop grand")
    
print("C'est gagné")


# In[74]:


borne_min = 0
borne_max = 101

proposition = ( borne_min + borne_max ) // 2

trouve = False

while not trouve:
    reponse = input(f"Nous pensons que c'est {proposition}. Est-ce exacte ? P/G/E")
    if reponse == "P":
        borne_max = proposition
    if reponse == "G":
        borne_min = proposition
    if reponse == "E":
        trouve = True
    proposition = ( borne_min + borne_max ) // 2

print("Vous avez gagné !")


# In[94]:


def change_first(liste):
    liste[0] = 15

def addition(a,b):
    return a + b

def dire_bonjour(nom, prenom="", age=42):
    return f"Bonjour {nom} {prenom}. Vous avez {age} ans."


a = 5
b = 2
a = addition(a, b)

ma_liste = [3,5,1]
change_first(ma_liste)
print(ma_liste)
# dire_bonjour("Martin")
# a = dire_bonjour("Helene")

# print(a)


# In[92]:


a = "14ké" #"1111111111111111111111111111111111111111111111111111111111111111111111é"
b = "14ké" #"1111111111111111111111111111111111111111111111111111111111111111111111é"
# id(a)

a is b


# In[99]:


def dire_bonjour(nom, prenom="", age=42):
    return f"Bonjour {nom} {prenom}. Vous avez {age} ans."

dire_bonjour("Dupont")
dire_bonjour("Dupont", "Laurent")
dire_bonjour("Dupont", "Laurent", 35)
print(dire_bonjour("Dupont", 35))
print(dire_bonjour("Dupont", age=35))


# In[102]:


a = 4

def affiche_a():
    print(a)
  
a = 6
affiche_a()


# In[101]:


a = 5

def affiche_a():
    a = 4
    print(a)
    
affiche_a()
print(a)


# In[103]:


a = 5

def affiche_a():
    print(a)
    a = 4

    
affiche_a()
print(a)


# In[104]:


a = 5

def affiche_a():
    global a
    a = 4
    print(a)

affiche_a()
print(a)


# In[107]:


personne = {"nom": "Depardieu", "prenom": "Gerard", "age": 70}

def dire_bonjour(param_personne):
    param_personne["prenom"] = "Guillaume"
    print(f"Bonjour {param_personne['nom']} {param_personne['prenom']}")
  

dire_bonjour(personne)
print(f"Bonjour {personne['nom']} {personne['prenom']}")
      


# In[112]:


mon_tuple = (45,74,8,12)
mon_tuple[0] = 15
print(mon_tuple[0])
tu = (2,)


# In[ ]:


# Tri bulle

def tri_bulle(array):
    sorted_list = array.copy()
    
    return sorted_list

tri_bulle([3,1,7,5,9,0])

