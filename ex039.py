# Escreva um programa que leia um ano de nascimento de um jovem e informe, de acordo com sua idade:
# -> Se ele ainda vai se alistar ao serviço militar;
# -> Se é hora de se alistar
# -> Se já passou do tempo de alistamento.
# Obs: Seu programa também deve mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime, date
from colorama import init
init() #inicia a biblioteca colorama
born = int(input('\nAno de nascimento: '))
hj = date.today()
idade = hj.year - born
if (idade < 18):
    print('\n\033[36mAinda irá se alistar, idade: {}anos, falta {} anos'.format(idade, 18 - idade))
elif(idade == 18):
    print('\n\033[36mHora de se alistar!'.format(idade))
else:
    print('\n\033[36mPassou do tempo de se alistar, idade: {} anos e passou {} anos do prazo de alistamento.'.format(idade, idade-18))



# print('Idade {}'.format(hj))
# print('\n\033[36mData americana: {}/{}/{}'.format(hj.day, hj.month, hj.year))
# print('\n\033[36mData Brasileira: {}'.format(data_texto))
# data_texto = hj.strftime('%d/%m/%Y')
