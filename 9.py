def idan(x):
    
    lista=[]
    while len(lista)<y:
        x=int(input())
        lista=lista+[x]
        lista.sort()
    return(lista[-2])
y=int(input("How many numbers are in your list?"))  
idan(y)


def a(z):
    
    lista=[]
    
    while len(lista)<y:
        x=int(input())
        lista=lista+[x]
        max=lista[0]    
        
        
        for i in lista:
            if i>max:
                max=i
                lista.sort()
                
    return(lista[-2])

y=int(input("How many numbers are in your list"))  
print(a(y))
