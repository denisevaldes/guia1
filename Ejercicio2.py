#Inicialice una variable en None y si la palabra ingresada es “Hola” debe imprimir Chao, caso contrario
#debe decir, no entiendo tú mensaje e imprimir el valor de la variable.

x = None 
x = input("ingrese una palabra: ")

if x == "Hola":
    print("chao")
else:
    print("no entiendo tu mensaje:", x)
