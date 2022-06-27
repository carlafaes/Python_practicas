#Ejercicio 2
#Escriba un programa que tenga dos listas y que, a continuacion, cree las siguientes listas (en las que no debe haber repeticiones):
#Lista de elementos que aparecen en dos listas
#Lista de elementos que aparecen en la primera lista pero no en la segunda
#Lista de elementos que aparecen en la segunda lista pero no en la primera
#Lista de elementos que aparecen en ambas listas

lista1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
lista2=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#Elimine los elementos repetidos de ambas listas
a=set(lista1)
b=set(lista2)
union=list(a | b)#Union de ambas listas
interseccion=list(a & b)#Interseccion de ambas listas
soloA= list(a - b)#Solo en la lista 1
soloB= list(b - a)#Solo en la lista 2