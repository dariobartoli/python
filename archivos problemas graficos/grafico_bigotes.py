#trabajando con un grafico de bigotes

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos problemas graficos\\bigotes.csv")

sns.boxplot(x="categoria", y="valor", data=df) #para crear grafico de bigotes o de cajas

plt.show()