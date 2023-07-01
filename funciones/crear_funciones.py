#crear una funcion simple
def saludar():
    print("saludos a todos")

saludar()

#funcion con parametros
def saludar2(nombre, sexo):
    sexo = sexo.lower()
    if (sexo == "femenino"):
        adjetivo = "reina"
    elif (sexo == "masculino"):
        adjetivo = "titan"    
    else:
        adjetivo = "amor"
    print(f"hola {nombre}, mi {adjetivo} ¿como andas?")
        
    
saludar2("dario", "masculino")

#crear una funcion que retorne valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num) #convertimos a string para despues obtener solo el primer numero
    number = int(num_entero[0]) #aca lo volvemos a convertir a entero pero primero extraemos el primer caracteres del string, para que solo vaya de 1 a 9
    c1 = number - 2
    c2 = number
    c3 = number - 5
    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    #return password
    #return (password, number) podemos retornar multiples valores, con una tupla por ejemplo
    return password, number
    
password, number = crear_contraseña_random(321)
print(f"tu contraseña es {password}")
print(f"tu numero es: {number}")




    
    