# ejercicio 7

# se muesta en pantallas opciones de hamburguesas
# se le pide a usuario que ingrese una opcion
print("hamburguesas el buen gordito")
print("< 1 > hamburguesa sencilla")
print("< 2 > hamburguesa doble")
print("< 3 > hamburguesa triple")
hamburguesa = int(input("indique el numero de la hamburguesa que quiere"))
# el precio cambiara dependiendo de la opcion elegida
if hamburguesa == 1:
    precio = 2000
elif hamburguesa == 2:
    precio = 2500
elif hamburguesa == 3:
    precio = 3000
else: 
    print("opcion invalida")

# se pide que se ingrese el numero de hamburguesas deseadas
numero_hamburguesas = int(input("ingrese el numero de hamburguesas que desea: "))
# se calcula el precio final añadiendo el cargo de 5% sobre la compra
precio_final = (precio * numero_hamburguesas) + ((5/100)* (precio * numero_hamburguesas))
print("precio a pagar: ", precio_final)