#conjuntos
# Un conjunto es una colección no ordenada de objetos únicos. Python provee este tipo de datos «por defecto» al igual que otras colecciones más convencionales como las listas, tuplas y diccionarios.

conjunto= set() #conjunto vacio
conjunto={1,2,3,4,5}#conjunto con elementos
print(conjunto)

conjunto.add(6)#agrega un elemento al conjunto
print(conjunto)

conjunto.discard(6)#elimina un elemento del conjunto
print(conjunto)

a=frozenset{1,2,3,4,5}#conjunto inmutable
b={4,5,6,7,8}
c= a | b #union de a y b
print(c)
c= a & b #interseccion de a y b
print(c)
c= a - b #diferencia de a y b
print(c)
c= a ^ b #diferencia simetrica de a y b
print(c)

d= {1,2,3,4,5}
print(d.issubset(a))#retorna true or false si d es un subconjunto de a
print(d.issuperset(a))#retorna true or false si d es un superconjunto de a
print(d.isdisjoint(a))#retorna true or false si d no tiene elementos en comun con a
