#DESAFIO 003: Crie um programa que leia dois números e mostre a soma entre eles.
from colorama import init
init()
n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite um numero inteiro: '))
soma = n1 + n2
print('\033[33mA soma de {} + {} é igual a: {}\033[m'.format(n1,n2,soma))