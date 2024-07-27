x = input('Valor1 = ')
y = input('Valor2 = ')

if x > y:
    print(f'{x} é maior que {y}')
elif x < y:
    print(f'{y} é maior que {x}')
elif x == y or y == x:
    print(f'{x} é igual a {y}')
else:
    print('Opção invalida.')