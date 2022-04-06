#Questão 2

def converteBinarioEmHexadecimal(lista):
    dicionarioHex = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    TempHexadecimal = []
    hexadecimal = []
    while len(lista) < 16:
        lista.insert(0, 0)
    for i in range(0, 16, 4):
        fatiamento = lista[i:i + 4]
        fatiamento.reverse()
        for j in range(4):
            calcule = fatiamento[j]*2**j
            TempHexadecimal.append(calcule)
        soma = sum(TempHexadecimal[i:i+4])
        if(soma) >= 10:
            hexadecimal.append(dicionarioHex[soma])
        else:
            hexadecimal.append(soma)
               
    return hexadecimal

converteBinarioEmHexadecimal()