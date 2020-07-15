# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre sua categoria, de acordo com a idade:
# Até 9anos: MIRIM ---- Até 14anos: INFANTIL ---- Até 19anos: JUNIOR ----
# Até 20anos: SÊNIOR ---Acima: Master
from datetime import datetime, date
from colorama import init
init()
hj = date.today()
born = int(input('\nDigite o ano de nascimento: '))
idade = hj.year - born
if(idade <= 9):
    print('\033[36mNADADOR MIRIM!')
elif(idade > 9 and idade <= 14):
    print('\033[36mNADADOR INFANTIL!')
elif(idade > 14 and idade <= 19):
    print('\033[36mNADADOR JUNIOR!')
elif(idade == 20):
    print('\033[36mNADADOR SÊNIOR!')
else:
    print('\033[36mNadador MASTER!')


