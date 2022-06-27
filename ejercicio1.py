##Ejercicio1: escribir la siguiente expresion en forma algoritmica:
# a3 x (b2 - 2ac)/2b

# a=float(input("Ingrese el valor de a: "))
# b=float(input("Ingrese el valor de b: "))
# c=float(input("Ingrese el valor de c: "))
# resultado= (a**3)*(b**2-2*a*c)/(2*b)
# print("El resultado es: ", resultado)

##Ejercicio 2: Determinar la solucion logica de la siguiente operacion:
## ((3+5*8)< 3 and ((-6/3*4)+2 < 2))  or (a > b)

# a= float(input("Ingrese el valor de a: "))
# b= float(input("Ingrese el valor de b: "))

# resultado= ((3+5*8 < 3 and (-6/3*4)+2<2)) or (a>b)
# print("El resultado es: ", resultado)

#Ejercicio 3: hacer un programa para intercambiar el valor de 2 variables
#a=10 -> a=5
# b =5 -> b=10
# a=int(input("Ingrese el valor de a: "))
# b=int(input("Ingrese el valor de b: "))
# a,b=b,a
# print("El valor de a es: ", a)
# print("El valor de b es: ", b)

#Ejercicio 4: Hacer un programa para ingresar el radio de un circulo y se reporte su area y la longitud de la circunferencia

# radio= float(input("Ingrese el valor del radio: "))
# area= 3.1416*(radio**2)
# longitud= 2*3.1416*radio
# print("El area es: ", area)
# print("La longitud es: ", longitud)

#Ejercicio 5: Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea saber cuanto debe pagar finalmente.

totalCompra= float(input("Ingrese el valor de la compra: "))
descuento= totalCompra*0.15
totalPagar= totalCompra-descuento
print("El total a pagar es: ", totalPagar)
