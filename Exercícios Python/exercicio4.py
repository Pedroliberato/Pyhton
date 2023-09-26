from datetime import date

'''
Fazer um programa que pergunte ao usuário
a sua idade e descubra em que ano o usuário
nasceu, Usando if e else.
'''

diaAtual = date.today().day
mesAtual = date.today().month
anoAtual = date.today().year
diaNascimento = int(input('Que dia você nasceu? '))
mesNascimento = int(input('E em que mês você nasceu? '))
anoNascimento = int(input('Agora por ultimo, em que ano você nasceu? '))
print(f'{diaAtual}/{mesAtual}/{anoAtual}')
if (mesNascimento == mesAtual):
    print('Você ainda não fez aniversário 😢')
    idade = anoAtual - anoNascimento
    print(f'Minha idade é {idade} ano(s) de vida')
else:
    print('Já fez aniversário 🎉🎂')