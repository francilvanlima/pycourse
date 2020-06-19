# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual a base de conversão.
# 1 - Binario           2 - Octal       3 - hexadecimal
from colorama import init
init()
num = int(input('Digite um numero inteiro: '))
print('\033[33m1-Binario\n2-Octal\n3-Hexadecimal\033[m')
base = int(input('Qual a base de conversão: '))

if (base == 1):
    print('\033[36m{} em binario é: {}\033[m'.format(num, bin(num)[2:]))
elif (base == 2):
    print('\033[36m{} em Octal é: {}\033[m'.format(num, oct(num)[2:]))
elif (base == 3):
    print('\033[36m{} em hexadecimal é: {}\033[m'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida!')