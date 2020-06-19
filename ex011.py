# Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua áera
# e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m quadrados.
from colorama import init
init()
alt = float(input('Digite a altura da parede: '))
lar = float(input('Digite a largura da parede: '))
area = (alt * lar)
tinta = area / 2

print('\nArea da parede: \033[33m{}m²\033[m e precisa de \033[33m{:.2f}l\033[m de tinta para pintá-la toda.\n'.format(area, tinta))

