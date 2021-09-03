#Un estacionamiento requiere determinar el 
#cobro que debe aplicar a las personas que lo utilizan.
#Considere que el cobro es con base en las horas 
#que lo disponen y que las fracciones de hora se toman como
#completas. Cree un programa que realice el cobro del estacionamiento.
 
cobro = int(input("ingrese el cobro por hora: "))
personas = int(input("ingrese el numero de personas a cobrar: "))
i = None

for i in range(0,personas):
    tiempo = int(input("ingrese el tiempo a cobrar en minutos: "))
    if tiempo % 60 != 0:
        hora = (tiempo // 60) + 1
    else:
        hora = tiempo / 60
    total = cobro * hora 
    print("el monto a cobrar es de: ", total)