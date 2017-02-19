def multi(x,y):
    if y < 1:
        return 0
    else:
        return x+ multi(x,(y-1))

print (multi(5,2))
        
