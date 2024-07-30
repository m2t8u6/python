# try = tenta executar o codigo
# except = ocorreu algun erro ao tentar executar

x = input('Digite um número eu vou dobrar ele: ')

try:
    x = float(x)
    print(f'O dobro do número {x} é {x * 2}')
except:
    print(f'Valor invalido.')

...