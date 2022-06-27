#Listas
lista=[23,34,45,56,67,78,89,90,91,92,93,94,95,96,97,98,99,100]
#para ordenar ascendentemente
lista.sort()
#para ordenar descendentemente
lista.sort(reverse=True)
#para imprimir la lista
print(lista)
#para imprimir el ultimo elemento de la lista
print(lista[-1])
#para imprimir el primer elemento de la lista
print(lista[0])
#para agregar un elemento a la lista
lista.append(101)
# para quitar un elemento de la lista
lista.pop()
#para insertar un elemento de la lista
lista.insert(0,0) ##indice, valor
#para eliminar mas de un elemento de la lista
lista.remove(23)
#para agregar mas de un elemento a la lista
lista.extend([23,34,45,56,67,78,89,90,91,92,93,94,95,96,97,98,99,100])
#para encontrar un elemento especifico en la lista
print(99 in lista)##retorna true or false
#para encontrar el indice de un elemento especifico en la lista
print(lista.index(99))
#tomar una porcion de la lista
print(lista[0:5])#retorna una lista desde el indice 0 hasta el indice 5
#para contar la cantidad de elementos de una lista
print(len(lista))
#para saber cuantas veces esta el elemento en la lista
print(lista.count(23))

