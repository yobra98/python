## 30:Crie um script que mostre os elementos de sua lista na tela, usando o loop for e explique.

carros = []     #lista de carros inicia vazia
l_carros = []   #lista l_carros inicia vazia

carros.append('Peugeot 207 prata')      #append adiciona item a item preenchendo a lista
carros.append('Golf TGI 2.0 preto')
carros.append('Audi A1 Sportback branco')
carros.append('Volkswagen Up 1.6 vermelho')
carros.append('Volkswagen Fox 1.6 amarelo')
carros.append('Mini Cooper Countryman chumbo')
carros.append('Honda Fit 2.0 azul marinho')
carros.append('Toyota Corolla 1.8 prata')
carros.append('Bmw ix35 Branco')
carros.append('Range Hover preto')

print("\nLista dos carros: \n")

for carro in carros:                #para cada elemento carro(contador interno) na lista carros
    l_carros.append(carro.upper())  #adiciona um item da lista l_carros em maiuscula, preenchendo a lista l_carros

for c in l_carros:                  #para cada elemento c(contador interno) em l_carros
    print(c)                        #exibe o conteudo da variavel c gerado por l_carros, criando a listagem
