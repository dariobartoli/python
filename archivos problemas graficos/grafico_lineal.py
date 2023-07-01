#trabajando con un grafico lineal, queremos encontrar los dias que la persona tuvo problemas estomacales

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos problemas graficos\\pedos.csv")

sns.lineplot(x="fecha", y="pedos", data=df)

plt.plot("01-09",17,"o")#para marcar el valor mas alto, en este caso conocemos los datos para poder marcarlo de manera manual

plt.show()