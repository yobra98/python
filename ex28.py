## 28:Crie um script que tente acessar uma posição em sua lista, maior que os elementos que
## nela possui, vai ocorrer um erro, explique pq isso acontece.

print("Lista de compras original: ")
l_compras = ['óleo', 'macarrão', 'café', 'arroz', 'feijão', 'fraldas']
print(l_compras)

print("\nNúmero de itens da Lista de compras: ")
print(len(l_compras))       ## a função len() conta o numero de itens de uma lista

print("\nAcessar item Número 7 da Lista de compras: ")
print(l_compras[6]) ## exibe o erro list index out of range, porque indice 6 da lista não existe,
                    # pois corresponderia ao item 7 que a lista não possui, o correto seria ou adicionar mais um item à lista ou
                    # exibir o item l_compras[5], que corresponde ao tamanho correto da lista