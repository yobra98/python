## 5. faça a soma de 2 números, e multplique ele por um número do 
## seu gosto, ex: 2+3*5 em seguida faça o mesmo e use () para a 
## adição ex: (2+3)*5 o resultado de ambos vão ser diferentes 
## explique pq isso acontece .

n1 = 35
n2 = 38
m = 3

soma = (n1 + n2) * m    #na primeira função, o cálculo prioriza a soma(entre parenteses) e então seu resultado é multiplicado
soma1 = n1 + n2 * m     #nessa função o calculo prioriza a multiplicação dos fatores, que por regra matemática prevalece sobre a soma

print(soma, soma1)      #exibição dos resultados diferentes em cada variável

