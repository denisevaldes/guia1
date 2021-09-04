# ejercicio 3

# usuario debe ingresar numero de trajes para calcular descuento
numero_trajes = int(input("ingrese el numero de trajes que quiere ingresar para calcular descuento: "))
indice = 0
# la estructura siguiente se repetira hasta que indice deje de ser menor que numero_trajes
while indice < numero_trajes: 
    traje = int(input("ingrese un valor: "))
    #dependiendo del valor del traje se escogera descuento determinado.
    if traje > 10000:
        descuento = (15/100) * traje
        print("descuento aplicado es de 15%")    
    else:
        descuento = (8/100) * traje
        print("descuento aplicado es de 8%")
    indice += 1
    # se calcula precio a pagar 
    # se imprime en pantalla el descuento y el precio a pagar.
    precio_pagar =  traje - descuento 
    print("descuento aplicado: ", descuento)
    print("precio tercer traje: ", precio_pagar)
   



