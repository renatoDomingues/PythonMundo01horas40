#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
#import string

print('Quatro nomes dos alunos serão digitados abaixo, para serem sorteados quem apagará o quadro:')
cand1 = input('Digite o primeiro nome: ')
cand2 = input('Digite o segundo nome: ')
cand3 = input('Agora, digite o segundo nome: ')
cand4 = input('O ultimo nome: ')
print(' ')

list = [cand1, cand2, cand3, cand4]
#alunos = random.randint(cand1, cand2, cand3, cand4) 
alunos = random.choice(list)

print('Você digitou acima os nomes de {}, {}, {} e {}.'.format(cand1.upper(), cand2.upper(), cand3.upper(), cand4.upper()))
print('Espere um pouco, processando o sorteio ... ...')
print('O nome sorteado é ... \n')

print('O nome que será responsavel de apagar o quadro será {}.'.format(alunos.upper()))