diccionario = {
    "nombre": "dario",
    "apellido": "bartoli",
    "edad": 28,
    "fuma": False,
    "ciudad": "Cordoba"
}

#recorrer diccionario para obtener las claves
for elementos in diccionario:
    print(f"la clave es: {elementos}")

#recorrer diccionario para obtener las claves y su valores
for elementos in diccionario.items():
    print(elementos)
    key = elementos[0]
    value = elementos[1]
    print(f"la clave es: {key} y su respectivo valor es: {value}")