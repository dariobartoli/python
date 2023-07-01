#KEYS: devuelve las claves, tambien nos sirve para iterar
#GET: devuelve el valor de una clave
#CLEAR: elimina todos los elementos
#POP: elimina un elemento
#items: para iterar

diccionario = {
    "nombre": "dario",
    "apellido": "bartoli",
    "edad": 28,
    "fuma": False,
    "ciudad": "cordoba"
}

resultado = diccionario.keys()
resultado2 = diccionario.get("nombre")
#diccionario.clear()
diccionario.pop("ciudad")


resultado3 = diccionario.items() #ahora es iterable


print(diccionario)
print(resultado3)
