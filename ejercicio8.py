#Se requiere obtener el área de la figura en
#la forma A de la siguiente imagen. Para resolver este problema
#se puede partir de que está formada por tres
#figuras: dos triángulos rectángulos, con H como hipotenusa
#y R como uno de los catetos, que también es el radio de la 
#otra figura, una semicircunferencia que forma
#la parte circular (ver forma B).
#Figura 1: Forma del terreno y cómo se puede interpretar.
#Por lo tanto, para poder resolver el problema, se tiene
#  que calcular el cateto faltante, que es la altura
#del triángulo, con ésta se puede calcular el área del triángulo,
#  y para obtener el área total triangular
#se multiplicará por dos. Por otro lado, para calcular el área
#  de la parte circular, se calcula el área de
#la circunferencia y luego se divide entre dos, ya que representa solo la mitad del cı́rculo.

hipotenusa = int(input("ingresa la hiputenusa: "))
r = int(input("por favor ingresa  medida de un r: "))

primer_paso = hipotenusa**2 - r**2
cateto_faltante = primer_paso**0.5

area_triangulo = ((r * cateto_faltante) / 2)*2

circunferencia = (3.14159265359 * r**2) / 2

print("el area de los triangulos es: ", area_triangulo)
print("el area de la mitad de la circunferencia es: ", circunferencia)
print("el area total de la figura original es: ", area_triangulo+circunferencia)
