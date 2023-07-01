import re

texto = """Hola, este es un texto y esta es la primer linea del texto (1)...
Esta va a ser la linea numero 2. del texto que estamos escribiendo
Y esta va a ser la linea numero 3. del Texto y la final
Numero random de 3 digitos 484
Otro numero random de mas digitos 9594411333
abb abbb abbbb
abab ababab abababab"""

#busqueda simple
#resultado = re.search("texto", texto) #search para buscar una sola coincidencia
#resultado = re.findall("texto", texto, flags=re.IGNORECASE) #con el ignore case ignoramos todas las mayusculas y minisculas

#\d busca digitos numericos del 0 al 9
#con la r le decimos es posible que usemos expresiones regulares
#resultado = re.findall(r"\d", texto)

#\D busca todo lo que no sea digitos numericos del numero 0 - 9
#poner la letra mayuscula busca resultados contrarios, no siempre es asi
#resultado = re.findall(r"\D", texto)

#\w busca todo lo que sea alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\w", texto)

#\W busca todo lo que NO sea alfanumericos [a-z A-Z 0-9 _]
#resultado = re.findall(r"\W", texto)

#\s busca espacios en blanco -> espacios, tabs, saltos de linea
#resultado = re.findall(r"\s", texto) #muestra los saltos de linea tambien \n

#\S busca todo MENOS espacios en blanco
#resultado = re.findall(r"\S", texto)

#. Busca todo MENOS saltos de linea
#resultado = re.findall(r".", texto)

#\n busca los saltos de linea
#resultado = re.findall(r"\n", texto)

# \ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r"\.", texto)



#armando una cadena que busque un numero, seguido de un punto y un espacio
#resultado = re.findall(r"\d\.\s", texto)



#^ busca el comienzo de una linea, para saber si cierta palabra está al principio de una linea, en este caso Hola
#resultado = re.findall(r"^Hola", texto)
#resultado = re.findall(r"^Esta", texto, flags=re.M) #con el parametro M activado busca el comienzo de cada linea.. activa la multilinea

#$ busca el final de una linea, para saber si cierta palabra está al final de una linea, en este caso ¿final?
#resultado = re.findall(r"final$",texto, flags=re.M)

#{n}  -> busca n cantidad de vecez el valor de la izquierda
#resultado = re.findall(r"\d{3}", texto) #con esto busca los digitos sucesivos, por eso sale el 484


#{n, m}  -> sirve para hacer rangos, al menos n cantidad de veces y como maximo m cantidad de veces
#resultado = re.findall(r"\d{3,7}", texto)

#conjunto, buscar un valor que tenga una a primero y luego el numero de rango de veces b que le asignemos. ejemplo
#resultado = re.findall(r"ab{2,4}", texto)
#si queres que tambien cuando a en la sucesion va entre parentesis
#resultado = re.findall(r"(ab){2,4}", texto) #esto nos devolvera las coincidencias si hay 3 ab junto, no devolvera un ab

#pero si queremos que nos devuelve todos los ab que coinciden lo encerramos entre corchetes  
#resultado = re.findall(r"[ab]{2,4}", texto)


# | -> busca una cosa o la otra
resultado = re.findall(r"\d{2,4}|Hola", texto) #primero nos devuelve el Hola, porque es lo primero que encuentra, no importa de que lado de la expresion se encuentre
#no es un condicional, sino si aparecen los 2 devuelve los 2


#poner un * despues de una coincidion lo que hace es decirle que te devuelva el mayor numero que encuentre, si encuentra 0, no importa que tambien lo devuelva. esto es para que la coincidencia la devuelva igual, aunque no encuentre nada




print(resultado)