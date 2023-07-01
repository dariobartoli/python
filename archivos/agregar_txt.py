#agregar texto con append (a), es lo mismo que con write, te añade texto, la diferencia es
#que con append no te sobreescribe el texto, simplemente te lo va agregando   

with open("archivos\\texto_prueba.txt","a",encoding="UTF-8") as archivo:
    #agregando el archivo:
    archivo.write("agrego una sexta linea con append\n")
    
    #tambien podemos hacer un ciclo con for
    for i in range(5):
        archivo.write(f"linea {i+1} agregada con append\n")
