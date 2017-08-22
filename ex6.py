## 6 Crie um script que tenha a idade de uma pessoa em uma
## variável,depois faça a concatenação da idade com duas "strings"
## adicionando o valor de ambos a outra nova variável, ex: nova
## ="parabéns"+idade+"anos" vai ocorrer um error, então tente
## resolver e explique pq isso acontece.

idade = 25
mensagem = 'parabéns'
mensagem2 = 'anos'
nova = mensagem + " " + str(idade) + " " + mensagem2

print(nova)

## da forma como o exercicio pede acontece o erro porque variáveis de tipo diferentes precisam ser exibidas de forma diferente também,
## por exemplo, a idade que é um número não pode ser exibida junto com string, a menos que ela seja uma string também ou seja tratada de
## forma diferente para a exibição