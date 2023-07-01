import pandas as pd

#cambiar el tipo de dato de una columna

df = pd.read_csv("archivos problemas resueltos\\texto_en_csv.csv")

#cambiar los datos de una columna a string
df["edad"] =  df["edad"].astype(str)

print(type(df["edad"][0]))
print("---------------")

#reemplazanod el nombre dario por ezequiel
df["nombre"].replace("dario", "ezequiel", inplace=True)

print(df["nombre"])
print("---------------")

#eliminar las filas con datos vacios o faltantes

print(df)
df_corregido = df.dropna() #para eliminar columnas con datos faltantes se pasa como parametro (axis=1)
print("---------------")
print(df_corregido)
print("---------------")

#eliminar las filas con datos repetidos
df_no_repetido = df_corregido.drop_duplicates()
print(df_no_repetido)


#creando un CSV con el dataframe resultante (corregido, limpio)
df_no_repetido.to_csv("archivos problemas resueltos\\texto_corregido.csv")