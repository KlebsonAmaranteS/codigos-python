# Questão 1 - Três amigos, Carlos, André e Felipe decidiram rachar igualmente a conta de um
#bar. Faça um programa em Python para ler o valor total da conta e imprimir quanto
#cada um deve pagar, mas faça com que Carlos e André não paguem centavos. Ex: uma
#conta de R$101,53 resulta em R$33,00 para Carlos, R$33,00 para André e R$35,53 para
#Felipe.

valor_total = float(input('Valor: '))

if valor_total<=0:
    print('Valor inválido')

else:
        valor_divisão = valor_total/3
        parte_carlos = int(valor_divisão)
        parte_andre = int(valor_divisão)
        calculo = valor_total - parte_andre
        calculo2 = calculo - parte_carlos
        parte_felipe = calculo2
        print(f" O valor total foi: {valor_total}\n O valor de Carlos é: {parte_carlos}\n O valor de André é: {parte_andre}\n O valor de Felipe é: {parte_felipe:.2f}")


