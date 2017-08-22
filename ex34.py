##34:Crie um script com uma lista , exiba 2 msgs na tela, ambas vão ter interação com o loop for,  a segunda msg  estará
#  fora do bloco, e so vai ser executada ao final do loop, apenas o ultimo elemento da lista aparecerá na 2msg, explique por que isso acontece.

pessoas = []     #lista de pessoas inicia vazia
l_pessoas = []   #lista l_pessoas inicia vazia

mensagem = []
l_mensagem = []

mensagem2 = 'Pronto para o próximo desafio!'

pessoas.append('Patricia')      #append adiciona item a item preenchendo a lista
pessoas.append('Priscila')
pessoas.append('Rogerio')
pessoas.append('Carlos')
pessoas.append('Fernando')
pessoas.append('Adriano')
pessoas.append('Steicy')
pessoas.append('Soraia')
pessoas.append('Giovane')
pessoas.append('Alessander')

mensagem.append('Você é bonito(a)')
mensagem.append('Você é boa pessoa')
mensagem.append('Você é inteligente')
mensagem.append('Você é esforçado(a)')
mensagem.append('Você é honesto(a)')
mensagem.append('Você é autodidata')
mensagem.append('Você é emotivo(a)')
mensagem.append('Você é companheiro(a)')
mensagem.append('Você é ético(a)')
mensagem.append('Você é gentil')

#mensagem2.append('Pronto para o próximo desafio!')

print("\nLista de pessoas: \n")

for pessoa in pessoas:                  #para cada elemento pessoa(contador interno) na lista pessoas
    l_pessoas.append(pessoa.upper())    #adiciona um item da lista l_pessoas, preenchendo a lista
    l_mensagem.append(mensagem)         #adiciona um item da lista l_mensagem, preenchendo a lista

i = 0                                   #contador interno i iniciando em 0
for c in l_pessoas:                     #para cada ocorrencia de c(contador interno) em l_pessoas
    print("\nPessoa Número: ", i, c, mensagem[i]) #exibe o conteudo da variavel c gerado por l_pessoas, criando a listagem, e o índice i
    i += 1                              #conta +1 a cada passagem do laço para o próximo

print(mensagem2.upper())                        #a mensagem2 aparece apenas apos o termino do loop, que indica a saida do laço de repetição
