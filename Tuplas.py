#tuplas

# ¿Qué es una tupla en Python ejemplos?
# En Python, una tupla es un conjunto ordenado e inmutable de elementos del mismo o diferente tipo. Las tuplas se representan escribiendo los elementos entre paréntesis y separados por comas. Una tupla puede no contener ningún elemento, es decir, ser una tupla vacía.

tupla=()
tupla=(1,2,3,4,5)
print(tupla)
print(tupla[0])

tupla.count(1)#cuenta la cantidad de veces que se repite el elemento
print(tupla.index(1))#retorna el indice del elemento

print(4 in tupla)#retorna true or false
len(tupla)#retorna la cantidad de elementos de la tupla

#convertir una tupla en una lista
lista=list(tupla)
#convertir una lista en una tupla
tupla=tuple(lista)


