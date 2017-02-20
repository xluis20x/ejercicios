def reversa(lista):
    if len(lista) == 0:
        return []
    else:
        return [lista[-1]]+reversa(lista[:-1])
print (reversa([2,4,6]))

