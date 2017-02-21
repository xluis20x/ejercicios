def minimo(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        n=minimo(lista[1:])
        return n if n < lista[0] else lista[0]
    
print (min([5,3,4,7]))


