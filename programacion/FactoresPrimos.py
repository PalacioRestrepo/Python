def FactoresPrimos(numero, i):
    if numero == 1:
        return 1 
    else:
        while i < 100:
            if (numero % i) == 0:
                break
            i += 1
        EsPrimo(i, primos)    
        return FactoresPrimos(numero/i, 2)

#buscar uno primo e imprimirlo
def EsPrimo (i, s):
    cont = 0
    j = 2
    while j < i:
        if (i % j) == 0:
            cont += 1 
            break
        elif i == 2:
            cont -= 1
        j += 1      
    if cont > 0:
        return False
    else:
        primos.add(i)
        return True

#FactoresPrimos(13195, 100)
primos = set()
FactoresPrimos(13195, 2)
print(primos)