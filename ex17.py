## 17: Crie um script que  remova o ultimo elemento da lista com método pop(), armazene em uma segunda variável,
# e faça a concatenação dele com uma frase “string” que comece com a primeira letra maiúscula .

l_compras = ['ovos', 'leite', 'iogurte', 'suco natural']

print(l_compras)
popped_l_compras = l_compras.pop()  ## esse método remove o último item da lista, apenas visualmente, sem excluir o registro

print('Este item foi removido da sua lista de compras: ' + popped_l_compras.title()) ## exibe o ultimo item retirado da lista
print(l_compras)        ## exibe a lista atualizada, sem o último item