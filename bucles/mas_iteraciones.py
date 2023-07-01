frutas = ["naranja", "mandarina", "banana","pera", "uva","pomelo","durazno"]


#evitando que se coma un pomelo con continue, con la sentencia continue salteamos esa iteracion
for fruit in frutas:
    if fruit == "pomelo":
        continue
    print(f"me voy a comer una {fruit}")
    
#evitar que el bucle siga ejecutandose, con break

for fruit in frutas:
    print(f"me voy a comer una fruta: {fruit}")
    if fruit == "banana":
        print("la banana le cayó mal a la panza y ya no come")
        break

#recorrer una cadena de texto
texto = "hola mundo"

for letra in texto:
    print(letra)
    
    
#bucle for en una sola linea de codigo
numbers = [1,5,7,8]
numbers_x2 = list()
for num in numbers:
    numbers_x2.append(num*2)
print(numbers_x2)

#en una sola linea de codigo seria:
numeros_duplicados = [x*2 for x in numbers]
print(numeros_duplicados)
