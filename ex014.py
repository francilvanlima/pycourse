# ex014: Escreva um programa que converta um a temperatura digitada em ºC e converta para ºF
from colorama import init
init()
c = int(input('Digite o valor de Grau Celsius: '))
f = ((c * 1.8) + 32)
print('\n\033[36m{}ºC\033[m em Fahrenheit é: \033[35m{:.2f}\033[m'.format(c,f))
