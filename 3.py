def idan (num):
    lista = []
    
    while len(lista)<numb:
        num = int(input())
        lista = lista + [num]
        
    for x in lista:
        if x > num:
            num = x
    return (num)
    
numb = int(input("how many"))
idan(numb)
