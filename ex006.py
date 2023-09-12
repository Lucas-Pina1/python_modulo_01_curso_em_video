# Exercício Python 006: 
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input("Digite um numero: "))

dobro = numero * 2
triplo = numero * 3
raiz_quadrada = pow(numero, 1/2)

print("O dobro do numero {} é: {}\nO triplo do numero {} é : {}\nA Raiz quadrada do numero {} é: {:.2f}"
      .format(numero, dobro, numero,triplo, numero, raiz_quadrada))