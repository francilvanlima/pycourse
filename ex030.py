# crie um program que leia um numero inteiro e mostre na tela se ele é PAR ou IMPAR.
num = int(input('Digite um numero inteiro: '))
if(num % 2 == 0):
    print('\nO numero {} é PAR!\n'.format(num))
else:
    print('\nO numero {} é ÍMPAR!\n'.format(num))