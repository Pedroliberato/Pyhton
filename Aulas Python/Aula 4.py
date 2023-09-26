engrenagemLogica = 1
print('Apresentando o \033[31mLaço While\033[m')
while(engrenagemLogica <= 10):
    print(engrenagemLogica)
    engrenagemLogica = engrenagemLogica + 1
print('E agora o \033[31mLaço For\033[m')
for contador in range(0,10):
    print(contador, end='')



soma = 0
for i in range (0,4):
    nota = float(input('Digite a nota: '))
    soma += nota
print(f'A soma de tudo é {soma}')
