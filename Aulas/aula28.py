'''
EXERCICIO:
Peca ao usuario para digitar seu nome.
Se nome for digitado:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou nao) espacos
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba: "Voce deixou campos vazios."        
'''
nome = input('digite seu nome usuario: ')

if nome == 0:
    print('Voce deixou campos vazios')
else:
    print('O nome tem as seguintes caracteristicas: ')
    print(f'Seu nome é: {nome}')
    print(f'Seu nome invertido é: {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contem espacos!')
    else:
        print('Seu nome nao contem espacos!')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é: {nome[0]}')
    print(f'A ultima letra do seu nome é: {nome[-1]}')

