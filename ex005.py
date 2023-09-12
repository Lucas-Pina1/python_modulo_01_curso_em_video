# Exercício Python 5: 
# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor 
# e seu antecessor.

numero = int(input('Digite um numero: '))

antecessor = numero - 1
sucessor = numero + 1

print('O antecessor de {} é {} e o sucessor é {}'.format(numero, antecessor, sucessor))
