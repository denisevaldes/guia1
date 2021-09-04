#ejercicio 5

#se pide que se ingrese el numero de personas al que se le calculara la edad
total_personas = int(input("indique el total de las personas para calcular su edad: "))
indice = None
suma_edades = 0
# for se repetira hasta alcanzar el total_personas
# dentro de estructura for se calculara la edad de las personas
for indice in range(0,total_personas):
    print("persona ", indice+1)
    año_nacimiento = int(input("indique el año de nacimiento: "))
    edad =  2021 - año_nacimiento
    #variable suma se ocupa de ir sumando todas las edades
    # con esto luego se calculara la edad promedio
    suma_edades = suma_edades + edad
    print("la edad de la persona es: ", edad)

#se calcula y muestra en pantalla la edad promedio
promedio = suma_edades/total_personas
print("la edad promedio es de: ", promedio)
