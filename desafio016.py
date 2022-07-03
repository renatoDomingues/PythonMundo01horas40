#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira. Ex: Digite um número: 6.127, sendo o número tem a parte inteira 6.

'''
#import math
from math import trunc

#numReal = float(input('Digite um número qualquer: '))
num = float(input('Digite um número qualquer: '))

#numInt = math.isqrt(numReal)

#print('A extração do número inteiro, do múmero digitado acima é: {}'.format(numReal))
#print('O valor digitado acima foi {} e a sua porção inteira é {}'.format(num, math.trunc(num)))
print('O valor digitado acima foi {} e a sua porção inteira é {}'.format(num, trunc(num)))
'''

num = float(input('Digite um valor: '))

print('O valor digitado acima foi {} sendo a sua porção interia é {}'.format(num, int(num)))
