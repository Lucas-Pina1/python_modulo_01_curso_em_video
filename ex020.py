# Exercício Python 20: 
# O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. 
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

aluno_01 = str(input('Digite o primeiro(a) aluno(a): '))
aluno_02 = str(input('Digite o segundo(a) aluno(a): '))
aluno_03 = str(input('Digite o terceiro(a) aluno(a): '))
aluno_04 = str(input('Digite o quarto(a) aluno(a): '))

lista = [aluno_01, aluno_02, aluno_03, aluno_04]

random.shuffle(lista)

print('A ordem de apresentação será: ')
print(lista)
