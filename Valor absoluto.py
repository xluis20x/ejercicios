def valor(n):
    if n > 0:
        return n
    else:
        return valor(n*(-1))


num = -5

print(num,valor(num))
