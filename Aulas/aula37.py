'''
Repeticoes
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeira
Loop infinito -> Quando um codigo nao tem fim
>> CONTINUE = retorna para o comeco do laço <<
'''

contador = 0

while contador < 20:
    contador += 1


    '''if contador == 6:
        continue'''

    if contador >= 10 and contador <= 17:
        continue
        
    print(contador)
    '''if contador == 4:
        break'''