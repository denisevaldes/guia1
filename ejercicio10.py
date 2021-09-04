#ejercicio 10

#se pide ingresar lados del terreno
lado_a = float(input("ingrese la medida de lado a: "))
lado_b = float(input("ingrese la medida de lado b: "))
lado_c = float(input("ingrese la medida de lado c: "))
#se calcula altura de triangulo para calcular el area del triangulo
altura_triangulo = lado_a - lado_c
area_triangulo = (altura_triangulo * lado_b) / 2
# se calcula area de rectangulo para luego calcular el area total
# sumando las areas encontradas anteriormente
area_rectangulo = lado_b * lado_c 
area_total = area_triangulo + area_rectangulo

print("el area de del terreno es de: ", area_total)