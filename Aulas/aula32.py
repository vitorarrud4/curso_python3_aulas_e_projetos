'''
Faca um programa que peca ao usuario para digitar um numero inteiro,
informe se este numero e par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao e um numero inteiro
'''
"""print('PROGRAMA 1 - par ou impar?')
numero_str = input('Entre com um numero inteiro: ')

try:
    numero_inteiro = int(numero_str)
    if (numero_inteiro % 2 == 0):
        print(f'O numero {numero_inteiro} e par!')
    else:
        print(f'O numero {numero_inteiro} e impar!')
except:
    print('O numero informado nao e inteiro!!!')
"""



'''
Faca um programa que pergunte a hora ao usuario e, baseando-se no horario
descrito, exiba a saudacao apropriada. Ex.:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''
"""print('PROGRAMA 2 - Horas')
horario = input('Entre com o horario atual humano em numeros inteiros: ')
horario_inteiro = int(horario)


horario_dia = horario_inteiro >= 0 and horario_inteiro <= 11
horario_tarde = horario_inteiro >= 12 and horario_inteiro <= 17
horario_noite = horario_inteiro >= 18 and horario_inteiro <= 23

if horario_dia:
    print('Bom dia usuario!')
elif horario_tarde:
    print('Boa tarde usuario!')
elif horario_noite:
    print('Boa noite usuario!')
else:
    print('Horario invalido usuario!!!')"""



'''
Faca um programa que peca o primeiro nome do usuario. Se o nome tiver
4 letras ou menos escreva "Seu nome e curto"; maior que 6 escreva
"Seu nome e muito grande".
'''

"""print('PROGRAMA 3 - Contagem de letras no nome')
nome = input('Entre com teu nome caro usuario: ')

contador_nome = len(nome)

contador_nome1 = contador_nome <= 4
contador_nome2 = (contador_nome == 5 or contador_nome == 6)
contador_nome3 = contador_nome > 6

if contador_nome1:
    print('Seu nome e curto.')
elif contador_nome2:
    print('Seu nome e normal.')
elif contador_nome3: 
    print('Seu nome e muito grande.')"""