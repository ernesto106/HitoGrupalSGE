# las lista soportan cualquier tipo de dato
lista=["juan",True,15,17.9,'madrid']
print(lista)

#las listas son mutables : el valor de sus elementos puede cambiar
lista[1]="dato cambiado"
print(lista)

# Acceder a un subconjunto de elementos de una lista
print(lista[2:3])

# El método len(), que devuelve la longitud de la lista,
len(lista)

# el metodo index() método recibe un elemento como argumento, y devuelve el índice de su primera aparición en la lista.
print(lista.index("juan"))

# el metodo pop devuelve el último elemento de la lista, y lo borra de la misma.
lista.pop()
print(lista)