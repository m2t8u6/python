num = input('Digite um número inteiro: ')

if num.isdigit() == False:
    print('Valor invalido.')
    quit()

num = int(num)
resultado = num % 2

if resultado == 0:
    print(f'O número {num} é par.')
else:
    print(f'O número {num} é impar.')