#crear un conjunto con set
conjunto = set(["dato1", "dato2"])

#meter un conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato3", "dato4"]) #frozenset crea un conjunto inmutable, que puede estar como congelado para que el conjunto sea hasheable osea poder añadirle datos que se pueden modificar, recordar que en los sets no se pueden modificar los datos

conjunto2 = {conjunto1, "dato5"}

print(conjunto2)


#teoria de conjuntos
#saber si un conjunto es subconjunto de otro o superconjunto

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}

#verificar si es un subconjunto
resultado = conjunto3.issubset(conjunto4) #con este metodos podemos ver si es un subconjunto, devuelve un booleano
#otra forma es con el <=
resultado = conjunto4 <= conjunto3

#verificar si es un superconjunto
resultado2 = conjunto3.issuperset(conjunto4)
resultado2 =  conjunto3 > conjunto4 #se usa solo el mayor >

#verificar si hay algun numero en comun
resultado3 = conjunto3.isdisjoint(conjunto4) #es true cuando ningun numero es igual, y dara false cuando haya algun numero igual

print(resultado3)
