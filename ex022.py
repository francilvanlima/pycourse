# Crie um program que leia o nome completo de uma pessoa e mostre:
# - O nome com  todas letras Maiuculas;
# - O com todas minusculas;
# - Quantas letras ao todo (sem considerar espaços);
# - Quantas letras tem o primeiro nome.
nome = input('Digite seu nome: ').strip()
print('\nMaiusculo = ', nome.upper())
print('Minusculo = ', nome.lower())
n = nome.replace(' ','')
print('Qtd Caracteres = ', len(n))
print('Primeiro nome = ', nome.split(' ')[0])