frase = 'aaaoooooobxxx'.lower()

i = 0
quandidade_letra = 0
letra = ' '

while i < len(frase):

    if quandidade_letra < frase.count(frase[i]):
        letra = frase[i]
        quandidade_letra = frase.count(letra)

    i += 1

print(f'A letra com mais quandidade é letra "{letra}" e sua quandidade no texto é de: {quandidade_letra}')