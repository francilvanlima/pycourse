# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar
# o VALOR DA CASA, o SALARIO do comprador e em QUANTOS ANOS ele vai pagar.
#   Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
#   ou  então o emprestimo será negado.
from colorama import init
init()
valor = float(input('\nDigite o valor do imóvel: '))
sal = float(input('Digite o salário: '))
qtd = float(input('Digite a quantidade anos para pagar: '))
val_prest = valor / (qtd*12)
sal_porc = (sal * 30) / 100
if(val_prest < sal_porc):
    print('\033[36mO empréstimo foi realizado com sucesso!')
else:
    print('\033[30;47mEmpréstimo negado!')

