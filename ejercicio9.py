#Se requiere obtener la distancia entre dos puntos en el plano cartesiano, tal y como se muestra en la
#figura siguiente.
#Figura 2: Representación gráfica de los puntos en el plano cartesiano.
#Para resolver este problema es necesario conocer las coordenadas de cada punto (X, Y), y con esto
#poder obtener el cateto de abscisas (X 1 y X 2 ) y el de ordenadas (Y 1 e Y 2 ), y mediante estos valores
#obtener la distancia entre P 1 y P 2 , utilizando el teorema de Pitágoras.


x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))

x2 = int(input("ingrese el valor de x2: "))
y2 = int(input("ingrese el valor de y2: "))

base = x2 - x
vertical = y2 - y

distancia = (base**2 + vertical**2)
raiz_cuadrada = distancia**0.5

print ("la distancia entre dos puntos es: ", raiz_cuadrada)