#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, casseno e tangente desse ângulo.

import math
#form math import radians, sin, cos, tan

angQual = float(input('Digite um número que será a base de um ângulo: '))
print(' ')

seno = math.sin(math.radians(angQual))
cosseno = math.cos(math.radians(angQual))
tangente = math.tan(math.radians(angQual))

'''
seno = sin(radians(angQual))
cosseno = cos(radians(angQual))
tangente = tan(radians(angQual))
'''

'''
SENO <=> Cateto Oposto;
COSSENO <=> Cateto Adjacente;

SENO "SEN" = CATETO OPOSTO / HIPOTENUSA
COSSENO "COS" = CATETO ADJACENTE / HIPOTENUSA
TANGENTE "TAN" = CATETO OPOSTO / CATETO ADJACENTE

O SEN é uma linha vertical;
O COS é uma linha horizontal;
'''

print('O número digitado acima que será um dos ângulos foi {}'.format(angQual))
print('O SENO do ângulo qualquer digitado acima foi de {:.2f}'.format(seno))
print('O COSSENO do ângulo qualquer digitado acima foi de {:.2f}'.format(cosseno))
print('A TANGENTE do ângulo qualquer digitado acima foi de {:.2f}'.format(tangente))
