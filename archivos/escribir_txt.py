with open("archivos\\texto_prueba.txt","w",encoding="UTF-8") as archivo:
    #sobreescribiendo archivo:
    #archivo.write("hacer esto, te sobreescribe todo el archivo, si no tenes creado un archivo el paramtro (w) te crea una")
    
    #sobreescribiendo lineas, de esta manera podes escribir texto, indicando cuando queres que se haga un salto de linea
    archivo.writelines(["aca estoy escribiendo la primer linea\n", "para hacer el salto de linea use el (\ n)\n", "que es lo que indica el salto de linea en texto plano\n"])
    
    #tanto write como writelines te reemplazan el archivo, pero usar de nuevo writelines lo que haces es acumularse con el anterior
    archivo.writelines(["aca estoy agregando mas lineas\n","esta es una quinta linea wow\n"])