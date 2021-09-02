#Una empresa que contrata personal requiere determinar 
#la edad de cada una de las personas que
#solicitan trabajo, pero cuando se les realiza la
#entrevista solo se les pregunta el año en que nacieron.
#También se requiere el promedio de edad de las personas contratadas.

total_personas = int(input("indique el total de las personas que solicitan trabajo: "))
indice = 0
suma = 0

for indice in range(0,total_personas):
    print("persona ", indice+1)
    año_nacimiento = int(input("indique el año de nacimiento: "))
    edad =  2021 - año_nacimiento
    suma = suma + edad
    print("la edad de la persona es: ", edad)

promedio = suma/total_personas
print("la edad promedio es de: ", promedio)
#a esta wea le falta la mierda de las personas contratadas, pero la verdad no entiendo na 
