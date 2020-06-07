# Faça um programa que leia um angulo qualquer e mostre o valor do Seno, Cosseno e Tangente de ângulo.
from math import sin, cos, tan

angulo = int(input('Valor do angulo: '))
print('-----------Seno de {}ºC é : {}'.format(angulo, sin(angulo)))
print('--------Cosseno de {}ºC é : {}'.format(angulo, cos(angulo)))
print('-------Tangente de {}ºC é : {}'.format(angulo, tan(angulo)))
