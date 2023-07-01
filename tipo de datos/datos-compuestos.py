lista = ["dario", "bartoli", False, 28]
#lista es una matriz, al igual que los array. Conjunto de datos

tupla = ("dario", "bartoli", False, 28)
#una tupla es igual a la lista, funciona igual pero esta no se puede modificar

#esto es valido
lista[3] = "mas"

#esto no es valido
#tupla[3] = "mas"

print(lista)

conjunto = {"dario", "bartoli", False, 28}
#en un cojunto los elementos no tienen un orden fijo, pueden variar, tampoco se puede modificar los elementos, no se puede acceder a los elemntos por el indice, y no se pueden repetir los valores

diccionario = {
    'nombre': "Dario",
    'apellido': "Bartoli",
    'edad': 28,
    'sabe_programar': True
}

print(diccionario["apellido"])
