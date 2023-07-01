#para importar una modulo dentro de una carpeta se hace asi:

import funciones_buenas.saludar as saludin

saludo = saludin.saludar("dario")
print(saludo)

#si el modulo está en una carpeta de fuera se usa el sys
#sys es un modulo built-in, un modulo construido en python 

import sys

sys.path.append("C:\\Users\\Dario\\Desktop\\python\\funcion_fuera")
print(sys.path)

import saludo_fuera

saludo2 = saludo_fuera.despedir("dario")
print(saludo2)