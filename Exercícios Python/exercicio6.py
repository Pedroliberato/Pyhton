'''
Faça um jogo JO - KEN - PO em que o usuario escolha entre pedra, papel ou tesoura
e o computador também atráves de um número aleatorio entre 1, 2 e 3.
@author Pedro Lucas Eleuterio Liberato data: 19/09/2023
versão 1.0
'''

from random import randint
from time import sleep
print('#'*50)
print('Bem vindo(a) ao jogo de JO - KEN - PO 👊 🤚 ✌')
sleep(1)
print(' JO-👊')
sleep(1)
print('KEN-🤚')
sleep(1)
print('PO-✌')
sleep(1)

escolhaPlayer = int(input('''
Digite [1] - 👊 - Pedra
Digite [2] - 🤚 - Papel
Digite [3] - ✌ - Tesoura
Faça a escolha: '''))
print(f'Sua escolha foi: {escolhaPlayer}')
if (escolhaPlayer == 1):
    print(f'A sua escolha foi 👊')
elif(escolhaPlayer == 2):
     print(f'A sua escolha foi 🤚')
elif(escolhaPlayer == 3):
     print(f'A sua escolha foi ✌')
else:
    print('Digite uma opção entre 1 e 3 e reinicie o jogo')
#escolha do computador
escolhaComputador = randint(1,3)
if (escolhaComputador == 1):
    print(f'O Computador escolheu 👊')
elif(escolhaComputador == 2):
     print(f'O Computador escolheu 🤚')
else:
     print(f'O Computador escolheu ✌')
if(escolhaPlayer == escolhaComputador):
    print(f'Temos um empate')

# Pedra ganha de tesoura então 1 ganha de 3
# Papel ganha de pedra então 2 ganha de 1
# Tesoura ganha de papel então 3 ganha de 2

elif((escolhaPlayer == 1 and escolhaComputador == 3) or
     (escolhaPlayer == 2 and escolhaComputador == 1) or
     (escolhaPlayer == 3 and escolhaComputador == 2)):
    print('Você ganhou, UAU')
else:
    print('Você perdeu, que pena')