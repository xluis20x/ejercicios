def palindroma(palabra):
    if palabra != palabra[::-1]:
        return "no es palindroma"
    else:
        return "es palindroma" 

print (palindroma("acaca"))



    
