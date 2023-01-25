# Calculadora com while

while True:
    num1 = input('digite um numero: ')
    num2 = input('digite outro numero: ')
    operador = input('digite o operador: (+ - / *)')

    resultado = 0
    numeros_validos = None
    num1_float = 0
    num2_float = 0

    try:
        num1_float = float(num1)
        num2_float = float(num2)
        numeros_validos = True
    except: 
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos!')
        continue

    if len(operador) > 1:
        print('Operador inválido!')
        continue

    if operador == '+':
        resultado = num1_float + num2_float
    elif operador == '-':
        resultado = num1_float - num2_float
    elif operador == '/':
        resultado = num1_float/num2_float
    elif operador == '*':
        resultado = num1_float*num2_float
    else:
        print('entre com um operador valido!')
        continue
    
    print(f'{num1_float} {operador} {num2_float} = {resultado:.2f}')

    # botao sair
    sair = input('Quer sair? [s] ou [n]').lower().startswith('s')
    
    if sair is True:
        break
    