#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random
#from random import shuffle

print('Olá, abaixo será sorteado e mostrado a todos a ordem dos quatro alunos, para apresentação dos seus trabalhos \n')

al1 = str(input('Digite o primeiro nome do aluno: '))
al2 = str(input('Digite o segundo nome do aluno: '))
al3 = str(input('Digite o terceiro nome do aluno: '))
al4 = str(input('Agora, o quarto nome do aluno: '))
print(' ')

list = [al1, al2, al3, al4]
#ord = random.shuffle(list)
random.shuffle(list)

print('Você digitou os nomes acima de {}, {}, {} e {}'.format(al1.upper(), al2.upper(), al3.upper(), al4.upper()))
print('Um momento, pois está sendo sorteado ... ')
print('Os quatros nomes sorteados em ordem para as suas apresentações, serão: ')
print(' ')
#print('{}'.format(ord))
print(list)
