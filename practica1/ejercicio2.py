#un persona dice 2 palabras por segundo, pedirle a una persona que diga una frase y calcular cuanto tardaria en decir la frase y ¿cuantas palabras dijo?

#si tarda mas de un min decirle, para flaco tampoco te pedi un testamento 

#cuanto tardaria una persona que habla un 30% mas rapido que el promedio 

frase = input("ingrese una frase por favor: ")
lista_frase = frase.split(" ")
numero_de_palabras = len(lista_frase)
segundos = float(numero_de_palabras/2)

if segundos > 60:
    print("te dije una frase, no un testamento")
else:
    print(f"tardaste {segundos} segundos en decir la frase y dijiste {numero_de_palabras} palabras")
    
segundos_persona_rapida = segundos / 1.3

print(segundos_persona_rapida)
