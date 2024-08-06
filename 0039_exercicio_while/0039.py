nome = input('Digite o seu nome: ')
tamanho_nome = len(nome)
contador = 0
novo_nome = ""

while contador < tamanho_nome:
    
    novo_nome += nome[contador] + '*'

    contador += 1

print(f'Nome alterado: {novo_nome}')