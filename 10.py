def idan(x):
    
    lista=[]
    
    while len(lista)<y:
        x=int(input())
        lista=lista+[x]
        a=lista[-1]
        
        for i in lista[:len(lista)-1]:  
            if a==i:
                print("There is a duplicate in the list")
                
y=int(input("How many  numbers in your list?"))  
idan(y)
