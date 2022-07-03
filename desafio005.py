#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.

n = int(input('Digite um número: '))
print(' ')

su = n+1
an = n-1

#No caso abaixo, não pode criar as variaveis acima
#print('Analisando o número {} digitado acima, pois o seu sucessor é {} e o seu antecessor é {}'.format(n, (n+1), (n-1)))

print('O sucessor do número {} digitado acima é {}: '.format(n, su))
print('O antecessor do número {} digitado acima é {}: '.format(n, an))