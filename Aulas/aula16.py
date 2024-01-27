# introducao aos blocos de codigo + if / elif  / else

# if / elif         / else
# se / se nao se    / se nao

# def e uma funcao
def sistema(entrada):
    
    if entrada == 'entrar':
        print('Voce entrou no sistema!')
    elif entrada == 'sair':
        print('Voce saiu do sistema')
    else:
        print('Nenhuma das opcoes...')
        chamando_sistema = sistema(entrada = input("Voce quer 'entrar' ou 'sair'? "))

chamando_sistema = sistema(entrada = input("Voce quer 'entrar' ou 'sair'? "))