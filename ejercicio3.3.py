
numero_trajes = int(input("ingrese el numero de trajes que quiere ingresar: "))
indice = 0

while indice < numero_trajes: 
    traje = int(input("ingrese un valor: "))
    if traje > 10000:
        descuento = (15/100) * traje
        print("descuento aplicado es de 15%")    
    else:
        descuento = (8/100) * traje
        print("descuento aplicado es de 8%")
    indice += 1
    precio_pagar3 =  traje - descuento 
    print("descuento aplicado: ", descuento)
    print("precio tercer traje: ", precio_pagar3)
   



