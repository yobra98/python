##40:Crie um script com range() quem mostre a saída com números de 1 a 5 em forma de lista explique.

print('\nRange de numeros de 1 a 6:\n')     #exibe a saida na tela os numeros de 1 ate 5, um por linha
for numeros in range(1,6):
    print(numeros)

print('\nRange de numeros de 1 a 6 em forma de lista:\n')       #exibe a saida na tela os numeros de 1 ate 5, em lista numa unica linha
numeros = list(range(1,6))
print(numeros)