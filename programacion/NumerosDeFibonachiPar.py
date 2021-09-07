def  fibonachi(numero):
    sumapar = 0

    if numero == 0 or numero == 1:
        return 0
    else:
        previo1 = 1
        previo2 = 1
        i = 2
        while i < numero:
            if (previo1 + previo2) % 2 == 0:
                sumapar = previo1 + previo2
            temporal = previo1
            previo1 += previo2
            previo2 = temporal
            i += 1
        return sumapar

print(fibonachi(9))