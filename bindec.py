def bindec(n):
    if n<10:
        return n
    else:
        return (n%10)+bindec(n/10)*2

print (bindec(2))
        
