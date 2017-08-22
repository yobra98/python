#43:Faça a mesma coisa do (42) só que sem a variável dentro do loop explique.

lista = []                                  #lista vazia
for valor in range(1,11):                   #para cada ocorrencia de valor no intervalo entre 1 e 11(para exibir 10)
    lista.append(valor**2)                  #calcula o resultado da variavel valor ao quadrado e adiciona direto na lista
print('Lista de numeros de 1 a 10:\n')
print(list(range(1,11)))                    #exibe a lista de numeros
print('\nLista de numeros de 1 a 10 com resultado ao quadrado:\n')
print(lista)                                #exibe o resultado na lista

