def contarX(texto, i):
    
    if(i == len(texto)):
        
        return 0;
    
    if(texto[i] == "x"):
        
        return 1+ contarX(texto, i+1)
    
    return (contarX(texto, i+1))  

texto = input()
print(contarX(texto, 0))