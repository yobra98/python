#54:Desafio extra: faça um programa que tenha uma lista de frutas que vc gosta, criei uma copia dessa lista ,
#  usando fatiamento, em seguida adicione uma nova fruta a cada lista, faça um loop for, mostrando as frutas que
#  vc gosta, e outro para mostrar as frutas que seus amigos gostam.

minhas_frutas = ['banana','abacate','pera','melancia','morango']
frutas_filho = minhas_frutas[:]
minhas_frutas.append('mexirica')
frutas_filho.append('uva')

print('Minhas frutas preferidas: ')
for i in minhas_frutas:
    print(i)
print('\nFrutas preferidas do meu filho: ')
for i in frutas_filho:
    print(i)
