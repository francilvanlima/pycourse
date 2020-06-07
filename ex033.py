# Faça um programa que leia 3 numeros e mostre qual é o maior e qual é o menor.
n1 = int(input('\nDigite o numero 1: '))
n2 = int(input('Digite o numero 2: '))
n3 = int(input('Digite o numero 3: '))

# Verificando o menor!
menor = n1
if ((n2 < n1) and (n2 < n3)):
    menor = n2
if((n3 < n1) and (n3 < n2)):
    menor = n3

# Verificando o MAIOR!
maior = n1
if((n2 > n1) and (n2 > n3)):
    maior = n2
if((n3 > n1) and (n3 > n2)):
    maior = n3
print('Menor valor: {}'.format(menor))
print('Maior valor: {}'.format(maior))

    