#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('Programa tabuada ... \n')
n = int(input('Digite um número qualquer, que a partir do mesmo será composto a tabuada: '))
print(' ')

#t0 = n*0
#t1 = n*1
#t2 = n*2
#t3 = n*3
#t4 = n*4
#t5 = n*5
#t6 = n*6
#t7 = n*7
#t8 = n*8
#t9 = n*9
#t10 = n*10

print('Calculando a tabuada completa do número {} digitado acima: \n'.format(n))
#print('Tabuada de {}: '.format(n))
#print('{} X 0 = {} '.format(n, t0))
#print('{} X 1 = {} '.format(n, t1))
#print('{} X 2 = {} '.format(n, t2))
#print('{} X 3 = {} '.format(n, t3))
#print('{} X 4 = {} '.format(n, t4))
#print('{} X 5 = {} '.format(n, t5))
#print('{} X 6 = {} '.format(n, t6))
#print('{} X 7 = {} '.format(n, t7))
#print('{} X 8 = {} '.format(n, t8))
#print('{} X 9 = {} '.format(n, t9))
#print('{} X 10 = {} \n'.format(n, t10))

print('-' *14)
print('{} X {:2} = {}'.format(n, 0, n*0))
print('{} X {:2} = {}'.format(n, 1, n*1))
print('{} X {:2} = {}'.format(n, 2, n*2))
print('{} X {:2} = {}'.format(n, 3, n*3))
print('{} X {:2} = {}'.format(n, 4, n*4))
print('{} X {:2} = {}'.format(n, 5, n*5))
print('{} X {:2} = {}'.format(n, 6, n*6))
print('{} X {:2} = {}'.format(n, 7, n*7))
print('{} X {:2} = {}'.format(n, 8, n*8))
print('{} X {:2} = {}'.format(n, 9, n*9))
print('{} X {:2} = {}'.format(n, 10, n*10))
print('-' *14)

print(' ')
print(' FIM ')
