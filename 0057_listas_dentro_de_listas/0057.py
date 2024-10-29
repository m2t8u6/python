grupos = [
    ['Maria', 'Elena', ],
    ['Elaine', ],
    ['Luiz', 'João', 'Eduarda', ],
]

# Para acessar um valor de uma lista dentro de uma lista você primeiro diz o indice da lista  e depois o indice do valor na lista

for grupo in grupos:
    for pessoa in grupo:
        print(pessoa)