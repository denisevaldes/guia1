#“El buen gordito” ofrece hamburguesas sencillas, 
#dobles y triples, las cuales tienen un costo de $2000,
#$2500 y $3000 respectivamente. La empresa acepta 
#tarjetas de crédito con un cargo de 5 % sobre la
#compra. Suponiendo que los clientes adquieren solo 
#un tipo de hamburguesa, realice un algoritmo para
#determinar cuánto debe pagar una persona por N hamburguesas.

print("hamburguesas el buen gordito")
print("< 1 > hamburguesa sencilla")
print("< 2 > hamburguesa doble")
print("< 3 > hamburguesa triple")
hamburguesa = int(input("indique el numero de la hamburguesa que quiere"))

if hamburguesa == 1:
    precio = 2000
elif hamburguesa == 2:
    precio = 2500
elif hamburguesa == 3:
    precio = 3000
else: 
    print("opcion invalida")

numero_hamburguesas = int(input("ingrese el numero de hamburguesas que desea: "))

precio_final = (precio * numero_hamburguesas) + ((5/100)* (precio * numero_hamburguesas))
print("precio a pagar: ", precio_final)