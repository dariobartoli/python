#2 listas, una con nombres y otra con apellidos
nombres = ["dario","juan","marcos","nestor","tomas","camila"]
apellidos = ["bartoli","lopez","herrero","mendoza","fonzi","zalazar"]

#registrar esta informacion en un TXT de forma optima

with open("archivos problemas resueltos\\nombre_apellidos.txt", "w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombre: {a}\nApellido: {b}\n----------------\n") for a,b in zip(nombres, apellidos)]
    #otra forma de hacer un for, es poniendolo dentro de una lista, y pasando el for al ultimo, for de una sola linea