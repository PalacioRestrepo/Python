from collections import deque
def mensajesEncriptados(cadena):
    lista = deque()
    for ch in cadena:
        if ch == "(":
            lista.append(ch)
        elif ch == ")":
            lista.pop()

def contrasenyas(cadena,n):
    lista = deque()
    contrasenyasRec(cadena, "", n, lista)
    return lista
def contrasenyasRec(pregunta, respuesta, n, lista):
    if n == 0:
        lista.append(respuesta) # O(1)
    else:
        for ch in pregunta:
            contrasenyasRec(pregunta, # O(k^n)
                            respuesta + ch, n-1,
                            lista)
def main():
    lista = contrasenyas([";","d3n13l","daniel","danielito","567567","2001","454254"],2)
    print(lista)
main()