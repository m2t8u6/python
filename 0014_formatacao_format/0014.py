# O primeiro modo de usar o format é colocando as variaveis na ordem de uso
a = 'AA'
b = 'BB'
x = 3.1415
variaveis_sem_sormatar = 'a = {} | b = {} | x = {:.2f}'
variaveis_formatadas = variaveis_sem_sormatar.format(a, b, x)
print(variaveis_formatadas)

# O segundo é nomeando as variaveis para elas serem usadas mais vezes
c = 'CCC'
d = 'DDD'
y = 3.141592

nv_variaveis_sem_formatar = 'c = {valc} | d = {vald} | y = {valy:.2f}'
nv_variaveis_formatadas = nv_variaveis_sem_formatar.format(valc = c, vald = d, valy = y)
print(nv_variaveis_formatadas)