#trabajando con un grafico de dispersion

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos problemas graficos\\dispersion.csv")

sns.scatterplot(x="tiempo", y="dinero", data=df) #para crear grafico de dispersion

plt.show()