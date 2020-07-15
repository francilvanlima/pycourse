# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida: Abaixo de 5.0 'REPROVADO' --- Entre 5 e 6.9 "RECUPERAÇÃO" --- >7 'APROVADO'
from colorama import init
init()
n1 = float(input('\nDigite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
media = (n1 + n2) / 2
if(media < 5):
    print('\033[36mREPROVADO!')
elif(media >= 5 and media < 7):
    print('\033[36mESTÁ DE RECUPERAÇÃO!')
else:
    print('Aprovado! Boas férias!')
