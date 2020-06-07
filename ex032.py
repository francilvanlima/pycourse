# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('\nDigite o ano: '))
if((ano % 400 == 0) or (ano % 4 == 0) and (ano % 100 != 0)):
    print('\nAno {} é um ano Bisexto!\n'.format(ano))
else:
    print('\nAno {} Não é um ano Bisexto!\n'.format(ano))

# Obs: Ou seja, para um ano ser bisexto ele tem que ser divisível por 400 ou por 4 e não ser por 100