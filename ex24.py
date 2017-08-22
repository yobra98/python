## 24:Crie um script que altere a ordem da lista de forma alfabética, mais que não altere o valor real

print("Lista de compras original: ")
l_compras = ['óleo', 'macarrão', 'café', 'arroz', 'feijão', 'fraldas']
print(l_compras)

print("\nLista de compras ordenada em ordem alfabética: ")
print(sorted(l_compras))    ## a função sorted não altera permanentemente a lista, organiza apenas para a exibição ordenada

print("\nLista de compras original novamente: ")
print(l_compras)
