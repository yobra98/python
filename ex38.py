##38:Desafio extra: Crie um script que tenha uma lista com pelo menos 3 animais, use o loop for com uma declaração para eles ,
#  no final do programa faça uma msg declarando oque esses animais tem em comum .

animais = ['macaco', 'cachorro', 'gato', 'coelho','raposa', 'bicho-preguiça']

print('Lista de animais:\n')
i = 1

for animal in animais:
    print(i, animal)
    i += 1

print('\nO que estes animais têm em comum: presença de pêlos')