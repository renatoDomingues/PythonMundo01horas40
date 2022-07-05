#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 sendo peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

#import random
from random import randint
from time import sleep

print('JOGO DE ADVINHAÇÂO, tenta advinhar qual número o computador está pensando e vai responder!')
print('-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!? ...')
print('-=-' *20)

numInt = int(input('Escolhe um número de 0 á 5? '))
print(' ')
print('Você digitou o número {}'.format(numInt))

#jogAdv = random.randint(0, 5)
jogAdv = randint(0, 5)

print('PROCESSANDO, o computador está pensando e já vai responder ...')
sleep(3)
print(' ')

if numInt>5:
    print('ERRO, desculpa digite números entre 0 a 5 novamente ...')
if numInt==jogAdv:
    print('O número que o computador decidiu é: {}'.format(jogAdv))
    print('Meus PARABÊNS, tu acertou o que o computador estava pensando!! !!')
else:
    print('O número que o computador decidiu é: {}'.format(jogAdv))
    print('DESCULPA, pois tu errou!')
