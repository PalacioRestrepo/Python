class Nodo:
    def __init__(self,dato):
        self.__dato__ = dato
        self.__siguiente__ = None
def insertarEnLaMitad(head, dato):
    n = tamanhoLista(head)
    i = n//2
    nodoMitad = obtenerElNodoEn(head, i-1)
    nuevoNodo = Nodo(dato)
    nuevoNodo.__siguiente__ = nodoMitad.__siguiente__
    nodoMitad.__siguiente__ = nuevoNodo

def borrarEnLaMitad(head):
    n = tamanhoLista(head)
    i = n//2
    nodoMitad = obtenerElNodoEn(head,i-1)
    nodoMitad.__siguiente__ = nodoMitad.__siguiente__.__siguiente__

def obtenerElElemento(head, i):
    n = tamanhoLista(head)
    if i < 0 or i >= n:
        raise Exception("ojo, no hay esa i = "+str(i))
    return obtenerElNodoEn(head,i).__dato__

def tamanhoLista(head):
    if head == None:
        return 0
    else:
        if head.__siguiente__ == None:
            return 1
        else:
            return 1 + tamanhoLista(head.__siguiente__)

def obtenerElNodoEn(head, i):
    if i <= 0:
        return head
    else:
        if head == None:
            return head
        else:
            return obtenerElNodoEn(head.next, i - 1)

def rotar(head, k: int):
    # El codigo va aqui!
    if k == 0:
        return head
    elif k < 0:
        n = tamanhoLista(head)
        if head == None or n == 1:
            return head
        
        else:
            nuevoprimero = head.next
            nuevoultimo = head
            nuevopenultimo = obtenerElNodoEn(head, n - 1)
            nuevopenultimo.next = head
            nuevoultimo.next = None
            return rotar(nuevoprimero, k + 1)
    else:
        n = tamanhoLista(head)
        if head == None or head.next == None:
            return head
        elif n == 2:
            if (k % 2) == 0:
                return head
            else:
                nodoex = head.next
                nodoex.next = head
                head.next = None
                return nodoex
        else:
            if k >= 1000:
                if (k % tamanhoLista(head)) == 0:
                    k = k // (tamanhoLista(head) * 10)
            nuevoprimero = obtenerElNodoEn(head, n - 1)
            nuevoultimo = obtenerElNodoEn(head, n - 2)
            nuevoprimero.next = head
            nuevoultimo.next = None
            return rotar(nuevoprimero, k - 1)  

def __main__():
    head = Nodo(12)
    nodo1 = Nodo(24)
    nodo2 = Nodo(36)
    nodo3 = Nodo(48)
    head.__siguiente__= nodo1
    nodo1.__siguiente__ = nodo2
    nodo2.__siguiente__ = nodo3
    nodo3.__siguiente__ = None

    print(obtenerElNodoEn(head, 2))

__main__()