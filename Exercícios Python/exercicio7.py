'''
Cálculo de média
@author Pedro Lucas Eleuterio Liberato data: 19/09/2023
versão 1.0
'''

print('#'*50)
print('Vamos fazer um cálculo de média')
quantidade = float(input('Quantas notas serão?'))
soma = 0
for i in range(1,quantidade + 1):
    nota = float(input('Qual é a nota {i}:')).replace(',','.')
    soma += 1
media = soma/i
print(f'A média é {media:2f}')