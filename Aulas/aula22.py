# Operador logico OR

'''
Operadores logicos
and (e) or (ou) not (nao)
and - Todas as condicoes precisam ser 
verdadeiras.
Se qualquer valor for considerado falso,
a expressao inteira sera avaliada naquele valor
Sao considerados falsy (que ja foi mostrado)
0 0.0 '' False
Tambem existe o tipo None que e
usado para representar um nao valor
'''

'''entrada = input('[E]ntrar ou [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha_permitida):
    print('Entrou')
else:
    print('Saiu')'''

# Avaliacao de curto circuito:
senha = input('Senha: ') or 'Sem senha'
print(senha)
