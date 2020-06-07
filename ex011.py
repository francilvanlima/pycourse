# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua áera
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.
alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = (alt * lar)
tinta = area / 2

print('\nArea da parede: {}m² e precisa de {:.3}l de tinta para pintá-la toda.\n'.format(area, tinta))

