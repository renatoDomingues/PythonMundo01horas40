#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

#import datatime
from datetime import date

print('Olá, vamos saber se o ano é ou não BISSEXTO!?')
print('O ano bissexto acontece a cada quatro anos e tem duração de 366 dias, diferentemente dos demais que têm 365 dias.')
print(' ')
print('Por favor, digite um ano abaixo, como exemplo "2012" OU pode colocar o número ZERO para analisar o ano ATUAL: ')
anoBis = int(input('=> '))
print(' ')
print('O ano que você digitou acima foi {:.0f}'.format(anoBis))

resto4 = anoBis%4
resto100 = anoBis%100
resto400 = anoBis%400
# if anoBis$4==0:

if anoBis==0:
    anoBiss = date.today().year
    print('O ano de {}'.format(anoBiss))
if resto4==0 and resto100!=0 or resto400==0:
    print('PARABÊNS, pois tu ACERTOU o ano que você digitou é BISSEXTO!!')
else:
    print('DESCULPA tu errou, o número digitado acima não é BISSEXTO!')
