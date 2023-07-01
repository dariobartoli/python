#vamos a crear una expcecion y a lanzarza con raise

class MiExcepcion(Exception): #hereda todos los atributos de exception
    def __init__(self, err):
        print(f"noob, cometiste el siguiente error: {err}")
        
#raise MiExcepcion("no puede ser")
#con raise podemos lanzar la excepcion

#ahora vamos a manejar al excepcion

try:
    raise MiExcepcion("no puede ser")
except:
    print("que pasó? tuviste un error de noob")