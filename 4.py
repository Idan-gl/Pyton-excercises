def idan(max):
    max= lista[0]
    for i in lista:
        if len(i)>len(max):
            max=i
    return max

lista=["idan","gamliel","ultradata"]
print(idan(lista))
