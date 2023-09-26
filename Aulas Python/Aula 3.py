'''
Condicionais é importante para se fazer
comparações entre variáveis ou valores
boolenos, numéricos eu de palavras.
Para realizar esses elementos é importante
utilizar a condição ""if" seguida de um senão,
else ou nada.
'''


moeda = True
ponto = 0
nome = str(input('Nome do personagem:\n'))
if((nome == 'Mario' and moeda == True)or(nome == 'mario' and moeda == True)):
    ponto = ponto + 1
    print(f'{nome} pegou a moeda e teve {ponto} ponto')
    moeda = str(input('Deseja pegar mais moedas?\n'))
    if(moeda == 'sim'):
        ponto = ponto + 1
        print(f'{nome} pegou a moeda e teve {ponto} pontos')
    else:
        print(f'{nome} não quis pegar mais moedas')
else:
    print(f'{nome} não pegou a moeda')