#Realice un programa en Python para determinar cuánto se debe pagar por equis cantidad de lápices
#considerando que si son 1000 o más el costo es de 85 pesos; de lo contrario, el precio es de 90 pesos.

cantidad_lapices = int(input("por favor ingrese la cantidad de lapices: \n"))
if cantidad_lapices >= 1000: 
    precio = 85 * cantidad_lapices
else:
    precio = 90 * cantidad_lapices
print("el precio a pagar es de: ", precio)    