# Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o ultimo nome separadamente.
# Ex: Ana Maria de Souza
# primeiro = Ana
# ultimo = Souza
n = str(input('Digite nome e sobrenome: ')).strip()
nome = n.split()
print('\nName and lastname = {} {}\n'.format(nome[0],nome[len(nome)-1]))
# print('ultimo nome = {}'.format(nome[len(nome)-1]))