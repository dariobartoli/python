numeros = [2,6,34,25,14]

#extraer numero mas alto
max = max(numeros)
print(max)

#extraer numero mas bajo
min = min(numeros)
print(min)

#redondear un numero con decimales
#con la funcion round podemos pasar un numero, y con el segundo parametro le decimos cuanto decimales queremos que nos deje
numero = 12.321562
redondeado = round(numero, 2)
print(redondeado)

#funcion bool -> retorna false si le pasamos como parametro: 0, False, None, vacio
#retorna true si le pasamos: True, numero != 0, cadena
resultado_bool = bool(())
resultado_bool_true = bool([3,4,7])
print(resultado_bool)
print(resultado_bool_true)

#funcion all -> retorna true si todos los valores son verdaderos
resultado_all = all([2314, "true", True, [32, 324]])
print(resultado_all)

#sum -> suma todos los valores de un iterable
suma = sum(numeros)
print(suma)

