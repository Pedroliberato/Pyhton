'''
Faça um programa em que o usuário digite um numero inteiro
e o programa diga se o número é primo ou não.
@author Pedro Lucas Eleuterio Liberato data: 19/09/2023
versão 1.0
'''

print(' ＼（〇_ｏ）／ '*8)
print(f'\033[31m NÚMEROS PRIMOS \033[m')
contador = 0
numero = int(input('Olá! Digite um número: '))
if numero == 1:
    print(f'O número {numero} é primo')
elif numero == 2:
    print(f'O número {numero} é primo')
for i in range(1,numero+1):
    if(numero % i == 0):
        contador += 1
if(contador <= 2):
    print(f'O número {numero} é primo')
else:
    print(f'O número {numero} não é primo')