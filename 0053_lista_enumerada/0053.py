lista = ['Marcio', 'Jorge', 'Maria']

lista_enumerada = enumerate(lista)

# for item in lista_enumerada:
#     indice, valor = item
#     print(f'O valor "{valor}" esta no indice "{indice}".')

for indice, valor in lista_enumerada:
    print(indice, valor)