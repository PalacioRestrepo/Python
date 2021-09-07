
def sat(M,i,j,d,k):
    if (M[i][j] == '*'):
        return d
    elif (M[i][j] == '#'):
        return k
    else:
        return 0
def c(M,i,j,d,k):
    n = len(M)
    m = len(M[0])
    if i>=n or j>=m:
        return 0
    elif i == n-1 and j == m-1:
        return sat(M,i,j,d,k)
    else:
        return sat(M,i,j,d,k) + max(c(M,i,j+1,d,k), c(M,i+1,j,d,k))
    
#Usuario
i,j = map(int, input().split())
d,k = map(int, input().split())
matriz = [["."] * j ] *i 
x = 0
while x < i:
    matriz[x] = input().split()
    x += 1
#print(matriz)
print(c(matriz,0,0,d,k))
#for x in range(0,i):
#    matriz[x] = input().split()
