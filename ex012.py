#Façca um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
from colorama import init
init()
preco = float(input('Digite o preço do produto: '))
desc = (5 * preco) / 100
precoAtual = preco - desc

print('\n\033[36mPreço original do produto:\033[m \033[33mR$ {}\033[m'.format(preco))
print('\033[36mPreço com desconto de 5%:\033[m \033[33mR$ {}\033[m\n'.format(precoAtual))