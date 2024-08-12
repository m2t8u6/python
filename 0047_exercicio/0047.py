palavra = 'batman'
letras_adivinhadas = ''  # Armazena as letras corretas adivinhadas
tentativas = 0  # Contador de tentativas

while True:
    letra = input('Digite uma letra: ').lower()

    if len(letra) != 1:  # Verifica se o usuário digitou uma única letra
        print('Digite apenas uma letra.')
        continue

    if letra in palavra:
        letras_adivinhadas += letra  # Adiciona a letra correta às letras adivinhadas
    else:
        print('*')  # Exibe '*' para letras incorretas

    # Exibe a palavra com as letras adivinhadas ou '*' para as não adivinhadas
    palavra_exibida = ''.join([letra if letra in letras_adivinhadas else '*' for letra in palavra])
    print(palavra_exibida)

    tentativas += 1

    if palavra_exibida == palavra:  # Verifica se a palavra foi adivinhada completamente
        print(f'Parabéns! Você adivinhou a palavra "{palavra}" em {tentativas} tentativas.')
        break
