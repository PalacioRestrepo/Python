def mcd(p, q):
    if p % q == 0:
        return q
    else :
        return mcd(q, p % q)

i = 0
n = int(input())
while i < n:
    largo, ancho =  map(int, input().split())
    print("Case {}: {}".format(i+1, mcd(largo, ancho)))
    i += 1