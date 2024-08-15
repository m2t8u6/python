# list | list() | [] | Suporta varios valores de qualquer tipo | Tudo que esta separado por virgula é um item

# Lista com: str, int, float, bool, outra lista
lista = ['oliver', 23, 3.1415, True, []]

print(lista, type(lista))
print(f'{lista[0]} tem {lista[1]} anos.')

lista[1] = 22

print(f'Na verdade ele tem {lista[1]}')