#61:Crie uma condição com um loop for, que contenha uma lista de coisas, faça uma condição,
#Se o elemento da lista for igual ao especificado,’string ‘print ele em letras maiúsculas, senão : print em minúsculas explique.

ingredientes = ['ovos', 'farinha', 'óleo de soja', 'manteiga','leite','açúcar']    # cria a lista
print(ingredientes)                                                                # exibe a lista

for ingrediente in ingredientes:                                                    #para cada ocorrencia do ingrediente na lista ingredientes
    if ingrediente == 'farinha':                                                    #se o item for igual ao digitado(no caso, farinha)
        print("Ingredientes da receita: " + ingrediente.upper())                    #exibe o item em letras maiusculas
    else:                                                                           #caso contrario
        print("Esse ingrediente não faz parte da receita " + ingrediente.lower() + ".") #exibe que o item nao faz parte da lista, em minuscula
print("\nFim dos itens!")