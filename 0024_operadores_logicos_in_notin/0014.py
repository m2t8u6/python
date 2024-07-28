# nome  = 'Thor'
# print('h' in nome)
# print('or' not in nome)

nome1 = 'Marcos'
nome2 = 'Otavio'
nome3 = 'Jorge'

encontrar = input('Qual nome vocẽ deseja  encontrar? ')

if (encontrar in nome1) or (encontrar in nome2) or (encontrar in nome3):
    print('Nome encontrado.')
else:
    print('Nome não enncontrado.')