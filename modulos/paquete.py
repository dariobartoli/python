#import paquete

#print(type(paquete)) #un paquete no deja de ser un modulo, nos dira que es un modulo pero teoricamente es un paquete, la diferencia es un tema enrutamiento
#print(paquete.__path__)#sino tuviera el init no podriamos usar la funcion __path__ para ver la ruta


import paquete.saludo
print(paquete.saludo.saludar("dario"))