'''
EXERCICIO: 
Faca uma lista de compras com listas. O usuario deve
ter a possibilidade de inserir, apagar e listar valores
da sua lista. Nao permita que o programa quebre com erros
de indices inexistentes na lista.
'''
import os

lista = []

while True:
    print('Selecione uma opcao:')
    opcao = input('[i]nserir, [a]pagar ou [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o indice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Nao foi possivel encontrar este indice!')
    elif opcao == 'l':
        os.system('cls')

        if(len(lista)) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)