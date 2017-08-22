## 3. Crie um script que contenha uma frase em uma variável sobre 
## aspas simples, e faça ocorrer o error de invalid syntax:
## faça a mesma coisa com aspas duplas, e depois explique por que o 
## error acontece.

frase = 'Isso é só mais 1 teste de string'
frase2 = "Isso é só mais 1 teste de string"
frase3 = "Isso é só mais" 1 "teste de string"   #erro na linha 8 de sintaxe inválida porque a variavel que contem a string só pode exibir
                                                #o conteúdo de uma variável entre um jogo de aspas, não mais que um
print(frase)
print(frase2)
print(frase3)