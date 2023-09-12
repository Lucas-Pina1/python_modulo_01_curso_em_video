# Exercício Python 9:  
# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input('Digite o numero que quer saber a tabuada: '))

print()
print('A tabuada do numero {} é: '.format(numero))
print('-' * 12)
print('{} * 1 = {:2}'.format(numero, numero * 1))
print('{} * 2 = {:2}'.format(numero, numero * 2))
print('{} * 3 = {:2}'.format(numero, numero * 3))
print('{} * 4 = {:2}'.format(numero, numero * 4))
print('{} * 5 = {:2}'.format(numero, numero * 5))
print('{} * 6 = {:2}'.format(numero, numero * 6))
print('{} * 7 = {:2}'.format(numero, numero * 7))
print('{} * 8 = {:2}'.format(numero, numero * 8))
print('{} * 9 = {:2}'.format(numero, numero * 9))
print('{} * 10 = {:2}'.format(numero, numero * 10))
print('-' * 12)

