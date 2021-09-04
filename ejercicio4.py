#ejercicio 4

# se pide ingresar monto inicial y el incremento en el ahorro mes a mes 
monto_inicial = int(input("indique el monto inicial para comenzar a ahorrar: "))
incremento = int(input("indique por cuanto quiere ir incrementando el ahorro inicial mes a mes: "))
i = None
total_ahorro = 0

# se crea estructura repetitiva
# se calculara cuanto debe ahorrar cada mes y 
# cuanto es el total del ahorro
for i in range(0,12):
    ahorro = monto_inicial + (i *incremento)
    total_ahorro = total_ahorro + ahorro
    print("mes: ", i)
    print("el ahorro de este mes quedaria en: ", ahorro)

print("el total ahorrado seria de: ", total_ahorro)
