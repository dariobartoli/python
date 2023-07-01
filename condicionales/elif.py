ingreso_mensual = 6000
gasto_mensual = 5000

if ingreso_mensual > 5000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("estas bien economicamente")
    else:
        print("estas gastando demasiado")
elif ingreso_mensual > 1000:
    print("estas bien en latam")
else:
    print("sos pobre")