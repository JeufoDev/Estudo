def duplicado(lista):
    #contador de respostas duplicadas
    resp = 0
    for i in range(len(lista)):
        #contador que sempre vai zerar com o inicio do laço
        cont = 0
        #variavel auxiliar que vai receber resutado por resultado da lista
        aux = lista[i]
        #vai percorer os valores da lista e comparar com a variavel aux
        for e in lista:
            #caso apareça mais de uam vez ele vai somar 1 no contador
            if aux == e:
                cont+=1
            #se o contador tiver mais de 1 significa dzr que algum numero se repetiu, entao adiciona 1 na resposta
            if cont > 1:
                resp +=1
    #se a resposta for diferente de zero, entao sabemos que existe numeros repetidos
    if resp != 0:
        print("Duplicado")
    else:
        print("Não duplicado")


duplicado([1,2])