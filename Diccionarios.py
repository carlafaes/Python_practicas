# ¿Qué es un diccionario en Python? Los diccionarios en Python nos permiten almacenar una serie de mapeos entre dos conjuntos de elementos, llamados keys and values (Claves y Valores). Todos los elementos en el diccionario se encuentran encerrados en un par de corchetes {}

diccionario={}#diccionario vacio
diccionario={1:"uno",2:"dos",3:"tres"}#diccionario con elementos
print(diccionario)

diccionario[4]="cuatro"#agrega un elemento al diccionario
print(diccionario)

diccionario.pop(4)#elimina un elemento del diccionario
print(diccionario)

del(diccionario[1])#elimina un elemento del diccionario
print(diccionario)

vasos={"vaso1":"rojo","vaso2":"azul","vaso3":"rosado"}
print(vasos.get("vaso1","no se encuentra en el diccionario"))#retorna el valor del elemento si esta, sino retorna el valor por defecto

print(vasos.keys())#retorna las claves del diccionario
print(vasos.values())#retorna los valores del diccionario
print(vasos.items())#retorna los pares clave-valor del diccionario
