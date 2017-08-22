## 29:Desafio extra: Crie um programa que tenha: (uma lista de carros, um comprador, e um vendedor) o vendedor vai falar: seja bem vindo.
## O comprador vai perguntar quantos carros tem na concessionária, use o len() para isso, em seguida, o comprador faz outra pergunta.
## Quais são os carros? O vendedor vai Responder: quais são ,  passe a posição de cada carro, que seja exibida todos com letras maiúsculas .
## O comprador vai gostar de um carro , então faça uma frase, que fale qual carro , ele gostou passando a posição.
## Por último ele pergunta o preço , o vendedor responde: , e ele dar risada e fala que está barato

comprador = 'Rogério'
vendedor = 'André'
carros = []
l_carros = []
preco = []
l_preco = []

carros.append('Peugeot 207 prata')
carros.append('Golf TGI 2.0 preto')
carros.append('Audi A1 Sportback branco')
carros.append('Volkswagen Up 1.6 vermelho')
carros.append('Volkswagen Fox 1.6 amarelo')
carros.append('Mini Cooper Countryman chumbo')
carros.append('Honda Fit 2.0 azul marinho')
carros.append('Toyota Corolla 1.8 prata')
carros.append('Bmw ix35 Branco')
carros.append('Range Hover preto')

preco.append('37.000.00')
preco.append('100.000.00')
preco.append('115.000.00')
preco.append('42.000.00')
preco.append('47.500.00')
preco.append('122.000.00')
preco.append('93.000.00')
preco.append('83.000.00')
preco.append('135.000.00')
preco.append('285.000.00')

print("\n" + vendedor + ": " + "Seja Bem vindo! Eu sou o vendedor: " + vendedor + "." + " Qual seu nome, e em que posso ajudar?")
print("\n" + comprador + ": " + "Olá, eu me chamo: " + comprador + "." + " Quantos carros tem na loja e quais são eles?")

for carro in carros:
    l_carros.append(carro.upper())
    l_preco.append(preco)

print("\n" + vendedor + ": " + "Temos " + str(len(l_carros)) + " carros e são eles: \n")

i = 0
for c in l_carros:
    print(c, "\t" + preco[i])
    i += 1

print("\n" + comprador + ": " + "Então, " + vendedor + " Eu gostei do carro: " + carros[9] + "." + " Qual o preço dele?")
print("\n" + vendedor + ": " + "O carro: " + carros[9] + " custa: R$" + preco[9])
print("\n" + comprador + ": " + "Não acredito!! kkk só isso? Embrulha dois " + carros[9] + " pra viagem entao =D ")