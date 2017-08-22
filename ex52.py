#52:Crie um script com uma lista faça a copia dela usando fatiamento, adicione um novo  elemento diferente  a cada lista 1 e 2,
#  exiba o resultado na tela , cada lista recebe um valor diferente explique.

cosmeticos = ['sabonete facial','sabonete corporal','hidratante','protetor solar','batom','shampoo']
comprar_cosmeticos = cosmeticos[:]                          #faz a copia da lista cosmeticos para a comprar_cosmeticos
cosmeticos.append('óleo para banho')                        #insere um elemento na lista original
comprar_cosmeticos.append('loção pós-barba')                #insere um elemento diferente na lista copiada para provar que são listas diferentes
print("Tenho estes cosméticos em casa: ")
print(cosmeticos)                                           #exibe a lista original cosmeticos
print("\nPreciso abastecer minha casa com estes produtos:")
print(comprar_cosmeticos)                                   #exibe a copia da lista original na lista comprar_cosmeticos

