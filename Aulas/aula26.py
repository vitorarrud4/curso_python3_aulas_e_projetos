'''
Formatacao basica de strings
s   -   string
d   -   int
f   -   float
.<numero de digitos>f
x ou X - hexadecimal
(caractere)(><^)(quantidade)
>   -   esquerda
<   -   direita
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}.')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.3439821:+,.1f}')
print(f'O hexadecimal de 1500 e de {1500:08X}')