'''
1) Data de nascimento criar um programa que pergunte
ao usuário seu nome e a data de seu nascimento e
calcule a idade com base no ano atual.

2) Crie um programa em que o usuário digite os valores
e o programa calcule a base de um triângulo retângulo.

3) Crie um programa que o usuário digite o peso e a altura
e o programa calcule o IMC(índice de massa corporal).

4) Crie um programa em que o usuário digite um número em
graus C°(célsius) e o programa converta em farenheit.

5) Faça o mesmo para farenheit em Célsius

6) Crie um programa que calcule báskara dos valores digitados
regras e tem que ser sempre elevado ao quadrado x² mas pode
ter qualquer valor ax² + ou - bx + ou - c = 0
'''


nome = input('Olá, qual é o seu nome? ')
idade = int(input(f'E qual é a sua idade {nome}? '))
data = 2023 - idade
print(f' Você nasceu em {data}')



print('Vamos ver a base de um triângulo retângulo')
cateto1 = float(input('Digite um número: '))
cateto2 = float(input('Mais um: '))
hipotenusa = cateto1 + cateto2
print(f'A hipotenusa do seu triangulo retangulo é {hipotenusa}')
base = cateto1 * cateto2
print(f'E a base do seu triângulo retângulo é {base}')



print('Vamos ver o seu IMC')
massa = float(input('Qual é o seu peso?'))
altura = float(input('E a sua altura?'))
estatura = altura ** 2
massaCorporal = massa // estatura
print(f'O seu IMC é {massaCorporal}')



print('Devemos mudar a temperatura de graus Célsius para farenheit')
celsius = float(input('Digite a temperatura em C°'))
farenheit = float((celsius * 1.8) + 32)
print(f'A temperatura em Farenheit é {farenheit}')



print('Agora vamos fazer ao contrário')
farenheit = float(input('Digite a temperatura em Farenheit '))
celsius = float((farenheit - 32) // 1.8)
print(f'Em celsius a temperatura é {celsius}')



print('Vamos calcular Báskara')
a = int(input('Escolha o valor de A: '))
b = int(input('Agora o valor de B: '))
c = int(input('E por ultimo o valor de C: '))
delta = pow(b,2) - 4 * a * c
print(f'O valor do Delta é: {delta}')