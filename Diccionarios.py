# ¿Qué es un diccionario en Python? Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values (Claves y Valores). Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes {}

diccionario={}#diccionario vacio
diccionario={1:"uno",2:"dos",3:"tres"}#diccionario con elementos
print(diccionario)

diccionario[4]="cuatro"#agrega un elemento al diccionario
print(diccionario)

diccionario.pop(4)#elimina un elemento del diccionario
print(diccionario)
