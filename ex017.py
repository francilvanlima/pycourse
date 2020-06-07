#Faça um progrma que leia o cateto oposto e  o cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
co = float(input('Digite o Cateto Oposto: '))
ca = float(input('Digite o cateto Adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa é igual a : {:.2f}\n'.format(hypot(hip)))


