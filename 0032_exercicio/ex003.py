nome = input('Qual é o seu nome? ')

tamanho = len(nome)

curto = tamanho <= 4
medio = tamanho = 5
longo = tamanho >= 6

if curto:
    print('Seu nome é curto.')
elif medio:
    print('Seu nome é normal.')
elif longo:
    print('Seu nome é longo.')
else:
    print('Valor invalido.')