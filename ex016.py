#Faça um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porçao inteira.
# ex: Digite um numero: 6.127      O numero 6.127 tem a porção inteira 6.
from math import trunc
num = float(input('Digite um numero ral: '))
porcao = trunc(num)
print('A porção inteira de {} é iguala : {}\n'.format(num, porcao))