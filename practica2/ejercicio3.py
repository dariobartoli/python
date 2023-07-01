#falta el profesor, y los alumnos arman la clase, piden nombre y edad. ordenarlos de menor a mayor
#el mayor es el profesor y el menor el asistente

def obtener_compañeros(cantidad_compañeros):
    compañeros = []
    for i in range(cantidad_compañeros):
        nombre = input("ingrese el nombre del compañero: ")
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre, edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    return asistente, profesor

asis, prof = obtener_compañeros(5)

print(f"el compañero que sera profesor es: {prof}, y el que sera el asistente: {asis}")
