def frase(nombre, apellido, adjetivo):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultado = frase("dario", "bartoli", "capo")
print(frase_resultado)


#crear funcion con parametro opcional y valor por defecto

def frase2(nombre, apellido, adjetivo = "tonto"):
    return f"hola {nombre} {apellido}, sos muy {adjetivo}"

#el tercer valor viene por defecto, puede estar vacio y se lo puede cambiar si se lo desea

frase_resultado2 = frase2("dario", "bartoli")
print(frase_resultado2)

frase_resultado3 = frase2("dario", "bartoli", "crack")
print(frase_resultado3)
