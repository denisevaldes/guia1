#Una empresa constructora vende terrenos con la forma A de la figura. Se requiere crear un programa
#para obtener el área respectiva de un terreno de medidas de cualquier valor.
#Figura 3: Representación gráfica de los puntos en el plano cartesiano.
#Para resolver este problema se debe identificar que la forma A está compuesta por dos figuras: un
#triángulo de base B y de altura (A - C); y por otro lado, un rectángulo que tiene base B y altura C y
#la suma de ambas áreas es el resultado final.


a = float(input("ingrese la altura a: "))
b = float(input("ingrese la medida de b: "))
c = float(input("ingrese la medida de c: "))

altura_triangulo = a - c

area_triangulo = (altura_triangulo * b) / 2
area_rectangulo = b * c 
area_total = area_triangulo + area_rectangulo

print("el area de del terreno es de: ", area_total)