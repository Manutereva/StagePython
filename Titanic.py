#!/usr/bin/env python
# coding: utf-8

# In[58]:


get_ipython().run_line_magic('matplotlib', 'inline')
import pandas as pd


df = pd.read_csv("train.csv")
df.columns
df.dtypes
df.describe()
df.count()

df["Age"].hist()
df[df["Survived"] == 1] # On récupère que ceux qui ont survécu
df[df["Survived"] == 1]["Age"].hist()
print("hello")

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})


# In[55]:


# len(df[(df["Survived"] == 1) & ()])
total = len(df)
# proportion de femmes
p_f = len(df[(df["Sex"] == "female")]) / total
# proportion d'hommes
p_h = len(df[(df["Sex"] == "male")]) / total
# proportion de femmes qui survivent
p_fs = len(df[(df["Sex"] == "female") & (df["Survived"] == 1)]) / len(df[(df["Sex"] == "female")])
# proportion d'hommes qui survivent
p_hs = len(df[(df["Sex"] == "male") & (df["Survived"] == 1)]) / len(df[(df["Sex"] == "male")])
# len(df["Sex"].dropna())

print(f"""
    Proportion de femmes : {p_f}
    Proportion d'hommes : {p_h}
    Proportion de femmes qui survivent : {p_fs}
    Proportion d'hommes qui survivent : {p_hs}
""")


# In[1]:


import pandas as pd

df = pd.read_csv("train.csv")
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
# df.groupby("Embarked").count()
df["Embarked"] = df["Embarked"].map({"S":0, "C": 1, "Q": 2})
df.drop(columns=["Cabin", "Ticket"], inplace=True)
df.dropna(inplace=True)

import re 

# chaine = "Cumings, Mrs. John Bradley (Florence Briggs Th"
# print(re.findall(", (.*)\.", chaine))

def extract_title(name):
    return re.findall(", ([^\.]*)\.", name)[0]

df["Title"] = df.Name.map(extract_title)
titles = list(df["Title"].unique())
df["Title"] = df["Title"].map(lambda t: titles.index(t))


# In[100]:





# In[ ]:




