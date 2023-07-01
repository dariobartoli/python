#crear un diccionario
diccionario = dict(nombre= "dario", apellido="bartoli")

#las listas no pueden ser claves, una tupla si puede ser clave, y los sets para ser claves necesitamos usar frozenset
diccionario2= {("nom","bre"):"dario"}
diccionario3= {frozenset(["nom","ap"]):"dario"}

#creando diccionarios con fromkeys, sin asignar los valores
diccionario4= dict.fromkeys(["nombre","apellido", "edad"])


print(diccionario4)