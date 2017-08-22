## 18: Faça a mesma coisa do desafio 17: só que passando a posição que vc deseja.

l_compras = ['ovos', 'leite', 'iogurte', 'suco natural']

print(l_compras)
item_l_compras = l_compras.pop(0)  ## esse método remove o item da lista na posição do registro 0, que é o primeiro

print('Este item foi removido da sua lista de compras: ' + item_l_compras.title()) ## exibe o item retirado da lista
print(l_compras)        ## exibe a lista atualizada, sem o último item