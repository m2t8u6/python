import os

lista = []

while True:
    print('\nSelecione uma opção')
    resposta = input('[i]nserir [a]pagar [l]istar [s]air: ').lower()

    if resposta == 'i':
        os.system('clear')
        
        valor = input('Valor: ')

        lista.append(valor)
    
    lista_enumerada = enumerate(lista)

    if resposta == 'l':
        os.system('clear')

        for indice, valor_lista in lista_enumerada:
            print(indice, valor_lista)
    
    if resposta == 'a':
        os.system('clear')

        apagar = int(input('Escolha um indice para apagar: '))

        try:
            del lista[apagar]
        
        except (ValueError, IndexError):
            print('Indice invalido.')
    
    if resposta == 's':
        print('saindo...')
        os.system('clear')
        quit()