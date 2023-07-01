#hacer una sucesion fibonacci desde 0 hasta el numero que le pasemos

def fibonacci(num):
    a,b = (0,1)
    lista_fibonacci = [0]
    for i in range(num):
        if(b > num):
            return lista_fibonacci
        else:
            lista_fibonacci.append(b)
            a,b = b, a+b #a es igual a b, y b es igual a a+b
    return lista_fibonacci

resultado = fibonacci(20)
print(resultado)