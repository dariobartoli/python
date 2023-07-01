#crear una funcion de suma, que recibe 2 numeros (int), al pasarle un string el programa va a tirar un error
#lo que vamos a hacer es manejar ese error con try

def sumar():
    #iniciamos un bucle que se ejecute siempre
    while True:
        a = input("ingrese un numero: ")
        b = input("ingrese otro numero: ")
        try: #el programa va a intentar sumar los numeros en try, si no puedo nos lanza la exception
            resultado = int(a) + int(b) #no olvidemos de convertir los string a enteros
        except Exception as e: #podemos hacer que nos muestre la excepcion con Exception(una clase)
            print("te pedi un numero, ingrese un numero por favor: ")
            print(f"ERROR: {e}")
        #el else se va a ejecutar si except no se ejecuta, si se ejecuta except no se ejecuta el else
        else:
            break #con break hacemos que se detenga el bucle y se salga del mismo, de esta manera salimos del bucle while
        finally: #finally se va a ejecutar siempre!!
            print("probando como manejar una excepcion")
    return resultado

print(sumar())