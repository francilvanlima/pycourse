# Faça um programa que calcule a soma entre todos os numeros ímpares que são multiplos de 3
# e que se encontram no intervalo de 1 até 500.
s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s += c
        cont = cont+1
        # print(c, end=' ')
print('\nQtd de multiplos de 3: {}'.format(cont))
print('\nSoma: {}'.format(s))
