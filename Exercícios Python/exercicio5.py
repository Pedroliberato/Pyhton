'''
Crie um programa em que o usuário digite um número
e o programa diga se aquele numero é par ou impar.
@author Pedro Lucas Eleuterio Liberato data: 19/09/2023
versão 1.0
'''

print('-'*45)
print('Vamos ver se os números são pares ou impares')
numero = int(input('Digite um número: '))
resto = numero % 2
if resto == 0:
    print(f'\033[31m O número é par \033[m')
else:
    print(f'\033[35m O número é impar \033[m')