contador = 0

while contador <= 100:
    
    contador += 1

    if contador == 6:
        print('Não mostre.')
        continue

    if contador >= 48 and contador <= 80:
        print('Não mostre.')
        continue

    if contador ==  95:
        break;

    print(f'{contador = }')
    

print('Acabou.')