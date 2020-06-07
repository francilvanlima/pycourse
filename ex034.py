# Faça um programa que leia o salário de um funcionário e calcule o valor de seu aumento.
# Para salários acima de R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('\nDigite o salário: '))
if( sal > 1250):
    aum = sal + ((sal * 10) / 100)
    print('O Salário ajustado com 10%: {:.2f} '.format(aum))
else:
    aum = sal + ((sal*15)/100)
    print('O Salário ajustado com 15%: {:.2f} \n'.format(aum))