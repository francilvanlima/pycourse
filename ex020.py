#O mesmo professor  do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle
aluno1 = input('Digite o nome do aluno1: ')
aluno2 = input('Digite o nome do aluno2: ')
aluno3 = input('Digite o nome do aluno3: ')
aluno4 = input('Digite o nome do aluno4: ')
nomes = [aluno1, aluno2, aluno3, aluno4]

# .sample(x, k=len(x)) ----- Esta função pega uma lista e embaralha os dados nela contido.
# ordem = random.sample(nomes, k=len(nomes))
shuffle(nomes)
print('\nOrdem de apresentação: {}'.format(nomes))

