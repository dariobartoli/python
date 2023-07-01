import re

#dectentando un numero de cba y ocultandolo

texto = "Hola, como estan? mi numero es: +54 351 652-5418"
pattern = r"\+\d{2}\s\d{3,4}\s\d{3}-\d{4}"
frase = "(numero oculto)"


#sub es para reemplazar un valor por otro
reemplazo = re.sub(pattern, frase, texto)

print(reemplazo)