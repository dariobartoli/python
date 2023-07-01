#forma de importar todo por defecto, a estos modulos se le llama namespaces

#import modulo_saludar as m_saludo

#saludo = m_saludo.saludar("dario")

#print(saludo)

#importar lo que queramos de una funcion
#cambiar el nombre con as
from modulo_saludar import saludar as hola, despedir as adios
#aca estoy importando las 2 funciones que hay en modulo saludar

#otra forma de importar, pero es una mala practica. porque sobrecarga la aplicacion
#from modulo_saludar import *

saludo = hola("dario")
despedida = adios("dario")

print(saludo)
print(despedida)



#para ver las propiedades y metodos del namespace ->  print(dir(m_saludo))