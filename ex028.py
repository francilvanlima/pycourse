# Escreva um programa que faça um computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuário tentar
# descobrir qual foi o numero escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
pc = randint(0, 5) #Faz o computador "PENSAR" em numero inteiro entre 0 e 5
print('pc: {}'.format(pc))
gamer = int(input('\nDigite o que PENSEI: '))
if(gamer == pc):
    print('\nPARABÉNS! Você ganhou!\n')
else:
    print('\nVocê PERDEU!\n')