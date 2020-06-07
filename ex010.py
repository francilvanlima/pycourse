#Crie um programa que leia quanto dinheiro dinheiro a pessoas tenha na carteira e mostre quantos dólares ela pode comprar.
num = float(input('Quanto tem na carteira: '))
# dolar atual = 5.32
dolar = num * 5.32

print('Com R${:.3} pode ser comprado: ${:.3} dólares!'.format(num, dolar))