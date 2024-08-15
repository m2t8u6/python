import os   

# list | list() | [] | Suporta varios valores de qualquer tipo | Tudo que esta separado por virgula é um item

# Lista com: str, int, float, bool, outra lista
lista = ['oliver', 23, 3.1415, True, []]

print(lista, type(lista))
print(f'{lista[0]} tem {lista[1]} anos.')

lista[1] = 22

print(f'Na verdade ele tem {lista[1]}')

os.system('clear')

# Create, Read, Updade, Delete -> CRUD
# Criar, ler, Alterar, Apagar

lista2 = [10, 20, 30, 40]

print(f'{lista2} contem {len(lista2)} elementos')

del lista2[2]

print(f'{lista2} contem {len(lista2)} elementos')

# É  recomendavel que você adicione ou remova itens em uma lista apenas no final

lista2.append(50)
lista2.append(60)
lista2.append(70)

print(f'{lista2} contem {len(lista2)} elementos')

lista2.append(80)

print(lista2)

# Remove o ultimo item da lista
valor_removido = lista2.pop()

print(f'{lista2} valor removido {valor_removido}')


lista2.clear()

print(lista2)

lista2 =  [20, 40, 60, 80]

lista2.insert(1, 25)

print(lista2)

lista.clear()
lista2.clear()

os.system('clear')

# Juntando listas

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b

print(lista_c)

lista_1 = ['a', 'b', 'c']
lista_2 = ['d', 'e', 'f']
lista_1.extend(lista_2)

print(lista_1)