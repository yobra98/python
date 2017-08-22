#45:Crie um script com o mesmo resultado dos desafios anteriores 42,43 com apenas 1 linha dento de uma lista [] essa forma
#  e chamada de Lista de Compreensões explique .

print('Lista de numeros de 1 a 10:\n')
print(list(range(1,11)))                    #exibe a lista de numeros

print('\nLista de numeros de 1 a 10 com resultado ao quadrado:\n')
#simplificacao de codigo para exibir tanto os numeros ao quadrado como publicar tudo em uma mesma lista
quadrado = [valor**2 for valor in range(1,11)]
print(quadrado)