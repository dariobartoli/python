#informacion
otro_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
curso_actual = 1.5

#duracion de crudos ( videos sin editar )
crudos_promedio = 5
crudo_actual = 3.5


#diferencias de duracion
diferencia_con_min = 100 - curso_actual/otro_cursos_min * 100
diferencia_con_max = 100 - curso_actual * 1000// otros_cursos_max /10 #hacemos de esta forma para acomodar los decimales, sino daria un numero muy largo y es la mejor forma de restarlos
diferencia_con_prom = 100 - curso_actual/otros_cursos_promedio * 100

#asd = curso_actual // otros_cursos_max
#print(asd)
print("-------------")
print(f"el curso actual dura un {diferencia_con_min}% menos que los cursos mas rapidos")
print(f"el curso actual dura un {diferencia_con_max}% menos que los cursos mas lentos")
print(f"el curso actual dura un {diferencia_con_prom}% menos que el promedio de cursos")
print("-------------")


#calculo de porcentaje de tiempo que se logra eliminar luego de edicion en los cursos
otros_cursos_tiempo = 100 - otros_cursos_promedio / crudos_promedio * 100
curso_actual_tiempo = round((100 - curso_actual / crudo_actual * 100), 2)

print(f"un curso promedio elimina un {otros_cursos_tiempo}% luego de la edicion")
print(f"el curso actual elimina un {curso_actual_tiempo}% luego de la edicion")
print("-------------")

#comparacion de tiempos de los cursos al ver
#ver 10 horas del curso actual a cuanto tiempo valdria de los otros cursos

actual_diez_min = 10 + 10 * diferencia_con_min / 100
actual_diez_max = 10 + 10 * diferencia_con_max / 100
actual_diez_prom = 10 + 10 * diferencia_con_prom / 100


print(f"ver 10 horas del curso actual equilvaldria a {actual_diez_min} horas de otros cursos minimos")
print(f"ver 10 horas del curso actual equilvaldria a {actual_diez_max} horas de otros cursos maximos")
print(f"ver 10 horas del curso actual equilvaldria a {actual_diez_prom} horas de otros cursos promedio")
print("-------------")



