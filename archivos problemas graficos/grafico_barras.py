#trabajando con un grafico de barras, con la informacion de ingresos de cofla

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archivos problemas graficos\\cofla_ingresos.csv")

sns.barplot(x="fuente", y="ingresos", data=df)

total_ingresos = df["ingresos"].sum() #metodo para sumar todos los datos de la columna ingresos, obviamente un valor numerico
print(f"el total de ingresos es ${total_ingresos} USD")

plt.show()