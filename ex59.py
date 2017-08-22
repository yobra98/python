#59:Crie um script com uma tupla e 2 elementos ,faça um loop for na primeira e print o resultado ,
# em seguida altere o valor da variável  com a tupla, novamente  repita outro loop abaixo com a variável alterada,
# e mostre o resultado explique.

tupla = (1000, 2000, 3000)      #tupla de valor definido
for i in tupla:                 #enquanto tiver ocorrencia de i na tupla(contador interno)
    print(i)                    #exibe os valores de i na tela, que é cada item cada vez que passa pelo laço
tupla = (2000, 3000, 4000)      #tupla de valor redefinido
for i in tupla:                 #enquanto tiver ocorrencia de i na tupla(contador interno)
    print(i)                    #exibe os valores de i na tela, que é cada item cada vez que passa pelo laço
                                #permite a alteração dos valores da tupla nesse caso pq ja terminou a instrução anterior