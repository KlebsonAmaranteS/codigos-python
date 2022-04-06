### Questão 3 - A série de FETUCCINE é gerada da seguinte forma: os dois primeiros termos são
#fornecidos pelo usuário; a partir daí, os termos são gerados com a soma ou subtração
#dos dois termos anteriores, ou seja:

#Faça um programa em Python para mostrar os N primeiros termos da série de FETUCCINE,
#sabendo-se que para existir esta série serão necessários pelo menos três termos.


termo_1 = termo_2 = int()
cont_termos = 0
qtd_termos = int(input("Quantos termos deseja que sejam mostrados: "))

while qtd_termos <= 2:
    print('Quantidade de termos inválida')
    qtd_termos = int(input("Quantos termos deseja que sejam mostrados: "))

    

termo_1 = int(input("Informe o valor de termo 1: "))
termo_2 = int(input("Informe o valor de termo 2: "))
print(termo_1, end=" - ")
print(termo_2, end=" - ")    



for i in range(3, qtd_termos + 1):
    if (i % 2 == 0):
        cont_termos = termo_2 - termo_1
    else:
        cont_termos = termo_2 + termo_1
        termo_1 = termo_2
        termo_2 = cont_termos

    print(cont_termos, end = " - ")