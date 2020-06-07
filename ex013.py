#Faça um algoritmo que leia uma salário de um funcionário e mostre seu novo salário, com 15% de aumento.

sal = float(input('DIgite o salário: '))
aum = (sal*15)/100
salAtual = sal + aum
print('Salario sem aumento: R$ {}'.format(sal))
print('Salario com aumento: R$ {}\n'.format(salAtual)) 