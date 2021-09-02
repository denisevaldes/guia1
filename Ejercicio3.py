#Una multitienda tiene una promoción: a todos los trajes que tienen un precio superior a $10000 se les
#aplicará un descuento de 15 %, a todos los demás se les aplicará sólo 8 %. Realice un programa para
#determinar el precio final que debe pagar una persona por comprar un traje y de cuánto es el descuento
#que obtendrá. Pida por lo menos ingresar 3 elementos.


print("por favor ingrese el precio de tres trajes")
primer = int(input("primer traje: "))
segundo_traje = int(input("segundo traje: "))
tercer_traje = int(input("tercer traje: "))

if primer > 10000:
    descuento = (15/100) * primer
    print("descuento aplicado es de 15%")    
else:
    descuento = (8/100) * primer
    print("descuento aplicado es de 8%")

precio_pagar = primer - descuento 
print("descuento aplicado: ", descuento)
print("precio primer traje: ", precio_pagar)

if segundo_traje > 10000:
    descuento2 = (15/100) * segundo_traje
    print("descuento aplicado es de 15%") 
else: 
    descuento2 = (8/100) * segundo_traje
    print("descuento aplicado es de 8%")

precio_pagar2 = segundo_traje - descuento 
print("descuento aplicado: ", descuento2)
print("precio segundo traje: ", precio_pagar2)

if tercer_traje > 10000:
    descuento3 = (15/100) * tercer_traje
    print("descuento aplicado es de 15%")
else:
    descuento3 = (8/100) * tercer_traje
    print("descuento aplicado es de 8%")

precio_pagar3 = tercer_traje - descuento 
print("descuento aplicado: ", descuento3)
print("precio tercer traje: ", precio_pagar3)



