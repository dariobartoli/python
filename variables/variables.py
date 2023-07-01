nombre = "dario"

numero = 10
numero += 5
numero -= 2
palabra = "hola"

#concatenar con f-strings
bienvenida = f"hola {nombre} ¿como estas?"
"de esta forma convierte todo a texto con el f(strings)"

#en python se recomiendo nombrar las variables con snake_case, no con camelCase
nombre_completo = "dario bartoli"

#del para eliminar una variable
del palabra



print(nombre)
print(numero)
print(bienvenida)
#operadores de pertenencia (in / not in)
print("ola" in bienvenida)
"va a devolver true porque existe ola en bienvenida"
print("samuel" not in bienvenida)
"lo contrario, tambien devolveria true"