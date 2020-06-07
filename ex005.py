#Faça um programa que leia um numero inteiro e mostre na tela seu sucessor e seu antecessor.
num = int(input('Digite um numero: '))

ant = num - 1
suc = num + 1

print ('O Antecessor de {} é: {}\nO Sucessor de {} é: {}\n\n'.format(num, ant, num, suc))