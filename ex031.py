# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem cobrando R$ 0,50 por km
# para viagens até 200km e R$ 0,45 para viagens mais longas.
d = int(input('Qual a distância da viagem? '))
if(d <= 200):
    preco = d * 0.50
    print('Valor da passagem: R$ {:.2f}\n'.format(preco))
else:
    preco = d * 0.45
    print('Valor da passagem: R$ {:.2f}\n'.format(preco))