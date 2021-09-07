def equilibra(personas):
    #codigo aqui
    if personas == None:
        return None, None
    elif (len(personas)%2) == 0:
        arreglo1 = []
        arreglo2 = []
        personas.sort()
        return equilibraPar(arreglo1, arreglo2, personas, len(personas))
    else:
        arreglo1 = []
        arreglo2 = []
        personas.sort()
        return equilibraImpar(arreglo1, arreglo2, personas, len(personas))

def equilibraImpar(arreglo1, arreglo2, personas, n):
    if len(personas) == 0:
        return arreglo2, arreglo1
    else:
        if len(personas) > n//2:
            arreglo1.append(personas[0])
            return equilibraImpar(arreglo1, arreglo2, personas[1:], n)
        else:
            arreglo2.append(personas[0])
            return equilibraImpar(arreglo1, arreglo2, personas[1:], n)

def equilibraPar(arreglo1, arreglo2, personas, n):
    if len(personas) == 0:
        return arreglo2, arreglo1
    else:
        if len(personas) <= n//2:
            arreglo1.append(personas[0])
            arreglo2.append(personas[1])
            return equilibraPar(arreglo1, arreglo2, personas[2:], n)
        else:
            arreglo2.append(personas[0])
            arreglo1.append(personas[1])
            return equilibraPar(arreglo1, arreglo2, personas[2:], n)



def main():
    personas = [80,59,60,81,57,58,76,75]
    nadie = None
    personasimparwtf = [26,58,72,71,59]
    #print(len(personasimparwtf)//2)
    print(equilibra(personas))
    print(equilibra(nadie))
    print(equilibra(personasimparwtf))
main()