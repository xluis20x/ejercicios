def division(x,y):
    if x<y:
        return 0
    else:
        return 1+division((x-y),y)
print (division(10,2))
