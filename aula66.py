while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')
    
    numero_validos = None
    num_1_float = 0
    num_2_float = 0
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numero_validos = True
    except:
        numero_validos = None
        
        
    if numero_validos is None:
        print('Digite um número válido.')
        continue

    operadores_permitidos = ['+', '-', '*', '/']
    
    if operador not in operadores_permitidos:
        print('Digite um operador válido.')
        continue
    
    if len(operador) > 1:
        print('Digite um operador válido.')
        continue
    
    print('Realizando sua conta. Configra o resultado abaixo:')
    
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Digite "sair" para sair: ').lower().startswith('s')
    print(sair)
    
    