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
    


# In[55]:


liste_prenoms = [
    "Martin",
    "Elise",
    "Mathieu"
]
liste_ages = [23, 43, 12, 56]

for prenom, age in zip(liste_prenoms, liste_ages):
    print(f"Prenom : {prenom} et age : {age}")
    
for i, val in enumerate(liste_prenoms):
    print(f"prenom n {i} : {val}")


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

# In[ ]:




