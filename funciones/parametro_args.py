#forma no optima de sumar valores, no es optima porque tenemos que pasar una lista y queremos un parametro indefinido
def suma(lista):
    numero_sumados = 0
    for number in lista:
        numero_sumados = numero_sumados + number
    return numero_sumados

resultado = suma([5,6,11])
print(resultado)


#forma optima con args de hacer una suma indefinida
#el parametro args se tiene que usar el final
def suma2(nombre,*numbers):
    return f"{nombre} la suma de tus numeros es: {sum(numbers)}"

resultado2 = suma2("dario",3,6,3,7,3,7)
print(resultado2)

#forma optima
def suma3(lista):
    return sum([*lista])

resultado3 = suma3([2,4,6,8])
print(resultado3)