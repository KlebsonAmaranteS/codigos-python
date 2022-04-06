#Questão 4:


lista1 = [1,2,3,4,5]
lista2 = [-11,12,7,8,9,25,0]

def insereOrdenado(lista1,lista2):
  for i in range(len(lista2)):
    for j in range(len(lista1)):
      if lista2[i] not in lista1:
        if lista1[j] > lista2[i]:
          lista1.insert(j, lista2[i])
          break
        if lista1[-1] < lista2[i] and j <= len(lista2):
          lista1.append(lista2[i])
          print(lista1)
  return lista1
       


print(insereOrdenado(lista1, lista2))