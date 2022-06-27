##Ejercicio1: escribir la siguiente expresion en forma algoritmica:
# a3 x (b2 - 2ac)/2b

a=float(input("Ingrese el valor de a: "))
b=float(input("Ingrese el valor de b: "))
c=float(input("Ingrese el valor de c: "))
resultado= (a**3)*(b**2-2*a*c)/(2*b)
print("El resultado es: ", resultado)