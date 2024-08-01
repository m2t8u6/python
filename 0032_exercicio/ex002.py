horario = input('Qual é o horario atual? ')

if horario.isdigit():
    horario = int(horario)
else:
    print('Valor inválido.')

inicio_manha = 0
fim_manha = 11

inicio_tarde = 12
fim_tarde = 17

inicio_noite = 18
fim_noite = 23

manha = (horario >= inicio_manha) and (horario <= fim_manha) 
tarde = (horario >= inicio_tarde) and (horario <= fim_tarde)
noite = (horario >= inicio_noite) and (horario <= fim_noite)

if manha:
    print('Bom dia!')
elif tarde:
    print('Boa tarde!')
elif noite:
    print('Boa noite!')
else:
    print('Valor inválido.')