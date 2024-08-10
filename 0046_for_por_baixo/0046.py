nome = 'Luiz'
iterador = iter(nome)

while True:
    
    try:
        letra = next(iterador)
        print(letra)

    except StopIteration:
        break