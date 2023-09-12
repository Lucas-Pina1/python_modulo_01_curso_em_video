# Exercício Python 10: 
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar

dinheiro_na_carteira = float(input('Quanto de dinheiro você term na carteira R$? '))

dolar = 4.93
real_para_dolar = dinheiro_na_carteira * dolar

print('Com R${:.2f} você pode comprar: US${:.2f}'.format(dinheiro_na_carteira, real_para_dolar))
