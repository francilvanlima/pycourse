# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multra vai custar R$ 7,00 por cada km acima do limite.
v = int(input('\nDigite a velocidade  de um carro: '))
if(v > 80):
    multa = ((v - 80) * 7)
    print('\nVocê ultrapassou 80km/h e foi multado em: R$ {:.2f}\n'.format(multa))
else:
    print('\nSiga tranquilo! Velocidade perfeita!')