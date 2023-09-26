#int = Para variaveis numericas EX(5)
#input = Deixa vc criar um lugar para o usuário digitar
#float = Para variaveis numericas com casas decimais EX(1/2)
#str = Para variaveis com caracteres EX(abc)
#bool = Para variaveis que tem apenas dois possíveis valores: false e true
# // = trabalha apenas com o valor inteiro da divisão EX:

a = 15
b = 6
c = a//b
print(c)

d = 15
e = 7
f = d/e
print(f)

#Módulo = Sempre vai pegar o resto da divisão EX:
x = 5
y = 8
r = x % y
print(r)

#Expoenciação da divisão EX:

x = 6
y = 2
r = x ** y
print(r)

#Para importar a biblioteca math se deve usar o seguinte comando:
import math

#Tudo oque o usuário digita vem no tipo (str)

#Para mudar da , para o . usamos o .replace EX:
n1 = float(input("Digite um número decimal").replace(',','.'))
print(n1)

#Igualdade é mostrada no python como ==
#! significa diferente no python
#if = (pegou a moeda)
#else = (não pegou a moeda)

#Como saber quando a pessoa nasceu: Saber o dia/mes/ano atual e a idade do usuário.
#mesNascimento<mesAtual?

#while e for = estruturas de repetição
# while = quando não se tem um numero de vezes especifica
# for = possui um número determinado de contagens


numero = int(input('Olá! Digite um número: '))
for i in range(1,numero+1):
    print(i)

