#Faça um programa que leia o comprimento do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

#import math
from math import hypot

print('Vamos fazer o calculo dos catetos da hipotenusa abaixo')

catAdj = float(input('Digite um número que será de base para o cateto adjacente "deitado" retâgulo da hipotenusa: '))
catOps = float(input('Agora, um outro número que será de base para o cateto oposto "em pé" retâgulo da hipotenusa: '))

# H² = C² + C²
# a² = b² + c²
# Rais quadrada de hipotenusa² = catetoOposto² + catetoAdjacente³

'''
catAdj2 = catAdj*2
catOps2 = catOps*2
hip = (catAdj2+catOps2)/2
'''
#h = (catOps**2+catAdj**2)**(1/2)

#h = math.hypot(catAdj, catOps)
h = hypot(catAdj, catOps)

print('O número digitado acima do cateto adjacente vai medir {}'.format(catAdj))
print('O número digitado acima do cateto oposto vai medir {}'.format(catOps))
#print('Os números acima, darão o resultado da hipotenusa {}'.format(hip))
'''
print('Os números acima, darão o resultado da hipotenusa que medirá {:.2f}'.format(h))
'''
print('Os números acima, darão o resultado da hipotenusa que medirá {:.2f}'.format(h))
