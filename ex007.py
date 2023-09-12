# Exercício Python 7: 
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Digite a primeira nota do aluno: '))
nota_2 = float(input('Digte a segunda nota do aluno: ')) 

media = (nota_1 + nota_2) / 2

print('O aluno teve a primeira nota: {:.1f}\n A segunda nota foi: {:.1f}\n Sua média foi de: {:1f}'
      .format(nota_1, nota_2, media))