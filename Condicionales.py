#Hacer un programa que simule un cajero automatico con un saldo inicial de $1000. Y tendra las siguientes opciones

## 1. Ingresar dinero en la cuenta
## 2. Retirar dinero de la cuenta
## 3. Mostrar saldo de la cuenta
## 4. Salir del programa

saldo=1000

print("Bienvenido al cajero automatico")
print("\t.:MENU:.")
print("1. Ingresar dinero en la cuenta")
print("2. Retirar dinero de la cuenta")
print("3. Mostrar saldo de la cuenta")
print("4. Salir del programa")
opcion = int(input("Digite una opcion: "))


if opcion == 1:
    dinero= float(input("Ingrese el valor del dinero: "))
    saldo= saldo+dinero
    print("El saldo actual es: $", saldo)
elif opcion == 2:
    dinero= float(input("Ingrese el valor del dinero: "))
    if dinero > saldo:
        print("No tiene suficiente saldo")
    saldo= saldo-dinero
    print("El saldo actual es: $", saldo)
elif opcion == 3:
    print("El saldo actual es: $", saldo)
elif opcion == 4:
    print("Gracias por usar el cajero automatico")
else:
    print("Opcion no valida")
    print("Gracias por usar el cajero automatico")