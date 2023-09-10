# Exercício Python 4:

# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele.

informacao = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(informacao))
print('Só tem espaços? ', informacao.isspace())
print('Só tem espaços? ', informacao.isnumeric())
print('É alfabético? ', informacao.isalpha())
print('É alfanumérico? ', informacao.isalnum())
print('Está em maiúsculas? ', informacao.isupper())
print('Está em minúsculas? ', informacao.islower())
print('Está capitalizada? ', informacao.istitle())
