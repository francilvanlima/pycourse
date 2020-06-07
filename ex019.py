#Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo os nomes deles e escrevendo o nome do escolhido.
import random

aluno1 = input('\nDigite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')
nomes = [aluno1, aluno2, aluno3, aluno4]

# .sample(x, k=len(x))
sorteado = random.choice(nomes)
print('\nALuno sorteado foi: {}\n'.format(sorteado))