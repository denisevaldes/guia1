#4. Se requiere un programa para determinar 
# cuánto ahorrará una persona en un año, si al final de cada
#mes deposita variables cantidades de dinero; 
# además, se requiere saber cuánto lleva ahorrado cada mes

i = 0
cantidad_ahorrada = 0

for i in range(0,12):
    print("mes", i+1)
    ahorro = int(input("indique la cantidad ahorrada este mes: "))
    cantidad_ahorrada =  ahorro + cantidad_ahorrada
    print("la cantidad ahorrada hasta ahora es de: ", cantidad_ahorrada)

print("cantidad ahorrada a finalizar el año: ", cantidad_ahorrada)