'''
Introducao ao try/except 
try -> tentar executar o codigo
except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Dobro do numero q vc digitar: ')

try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_str} e igual a {numero_float * 2}')
except:
    print('Isso nao e um numero!')