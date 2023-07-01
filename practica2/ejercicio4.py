#crear una funcion que devuelva los numeros primos entre 0 y el argumento que pasamos

#creamos una funcion para saber si un numero es primo

def es_primo(num):
    for i in range(2, num-1):
        if(num%i == 0):
            return False
    return True
    
#print(es_primo(9))

#todos los numeros que llegar a ser primos desde el 0 al argumento que le pasamos

def numeros_primos(num):
    primos = []
    for i in range(3, num+1):
        resultado = es_primo(i)
        if(resultado == True):
            primos.append(i)
    return primos

primo = numeros_primos(13)
print(primo)
