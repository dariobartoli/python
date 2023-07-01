#LIST: crea una lista
#LEN: cuenta la cantidad de elementos de una lista
#APPEND: agrega un elemento a la lista
#INSERT: agrega un elemento a la lista en el indice especificado
#EXTEND: agrega varios elementos a la lista
#POP: elimina una elemento de la lista, pide indice y devuelve valor
#REMOVE: remueve un elemento de una lista, pide valor
#CLEAR: elimina todos los elementos de una lista
#SORT: ordena una lista de forma ascendente o descendente
#REVERSE: invierte los elementos de un lista

lista = list(["hola", "mundo", 34])
lista_de_compra = ["harina", "leche", "manteca", "arroz", "pollo", "fideos", "tarta", "pizza", "bebidas"]
lista_de_numero = [45, 32, 2, 1, 5, 432, 51, 42, 23, 9]

resultado = len(lista_de_compra)
lista_de_compra.append("vino") #no se crea una variable, se hace directamente sobre la lista
lista_de_compra.insert(2, "queso") #agrega un elemento en el indice especificado
lista_de_compra.extend(["tomate", "milanesa"]) #agrega varios elementos
lista_de_compra.pop(1) #si se pone el indice -1 se elimina el ultimo elemento de la lista, si pones -2 elimina el anteultimo
lista_de_compra.remove("Arroz".lower())
#lista_de_compra.clear()
lista_de_numero.sort(reverse=True) #por defecto ordena de manera ascendente, tiene que ser una lista de solo numeros, puede tener booleanos
lista_de_compra.reverse() #invierte los elementos de la lista


elemento_encontrado = lista_de_compra.index("manteca")
#en una tupla lo unico que se puede hacer es buscar por index, o contar los elementos de la tupla con count, porque estas misma no se pueden modificar
#en un set se puede sacar elementos con pop o removerlos, pero no se pueden agregar elementos al set, ya sea con un append o insert, tampoco se puede usar index en un set


print(lista_de_compra)
print(elemento_encontrado)