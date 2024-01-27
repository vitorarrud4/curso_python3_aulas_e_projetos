# formatação de strings = f-strings
nome = 'vitor'
altura = 1.82
valor = 54000.4801

# e uma f string abaixo, se tirar o f da string retorna uma string sem atribuir os resultados de fato as variveis

linha_1 = f'O meliante {nome} tem {altura} de altura e recebe o valor de {valor:,.2f}'

print(linha_1)