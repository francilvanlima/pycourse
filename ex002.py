from colorama import init
init()
nome = input('Digite seu nome: ')
print ('\033[32mBem vindo ao curso de python\033[32m, \033[35m{}!\033[m'.format(nome))
