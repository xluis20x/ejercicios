def mcd(m , n):    
    if m%n == 0:
        return n
    else:
        return mcd(n,m%n)
        
        
num1 = 16
num2 = 10
 
print (mcd(num1,num2))
