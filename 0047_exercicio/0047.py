palavra = 'batman'
letras_adivinhadas = ''
tentativas = 0 

while True:
    letra = input('Digite uma letra: ').lower()

    # Verifica se foi digitada apenas uma letra:
    if len(letra) != 1:
        print('Digite apenas uma letra.')
        continue
    
    # Verifica se a letra  digitada esta na palavra secreta, se sim a letra digitada é concatenada em 'letras_adivinhadas'
    if letra in palavra:
        letras_adivinhadas += letra

    # Exibe a palavra com as letras adivinhadas ou '*' para as não adivinhadas
    palavra_exibida = ''.join([letra if letra in letras_adivinhadas else '*' for letra in palavra])
    print(palavra_exibida)

    tentativas += 1

    # Verifica se a palavra esta correta:
    if palavra_exibida == palavra:
        print(f'Parabéns! Você adivinhou a palavra "{palavra}" em {tentativas} tentativas.')
        break
