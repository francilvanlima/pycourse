# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
# Escaleno: All different sides;
# Isóscele: Two sides equal and one different;
# Equilátero: All sides equal;
from colorama import init
init()
r1 = int(input('\nDigite o comprimento da Reta1: '))
r2 = int(input('Digite o comprimento da Reta2: '))
r3 = int(input('Digite o comprimento da Reta3: '))
if((r1 + r2>r3) and (r2 + r3>r1) and (r1 + r3>r2)):
    print("\n\033[34mÉ possível formar um triângulo!")
    
    if(r1 != r2 != r3 and r1!=r3):
        print('\033[33mÉ um triângulo Escaleno!')
    elif((r1 == r2 != r3) or (r2 == r3 != r1) or (r3 == r1 != r2)):
        print('\033[33mÉ um triângulo Isósceles!')
    elif(r1 == r2 == r3):
        print('\033[33mÉ um triângulo Equilátero!')
else:
    print("\n\033[31mIMPOSSÍVEL formar um triângulo!")
    #  Prezado prefeito Junior, boa tarde, quem vos!
    # 