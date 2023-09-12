# Exercício Python 12: 
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preço_do_produto = float(input('Digite o preço do produto? R$ '))

desconto = preço_do_produto *  (5 / 100)

novo_preço = preço_do_produto - desconto

print('Hoje você ganhou 5% de desconto, o preço do produto ficou: R${:.2f}'.format(novo_preço))
