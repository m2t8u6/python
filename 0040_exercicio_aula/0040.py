def sair():
    sair = input('Digite "s" para sair ou outro  valor  para  continuar: ')
    
    if sair.isdigit():
        print('ERRO')
        quit()
    
    sair = sair.lower().startswith('s')

    return sair

while True:

    operador = input('Qual vai ser o operador? ')
    x = input('Digite o primeiro número da operação: ')
    y = input('Digite o segundo número da operação: ')

    if x.isdigit and y.isdigit:
        x = int(x)
        y = int(y)
    else:
        print('ERRO')
        break

    match operador:
        case "+":
            print(f'{x} + {y} = {x + y}')
        case "-":
            print(f'{x} - {y} = {x - y}')
        case "*":
            print(f'{x} * {y} = {x * y}')
        case "/":
            print(f'{x} / {y} = {x / y}')
        case "%":
            print(f'{x} % {y} = {x % y}')
        case "**":
            print(f'{x} ** {y} = {x ** y}')

    if sair():
        break