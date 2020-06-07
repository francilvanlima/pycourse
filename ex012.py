#Façca um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto: '))
desc = (5 * preco) / 100
precoAtual = preco - desc

print('\nPreço original do produto: R$ {}'.format(preco))
print('Preço com desconto de 5%: {}\n'.format(precoAtual))