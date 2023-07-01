archivo_sin_leer = open("archivos\\texto_prueba.txt", encoding="UTF-8")
#archivo = archivo_sin_leer.read() #una vez que se lee un archivo no se puede volver a leer, por un motivo de seguridad. para poder volver a leer hay que cerrarlo, por este motivo lineas nos da una lista vacia



#leer linea por linea
#lineas = archivo_sin_leer.readlines() #nos va a leer todas las lineas del archivo, nos devuelve la lista con la cantidad de elementos como cantidad de lineas tiene el texto, el caracter "\n" es como se interpreta un salto de linea en un texto plano

#print(lineas)



#leer una sola linea

linea = archivo_sin_leer.readline() #podes leer la primer linea del archivo, si le pasas un valor de parametro te lee la cantidad de caracteres que le pases como parametro

#cerrar el archivo:
archivo_sin_leer.close() #ahora para poder volver a leer hay que usar el open de nuevo
#es importante cerrarlo porque se puede perder archivos si se cierra de manera inesperada

print(linea)