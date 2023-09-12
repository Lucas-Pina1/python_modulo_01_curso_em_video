# Exercício Python 11: 
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura_parede = float(input('Digite a largura em metros da parede: '))
altura_parede = float(input('Digite a altura em metros da parede: '))

area_da_parede = largura_parede * altura_parede

um_litro_de_tinta_pinta_em_metros = 2

litros_para_pintar_a_parede = area_da_parede / 2

print('A área da parede é de : {:.2f}m² e será nescessário {:.2f} litros de tinta para pintar a parede'.format(area_da_parede, litros_para_pintar_a_parede)) 