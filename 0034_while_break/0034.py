condicao = True
nome = ...

while condicao:
    nome = input('Qual é o seu nome? ')
    
    if nome == 'sair':
        break

    print(f'Olá, {nome}')

print('Resto do coodigo...')