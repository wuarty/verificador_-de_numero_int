velocidade = 61
km_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

velocidade_carro_passou_radar1 = velocidade > RADAR_1
passou_radar_1 = km_carro >= (LOCAL_1 - RADAR_RANGE) and km_carro <= (LOCAL_1 + RADAR_RANGE)
carro_passou = passou_radar_1 and velocidade_carro_passou_radar1

if velocidade_carro_passou_radar1:
    print('Velocidade do carro passou do radar 1')

if carro_passou:
    print('Carro passou radar 1')

if passou_radar_1:
    print('Carro multado no Radar 1')
