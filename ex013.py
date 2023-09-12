# Exercício Python 13: 
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salário =  float(input('Digite o salário do funcionario: R$ '))

aumento = salário * (15 / 100)

novo_salário = salário + aumento

print('Você ganhou um aumento de 15% no seu salário, seu novo salário é: R${:.2f}'.format(novo_salário))
