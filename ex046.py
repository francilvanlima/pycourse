# Faça um programa que mostre na tela uma CONTAGEM REGRESSIVA, para o estou de fogos de artifícios
# indo de 10 até 0, com uma pausa de 1seg entre eles.
# from colorama import init
from time import sleep
# init()
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('Fim!')