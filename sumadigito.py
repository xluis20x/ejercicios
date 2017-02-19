def suma(n):
    if n == 0:
        return n
    else:
        return n%10+suma(n/10)

num = 1250

print (num,suma(num))
