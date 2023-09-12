# Exercício Python 15: 
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado 
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia 
# e R$0,15 por Km rodado.

quantidade_de_dias_que_foi_alugado = int(input('Por quantos dias o carro foi alugado? '))
km_percorridos = float(input('Quantos Km foram percorridos com o carro? '))

VALOR_DIARIA = 60
VALOR_KM_RODADO = 0.15

preco_aluguel_do_carro_por_dia = VALOR_DIARIA * quantidade_de_dias_que_foi_alugado
preco_por_km_rodado = VALOR_KM_RODADO * km_percorridos

preco_final = preco_aluguel_do_carro_por_dia + preco_por_km_rodado

print('-' * 100)
print('Você ficou {} dias com o carro - valor da diaria é: R$ {:.2f}, totalizando R$ {:.2f}'
      .format(quantidade_de_dias_que_foi_alugado, VALOR_DIARIA, preco_aluguel_do_carro_por_dia))
print('Você pecorreu {}Km com o carro - valor por Km rodado é: R$ {:.2f}, totalizando R$ {:.2f}'
      .format(km_percorridos, VALOR_KM_RODADO, preco_por_km_rodado))
print('-' * 100)
print('TOTAL: R${:.2f}'.format(preco_final))
