def palindroma(x):
    if x[0] != x[-1]:
        return "no es palindroma"
    if len(x) < 2:
        return "es palindroma"
    return palindroma(x[1:-1])
print (palindroma("carro"))

