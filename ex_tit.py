# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")
df.columns
df.dtypes
df.describe()
df.count()

df["Age"].hist()
df[df["Survived"] == 1] # On récupère que ceux qui ont survécu
df[df["Survived"] == 1]["Age"].hist()

plt.show()