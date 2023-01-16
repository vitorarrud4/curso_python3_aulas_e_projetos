'''
Operadores in e not in
Strings sao iteraveis
0   1   2   3   4
v   i   t   o   r
5   4   3   2   1
'''
nome = 'Vitor'
# print(nome[2])
# print(nome[-4])
''''print('r' in nome) # retorna True ou False se o que esta incluso nas aspas
print('z' not in nome)
print('tor' in nome)
print('vic' in nome)'''

nome = input('digite seu nome: ')
encontrar = input('digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} esta em {nome}')
else:
    print(f'{encontrar} nao esta em {nome}')