'''
Listas em Python
Tiop list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - indices e fatiamento
Metodos uteis: 
    append, insert, pop, del, clear, extend, *
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
'''

#        +01234
#        -54321
string = 'ABCDE' # 5 caracteres

lista = [123, True, 'Vitor', 1.2, []]
#lista[-3] = 'Arruda'
#del lista[1]
#print(lista)
#print(lista[1], type(lista[2]))

lista.append(50)
ultimo_valor_removido = lista.pop()
print('Lista :',lista,'\nUltimo valor removido: ', ultimo_valor_removido)