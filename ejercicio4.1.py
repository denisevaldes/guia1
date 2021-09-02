#4. Se requiere un programa para determinar 
# cuánto ahorrará una persona en un año, si al final de cada
#mes deposita variables cantidades de dinero; 
# además, se requiere saber cuánto lleva ahorrado cada mes

monto_inicial = int(input("indique el monto inicial para comenzar a ahorrar: "))
incremento = int(input("indique por cuanto quiere ir incrementando el ahorro inicial mes a mes: "))
i = 0
ahorro = 0

for i in range(0,12):
    ahorro = monto_inicial + (i *incremento)
    print("mes: ", i)
    print("el ahorro de este mes quedaria en: ", ahorro)

print("el total ahorrado seria de: ", ahorro)
