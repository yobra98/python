## 20: Crie um script com uma lista depois armazene um elemento da lista, em uma variável ,remova o elemento da lista, com o método  .remove()
#  faça a concatenação usando o segundo valor da variável, com uma frase ‘string’  observe que o remove apenas elimina a primeira
# ocorrência explique pq isso acontece .

l_compras = ['ovos', 'leite', 'iogurte', 'suco natural']
print(l_compras)

aumentou_preco = 'iogurte'
l_compras.remove(aumentou_preco)

print("\nO item " + aumentou_preco.title() + " aumentou o preço e não vou comprar este mês.\n")

print(l_compras)        ## exibe a lista atualizada, sem o último item