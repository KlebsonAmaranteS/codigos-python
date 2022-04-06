#Questão 3

def determinanteEhNulo(matriz):
    for i in range(len(matriz)):
        linhas = []
        colunas = []
        for j in range(len(matriz[0])):
            linhas.append(matriz[i][j])
            colunas.append(matriz[j][i])
            cont = 0
        for ind in range(len(linhas)):
            if linhas[ind]==0:
                cont+=1
                if cont == len(colunas):
                    return (True)

            cont = 0
        for ind in range(len(colunas)):
            if colunas[ind]==0:
                cont+=1
        if cont == len(linhas):
            return (True)
    return (False)
    

linhas = int(input('Digite a quantidade de linhas da sua matriz: '))
colunas = int(input('Digite a quantidade de colunas da sua matriz: '))
matriz = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append(int(input('Digite o valor da matriz [' + str(i) + ',' + str(j) + ']: ')))
    matriz.append(linha)
    for i in range(len(matriz)):
        print(matriz[i])
print(determinanteEhNulo(matriz))