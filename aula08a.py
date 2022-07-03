import math
#from math import sqrt, floor

num = int(input('Digite um número: '))

raiz = math.sqrt(num)
#raiz = sqrt(num)

print('A raiz do número digitado acima {} é igual a {:.2f}'.format(num, raiz))
print('A raiz do número digitado acima {} é igual a {} arrendodado para acima;'.format(num, math.ceil(raiz)))
print('A raiz do número digitado acima {} é igual a {} arrendodado para abaixo;'.format(num, math.floor(raiz)))
