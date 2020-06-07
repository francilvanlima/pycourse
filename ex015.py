# ex015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0,15 por Km rodado.
from colorama import init
init()
km = float(input('\nDigite a quantidade de km percorrido: '))
dia = float(input('Digite a quantidade de dias: '))
valor = ((km*0.15) + (dia*60)) 
print('\n\033[36mValor a pagar: {}\033[m'.format(valor))