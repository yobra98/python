## 21:Desafio extra:  faça um programa que tenha 3 pessoas em uma mesa.
## Elas vão estar em sua lista, então a ultima pessoa da lista não pagou a conta.
## Vc vai fazer uma mensagem que fale que  ela não pagou a conta , então  fale que vai expulsar ela.
## Em seguida vc vai substituir a pessoa que não pagou , e vai adicionar outra pessoa a mesa .
## Depois faça uma mensagem ao qual , pergunte a ela, se ela quer se juntar a mesa .
## E ela vai responder que sim .
## Depois , faça uma mensagem que envolva mais 1 pessoa da sua lista .
## Faça que seu programa fique bem intuitivo e com funções que  foram estudadas ate agora .

mesa = ['patricia', 'pamela', 'gisele']

print(mesa)
print(mesa.pop() + ' caloteira não pagou a conta!, sai fora da mesa!')

mesa.append('camila')

print(mesa[-1] + ' venha se juntar à nossa mesa!')
print(mesa)


