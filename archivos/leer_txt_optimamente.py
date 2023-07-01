#para leer un texto optimamente usamos with open
#esto consume menos recursos y es mas optimo
#abre el archivo y lo cierra automaticamente, no tenemos que andarlo cerrando
#trae muchos menos errores de secciones
#UTF-8 abrir archivo con codificacion universal

with open("archivos\\texto_prueba.txt", encoding="UTF-8") as archivo:
    contenido = archivo.read()
    print(contenido)