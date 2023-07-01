#funcion lambda es como una funcion flecha en javascript, se puede crear funciones anonimas que se pueden almacenar en variables
#beneficio se puede usar cuando queremos hacer algo sencillo y rapido, y retornan automaticamente
#no son aptas cuando queremos dar mas de una expresión

#creando funcion lambda de multiplicar x2
multiplicacion = lambda x : x*2

print(multiplicacion(6))

#creando funcion comun que diga si es par o no
def es_par(num):
    if (num%2 == 0):
        return True


#usando filter con una funcion comun
numbers = [2,6,2,7,4,62,15,9,8]
numeros_pares = filter(es_par, numbers)

print(list(numeros_pares))

#crear lo mismo pero con lambda
pares = filter(lambda numero: numero%2==0, numbers)
print(list(pares))