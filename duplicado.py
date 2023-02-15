def duplicado(lista):
    for i in range(len(lista)-1):
        for j in range(i+1,len(lista)):
            if lista[i] == lista[j]:
                return True
    return False


a = duplicado([1,2,5,6])

if a == True:
    print("Duplicado")
else:
    print("Não duplicado")
