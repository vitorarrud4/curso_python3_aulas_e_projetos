'''
Introducao a desempacotamento + tuplas
_ (unerline) =  pode ser usado para ser variavel que nao vai ser usada,
                nesse caso foi usado para o restante dos itens da lista.
'''

nome1, *_ = ['Vitor', 'Jorge', 'Roberta']
print(nome1, _)