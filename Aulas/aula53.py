'''
enumerate = enumera iteraveis
'''
import os
os.system('cls') # serve para dar um cls (limpar) o prompt de comando

lista = ['Vitor', 'Jorge', 'Amanda', 'Roberta']

for indice, nome in enumerate(lista):
    print(indice, nome)