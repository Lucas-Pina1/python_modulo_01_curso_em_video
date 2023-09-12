# Exercício Python 8: 
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

valor_em_metros = float(input('Digite um valor em metros: '))

valor_em_centímetros = valor_em_metros * 100
valor_em_milímetros = valor_em_metros * 1000

print('{} m em centímetros é: {:.0f} cm.\n{} m em milímetros é: {:.0f} mm'
      .format(valor_em_metros, valor_em_centímetros, valor_em_metros, valor_em_milímetros))