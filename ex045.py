from random import randint
from colorama import init
from time import sleep
init()
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
# print('O PC escolheu: {}'.format(itens[pc])) # O computador escolhe a jogada dele
print('''Qual a sua opção:
[0] Pedra
[1] Papel
[2] Tesoura''')
gamer = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 15)
print('O PC jogou: {}'.format(itens[pc]))
print('O Gamer jogou: {}'.format(itens[gamer]))
print('-=' * 15)
if (pc == 0): #PC jogu Pedra
    if (gamer == 0):
        print("\n\033[33mEmpate!")
    elif(gamer == 1):
        print('\n\033[33mVocê ganhou!')
    elif(gamer == 2):
        print('\n\033[33mVc perdeu!')
    else:
        print('JOGADA INVÁLIDA!')
elif(pc == 1): #PC jogu Papel
    if (gamer == 0):
        print("\n\033[33mVocê perdeu!")
    elif(gamer == 1):
        print('\n\033[33mEmpatou!')
    elif(gamer == 2):
        print('\n\033[33mVocê ganhou!')
    else:
        print('JOGADA INVÁLIDA!')
elif(pc == 2): #PC jogou Tesoura
    if (gamer == 0):
        print("\n\033[33mVocê Ganhou!")
    elif(gamer == 1):
        print('\n\033[33mVocê perdeu!')
    elif(gamer == 2):
        print('\n\033[33mEmpatou!')
    else:
        print('JOGADA INVÁLIDA!')