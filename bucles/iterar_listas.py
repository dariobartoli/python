animales = ["perro", "gato", "gallina", "caballo"]

for animal in animales:
    print(f"ahora la variable es {animal}")
    
numeros = [2, 4, 6, 9, 4, 2,52,32]

for numero in numeros:
    print(numero*3)
    

#recorrer 2 listas, las 2 listas tienen que tener la misma cantidad de elementos.. o mas listas
objectos = ["taza", "mesa", "silla", "casco"]
numbers = [3,5,2,6] #4 elementos cada lista

for objecto, number in zip(objectos, numbers):
    print(f"resultado de la lista objecto: {objecto}")
    print(f"resultado de la lista numbers: {number}")
    

#range te recorre un rango de numeros, se puede pasar un valor o 2
for rangos in range(3,7):
    print(rangos)
    
#forma no optima de recorrer una lista por su indice
for numero in range(len(numbers)):
    print(numbers[numero])
    
#forma correcta de recorrer una lista con su indice
#se vuelve una tupla la lista con este metodo, donde podes obtener su indice y su valor
for numero in enumerate(numbers):
    print(numero)
    indice = numero[0]
    valor = numero[1]
    print(f"indice es: {indice}, y el valor es: {valor}")
    
#usando el for/else
for numero in numbers:
    print(f"valor de este bucle es: {numero}")
else:
    print("el bucle ha terminado")#el else se muetra una sola vez, al final del bucle
    
#Todo ESTOS METODOS FUNCIONAN TAMBIEN CON LAS TUPLAS