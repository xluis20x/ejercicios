

def factorial(n):
  
   if n == 1:
       return n
   else:
       return n*factorial(n-1)


num = 9

if num < 0:
   print("imposible")
elif num == 0:
   print("da 1")
else:
   print(num,factorial(num))
