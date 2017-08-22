#42:Crie um script com duas variáveis , a 1 com uma lista vazia ficará (fora) do loop, a 2 vai receber um range de números de
#  1 a 10 (dentro) do loop for ao quadrado **, por último adicione os valores da segunda  variável a lista vazia, explique o método .

lista = []                  #lista vazia
for valor in range(1,11):   #para cada ocorrencia de valor no intervalo entre 1 e 11(para exibir 10)
    quadrado = valor**2     #a variavel quadrado recebe o valor da variavel valor, ao quadrado
    lista.append(quadrado)  #insere o resultado do calculo da variavel quadrado na lista
print('Lista de numeros de 1 a 10:\n')
print(list(range(1,11)))                  #exibe a lista de numeros
print('\nLista de numeros de 1 a 10 com resultado ao quadrado:\n')
print(lista)                    #exibe o resultado na lista

