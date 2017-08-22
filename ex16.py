## 16: Crie um script que remova o ultimo elemento da lista de forma que vc ainda possa usar o elemento removido.  explique  o método.

l_compras = ['ovos', 'leite', 'iogurte', 'suco natural']
print(l_compras)

popped_l_compras = l_compras.pop()  ## esse método remove o último item da lista, apenas visualmente, sem excluir o registro

print(popped_l_compras) ## exibe o ultimo item retirado da lista
print(l_compras)        ## exibe a lista atualizada, sem o último item