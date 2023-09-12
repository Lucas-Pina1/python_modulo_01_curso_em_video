# Exercício Python 14: 
# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_em_graus_celsius = float(input('Digite uma temperatura em graus Celsius: '))

temperatura_convertida_em_fahrenheit = temperatura_em_graus_celsius * 1.8 + 32

print('A temperatura {}°C em Fahrenheit é {}°F'
      .format(temperatura_em_graus_celsius, temperatura_convertida_em_fahrenheit))
