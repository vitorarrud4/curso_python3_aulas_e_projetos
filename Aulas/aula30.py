'''
CONSTANTE = "Variaveis" que nao vao mudar
Muitas condicoes no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
'''

velocidade = 85    # velocidade atual do carro
local_carro = 99   # local em que o carro esta na estrada

RADAR_1 = 60    # Velocidade maxima do RADAR 1
LOCAL_1 = 100   # Local onde o RADAR 1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

velocidade_carro_passou_radar1 = velocidade > RADAR_1
carro_multado_radar1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)

if velocidade_carro_passou_radar1 and carro_multado_radar1:
    print('Multado chefia!')
else:
    print('Ta tranquilo!')

