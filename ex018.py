# Exercício Python 18: 
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Digite um Ângulo: '))
radianos = math.radians(angulo)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('O Ângulo de {} tem: '.format(angulo))
print("Seno: {:.2f}, cosseno: {:.2f}, tangente: {:.2f}".format(seno, cosseno, tangente))