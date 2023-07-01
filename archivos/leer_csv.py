import csv #para leer archivos csv, usamos el import csv. esto nos devuelve un iterable, que lo recorremos y cada recorrido nos devuelve una fila del texto

with open("archivos\\texto_en_csv.csv", encoding="UTF-8") as archivo:
    reader = csv.reader(archivo)
    for row in reader:
        print(row)