'''
Iterando strings com while
Exercicio: resultado quer que o nome fique *V*i*t*o*r
'''

nome = 'Vitor'
tamanho_nome = len(nome)
contador = 0
novo_nome = ''

while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1

novo_nome += '*'
print(novo_nome)