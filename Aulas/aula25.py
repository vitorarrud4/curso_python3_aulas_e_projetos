'''
Interpolacao basica de strings
s   -   string
d e i - int
f   -   float
x e X - Hexadecimal (ABDEF0123456789)
'''

produto = 'Caneta azul'
preco = 3.500000
variavel = 'O produto %s tem o valor de R$%.2f' % (produto, preco)
print(variavel)
print('O hexadecimal de %d e %x' % (1500,1500)) 