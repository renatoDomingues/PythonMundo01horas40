#Crie um programa que leia um número inteiro qualquer e mostra na tela se ele é PAR ou ÍMPAR.

print('Esse programa irá dizer se o número digitado é PAR ou IMPAR')
ParImpar = int(input('Digite um número inteiro qualquer: '))
print(' ')
print('Você digitou acima o número {}'.format(ParImpar))

num = ParImpar%2
#print('O resultado foi {}'.format(num))

if num==0:
    print('O número digitado acima é PAR!')
else:
    print('O número digitado acima é IMPAR!!')

'''
Um número pode ser considerado par ou ímpar. 
Os números pares são aqueles terminados em 0, 2, 4, 6 ou 8, 
já os ímpares são números terminados em 1, 3, 5, 7 ou 9.
'''
