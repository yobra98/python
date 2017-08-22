##39:Crie um loop for com a função range() com números de 1 a 5, a saída são apenas números de 1 a 4, explique por que isso acontece.
print('\nRange de numeros de 1 a 5:\n')
for numeros in range(1,5):
    print(numeros)

#a funcao range recebe os numeros que vc delimitou, entao nesse comeca em 1, e mostra ate o quatro porque o segundo valor nunca atinge
# o valor final no laço for, para exibir exatamente de um a 5 o codigo tem que ser:

print('\nRange de numeros de 1 a 6:\n')
for numeros in range(1,6):
    print(numeros)
