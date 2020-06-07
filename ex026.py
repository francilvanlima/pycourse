# Faça um programa que leia uma frase pelo teclado e mostre:
#  - Quantas vezes aparece a letra 'A';
#  - Em que posição ela aparece a primeira vez;
#  - Em que posição ela aparece pela ultima vez;
frase = str(input('Digite a Frase: ')).upper().strip()
print('\nA letra A aparece {} vezes'.format(frase.count('A')))
print('Primeira vez o A aparece na posição: [{}]'.format(frase.find('A')+1))
print('Ultima vez o A aparece na posição: [{}]'.format(frase.rfind('A')+1))