#ejercicio 6

#usuario debe ingresar cuanto cobra por hora y a cuantas personas le debe cobrar 
cobro = int(input("ingrese el cobro por hora: "))
personas = int(input("ingrese el numero de personas a cobrar: "))
indice = None
#estructura se repite hasta alcanzar el numero de personas a cobrar.
for indice in range(0,personas):
    #usuario debe ingresar horas y minutos a cobrar
    print("A continuacion se le pedira que ingrese horas y minutos por separado")
    horas = int(input("ingrese horas a cobrar: "))
    minutos = int(input("ingrese minutos: "))
    #dependiendo de si los minutos son iguales a cero o no, 
    # se le agregara una hora al total a cobrar. 
    if minutos != 0:
        total = (horas + 1) * cobro
    else:
        total = horas * cobro    
    print("el monto a cobrar es de: ", total)