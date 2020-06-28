# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.
r1 = int(input('\nDigite o comprimento da Reta1: '))
r2 = int(input('Digite o comprimento da Reta2: '))
r3 = int(input('Digite o comprimento da Reta3: '))
if((r1 + r2>r3) and (r2 + r3>r1) and (r1 + r3>r2)):
    print("\nÉ possível formar um triângulo!")
    if( r1 == r2 == r3):
        print('É um triângulo equilátero!')
    # elif():
else:
    print("\nIMPOSSÍVEL formar um triângulo!")
    #  Prezado prefeito Junior, boa tarde, quem vos!
    # 