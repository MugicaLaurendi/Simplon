import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


csv = "akinator.csv"
df = pd.read_csv(csv)


print(df['Sucré ou salé?'])
print(type(df['Sucré ou salé?']))


df.groupby('Sucré ou salé?')['Nom'].nunique().plot(kind='bar')
plt.show()
