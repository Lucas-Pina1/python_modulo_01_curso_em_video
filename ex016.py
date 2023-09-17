# Exercício Python 16: 
# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira, usando modulos.

from math import trunc

numero_real = float(input('Digite um numero real: '))

parte_inteira_do_numero = trunc(numero_real)

print('A parte inteira de {} é: {}'.format(numero_real, parte_inteira_do_numero))