# ejercicio 9

# se piden los valores de (x,y) y de (x2,y2) para calcular la base y altura
x = int(input("ingrese el valor de x: "))
y = int(input("ingrese el valor de y: "))

x2 = int(input("ingrese el valor de x2: "))
y2 = int(input("ingrese el valor de y2: "))

# se calcula base y altura, con esos datos se calcula distancia entre puntos
base = x2 - x
altura = y2 - y
distancia = ((base**2 + altura**2)**(0.5))

print ("la distancia entre dos puntos es: ", distancia)