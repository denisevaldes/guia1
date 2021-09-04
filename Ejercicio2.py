#ejercicio 2

# se inicia variable en None y se pide al usuario ingresar una palabra
x = None 
x = input("ingrese una palabra: ")
#dependiendo de la respuesta se devolvera un "hola" o un "no entiendo tu mensaje"
if x == "Hola":
    print("chao")
else:
    print("no entiendo tu mensaje:", x)
