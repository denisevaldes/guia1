# ejercicio 1

# se le pide al usuario que ingrese cantidad de lapices a comprar
cantidad_lapices = int(input("por favor ingrese la cantidad de lapices: \n"))
# dependiendo de la catidad de lapices se calculara un preciio u otro. 
if cantidad_lapices >= 1000: 
    precio = 85 * cantidad_lapices
else:
    precio = 90 * cantidad_lapices
print("el precio a pagar es de: ", precio)    