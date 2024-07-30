nome = input('Digite o seu nome: ')
qnt = len(nome)
idade = input('Digite a sua idade: ')

if nome == ' ':
    print('Digite um nome valido.')
    quit()
elif idade.isalpha():
    print('Você digitou uma letra ou caractere não númerico.')
    quit()
else:
    idade = int(idade)

print(f'\nSeu nome é: {nome}')
print(f'Seu nome invertido é: {nome[::-1]}\n')

if ' ' in nome:
    print('O nome contem espaço.')
else:
    print('O nome não tem espaço.')

print(f'\nSeu nome tem {qnt} caracteres.')
print(f'\nA primeira letra do seu nome é: {nome[0]}')
print(f'A ultima letra do seu nome é: {nome[-1]}')