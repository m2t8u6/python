valor = input('[E]ntrar [S]air: ') or 0

if valor == 'E' or valor == 'e':
    print('Você esntrou.')
elif valor == 'S' or valor == 's':
    print('Saindo...')
else:
    print('Opção invalida.')