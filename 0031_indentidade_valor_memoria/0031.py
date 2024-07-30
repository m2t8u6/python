# id | todas as variaveis possuem | para descobrir o id use: id(variavel)
a = 'ola'
print(f'{a=} {id(a)}')
b = 'ola'
print(f'{b=} {id(b)}')

if id(a) == id(b):
    print('Os valores são iguais entção o python coloca os mesmos id para gastar menos memoria.')

# None = não valor
condicao = False
passou_no_if = None

if condicao:
    print('A condição é verdadeira.')
    passou_no_if = True
else:
    print('A condição é False.')

print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)