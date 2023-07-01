import pandas as pd #para pandas generalmente se usa la abreviatura pd para mencionarlo

#usamos la funcion read_csv para leer el archivo csv

df = pd.read_csv("archivos\\texto_en_csv.csv") #df = dataframe, estructuras de datos, bidimensionales como si fueran hojas de calculo. no se comporta como un archivo, tiene su propia forma de acceder, filas y columnas
#si queres cambiar el nombre de las columnas, le pasamos el parametro en el read names=[], por ejemplo cambiarlos al ingles. le agrega un encabezado, y el antiguo encabezado se convierte en la primer fila
df2 = pd.read_csv("archivos\\texto_en_csv.csv")
print(df)
print("--------------------")


#obteniendo los datos de la columna nombre:
nombres = df["nombre"]
print("--------------------")


#el metodo slice, en python se usa con :, pasando del lado izquierdo el primer valor donde empieza y en el derecho donde termina. Ejemplo:
#cadena = "0123456789"
#print(cadena[3:7])


#ordenando el dataframe por la edad
df_ordenado = df.sort_values("edad")
df_ordenado2 = df.sort_values("edad", ascending=False) #de esta forma lo ordenamos de manera descendiente... por defecto viene en ascendente

print(df_ordenado2)
print("--------------------")


#concatenar 2  dataframe
df_concatenado = pd.concat([df,df2])

print(df_concatenado)
print("--------------------")

#accediendo a la primer fila con head(), se le tiene que pasar un parametro
primer_fila = df.head(1) #si le pasamos 0, nos devuelve el encabezado.. si ponemos 2, nos muestra las 2 primeras filas
print(primer_fila)
print("--------------------")

#accediendo a la ultima fila, ultimas 3 filas con tail()
ultimas_filas = df.tail(3)
print(ultimas_filas)
print("--------------------")

#accediendo a las cantidad de filas y columnas con shape
filas_y_columas_totales = df.shape #shape, nos devuelve una tupla con la cantidad de filas totales en el primer valor y las columnas totales en el segundo valor
#por lo tanto podemos acceder a ella descomponiendo una tupla
filas_totales, columnas_totales = df.shape


print(columnas_totales)
print("--------------------")


#obteniendo data estadistica del dataframe
#se usa mas para el analisis del dato
df_info = df.describe()
print(df_info)
print("--------------------")

#accediendo a un elemento especifico del df con loc
elemento_especifico_loc = df.loc[2, "edad"] #accedemos a la fila 2, y a su edad en este caso 35
print(elemento_especifico_loc)
print("--------------------")

#accediendo con iloc
elemento_especifico_inloc = df.iloc[2,2] #accederemos al mismo valor pero esta vez pasandole fila 2, columna 2
print(elemento_especifico_inloc)
print("--------------------")


#accediendo a todas las filas de una columna
apellidos = df.iloc[:,1]
print(apellidos)
print("--------------------")

#accediendo a todos los datos de una fila
fila_3 = df.loc[2,:] #podemos hacerlo tambien con iloc
print(fila_3)
print("--------------------")

#accediendo a filas con edad mayor que 30
mayor_30 = df.loc[df["edad"]>30,:]
print(mayor_30)
