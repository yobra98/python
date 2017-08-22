## 25:Crie um script que inverte a ordem da lista, mais que vc possa reverter  para a forma anterior.

print("Lista de compras original: ")
l_compras = ['óleo', 'macarrão', 'café', 'arroz', 'feijão', 'fraldas']
print(l_compras)

print("\nLista de compras ordenada em ordem inversa(não é ordem alfabética!): ")
l_compras.reverse()
print(l_compras)      ## a função reverse altera permanentemente a lista

print("\nLista de compras original novamente: ")
l_compras.reverse()
print(l_compras)      ## a função reverse aplicada para alterar novamente a lista de forma permanente


