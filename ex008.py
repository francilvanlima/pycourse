#Desafio 008 - Escreva um programa que leia uma valor em metros e o exiba convertido em centímetros e milímetros.
metro = int(input('Quantos metros?  '))
c = metro * 100
m = metro * 1000

print('{}m em centimetro equivale a: {}cm\n{}m em milimetros equivale a: {}mm\n\n'.format(metro, c, metro, m))