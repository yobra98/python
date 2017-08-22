#53:faça a mesma coisa do 52, sem usar o fatiamento, ambas as listas vão receber os 2 valores, explique pq isso acontece.

cosmeticos = ['sabonete facial','sabonete corporal','hidratante','protetor solar','batom','shampoo']
comprar_cosmeticos = cosmeticos                             #faz a copia da lista cosmeticos para a comprar_cosmeticos sem o slice[:]
print("Tenho estes cosméticos em casa: ")
print(cosmeticos)                                           #exibe a lista original cosmeticos
print("\nPreciso abastecer minha casa com estes produtos:")
print(comprar_cosmeticos)                                   #exibe a copia da lista original na lista comprar_cosmeticos
