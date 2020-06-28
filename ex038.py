# Escreva um program que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
# O 1º valor é maior!
# O 2º valor é maior!
# Os valores são iguais!
from colorama import init
init()
n1 = int(input('\nDigite 1º numero: '))
n2 = int(input('Digite 2º numero: '))
if(n1 > n2):
    print('\033[36mO 1º valor é maior: {}\033[m'.format(n1))
elif(n1 == n2):
    print('\033[36mOs valores são iguais!: {} == {}\033[m'.format(n1,n2))
else:
    print('\033[36mO 2º valor maior é: {}\033[m\n\n'.format(n2))

