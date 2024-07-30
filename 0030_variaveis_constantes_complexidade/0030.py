# Em python o conceito de constante (uma variavel que oo valor não pode ser alterado em nehum momento) não existe mas quando uma variavel  esta com o nome em maiusculo é sinal de que o seu valor não deve ser mudado.

# Definindo as variaveis de localização e velocidade do carro
v_carro = 61
numero_local = 90

# Configuração do radar
RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_acima_radar = v_carro > RADAR_1
carro_passou_radar1_depois = numero_local >= (LOCAL_1 - RADAR_RANGE) 
carro_passou_radar1_antes =  numero_local <= (LOCAL_1 + RADAR_RANGE)

if velocidade_acima_radar:
    print('O carro esta acima do limite de velocidade.')

if carro_passou_radar1_depois and carro_passou_radar1_antes and velocidade_acima_radar:
    print('O carro foi multado.')