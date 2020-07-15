# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu PREÇO NORMAL e CONDIÇÃO DE PAGAMENTO.
# - À vista dinheiro/cheque: 10% de desconto;
# - Á vista no CARTÃO: 5% de desconto;
# - Em até 2x no cartão: Preço normal;
# - 3x ou mais no cartão: 20% de juros;
from colorama import init
init()
valor = float(input('Valor do produto: '))
print('[ 1 ] - Á vista dinheiro/cheque.\n[ 2 ] - Á vista no cartão.\n[ 3 ] - 2x no cartão.\n[ 4 ] - 3x ou mais no cartão.')
cond = int(input('Condição de Pagamento: '))
if (cond == 1):
    prod = valor - ((valor * 10)/100)
    print('\n033[33mValor do produto: R$ {:.2f}'.format(prod)) 
elif (cond == 2):
    prod = valor - ((valor * 5)/100)
    print('\n033[33mValor do produto: R$ {:.2f}'.format(prod)) 
elif (cond == 3):
    print('\n\033[33mValor do produto: R$ {:.2f}'.format(valor))
    print('\033[33mValor das parcelas: 2 x R$ {:.2f}'.format(valor/2))
elif (cond == 4):
    prod = valor + ((valor * 20)/100)
    print('\n\033[33mVALOR DO PRODUTO: R$ {:.2f}'.format(prod))
    parc = int(input('Quantida de parcela: '))
    valor_parc = prod / parc
    print('Valor das parcelas: {} x R$ {:.2f}'.format(parc, valor_parc))
     

