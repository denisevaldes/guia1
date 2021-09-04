#ejercicio 8

#se pide ingresar medida de hipotenusa y r(radio y cateto)
hipotenusa = int(input("ingresa la hiputenusa: "))
r = int(input("por favor ingresa  medida de un r: "))
#se calcula el cateto faltante y con eso se calcula el area de triangulo
#se calcula circunferencia 
cateto_faltante = ((hipotenusa**2 - r**2)**(0.5))
area_triangulo = ((r * cateto_faltante) / 2)*2
circunferencia = (3.14159265359 * r**2) / 2

print("el area de los triangulos es: ", area_triangulo)
print("el area de la mitad de la circunferencia es: ", circunferencia)
print("el area total de la figura original es: ", area_triangulo+circunferencia)
