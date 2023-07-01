#DIR: devuelve la lista de atributos validos del objeto pasado
#UPPER: convierte a mayuscula
#LOWER: convierte a minuscula
#CAPITALIZE: primera en mayuscula
#FIND: metodo encuentra la primera aparicion del valor especificado, sino devuelve 1
#INDEX: metodo encuentra la primera aparicion del valor especificado, sino devuelve una excepcion 
#ISNUMERIC: si es numerico devuelve true
#ISALPHA: si es alfa numerico devuelve true
#COUNT: devuelve el numero de ocurrencias de una subcadena en la cadena dada
#LEN: cuenta los caracteres de una cadena
#ENDSWITH: verifica si una cadena termina con
#STARTSWITH: verifica si una cadena empieza con
#REPLACE: reemplaza un valor por otro
#SPLIT: separa por el parametro dado


cadena1 = "Hola mundo desde python"
cadena2 = "aprendiendo a Programar en py"
cadena3 = "21313"
cadena4 = "dsad"

resultado = dir(cadena1)
resultado2 = cadena1.upper()
resultado3 = cadena1.lower()
resultado4 = cadena2.capitalize() #convierte todo a minuscula y luego a la primer letra la hace mayuscula
resultado5 = cadena1.find("mundo") #devuelve la posicion, si no encuentra devuelve -1
resultado6 = cadena1.index("u") #devuelve la posicion pero si aca no encuentra anda, devuelve una excepcion
resultado7 = cadena3.isnumeric()
resultado8 = cadena4.isalpha() #tiene que ser sin espacios para que sea true
resultado9 = cadena1.count("e") #busca el numero de coincidencias
resultado10 = len(cadena1) #cuenta el numero de caracteres
resultado11 = cadena1.endswith("n")
resultado12 = cadena1.startswith("H")
resultado13 = cadena1.replace("Hola", "Adios")
resultado14 = cadena1.split(" ")#crea una lista, separandola por el valor que le pasamos por parametro


print(resultado14)

