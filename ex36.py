##36:Crie um script que tenha uma lista, faça 3 msgs, as 2 primeiras vão ter interação com a lista no loop for, a 2 msg ,
# vai ter uma quebra de linha no final \n , a 3 msg  vai ser uma qualquer dentro do loop, vai acontecer uma desordem nas msgs,
# tente arrumar e explique, oque aconteceu.


mensagem = 'Filmes em cartaz: '
mensagem2 = 'Ultima exibição para este filme: '
mensagem3 = 'Próximas estréias: '

filmes = ['Mulher Maravilha', 'Minions','Diário de um banana','As aventuras de Pi','Guardiões da Galáxia 2', 'Dunkirk']

print(filmes)

for item in filmes:             #para cada ocorrencia de um item da lista de filmes
    print(mensagem, item)       #exibe a mensagem, seguida do item(filme)
    print(mensagem2, item,"\n") #exibe a mensagem2, seguida do item(filme), e pulando uma linha no final
                                #fim do laço for
print(mensagem3, item)          #exibe a mensagem3 ao termino de todas as intru~ções anteriores