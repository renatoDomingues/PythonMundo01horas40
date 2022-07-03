#Crie um algaritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Por favor, digite um número: '))
print(' ')

do = n*2
tri = n*3
#tParte = n/3 =>essa variavel seria a terça parte
raiz = n**(1/2)

#Na situação abaixo, não podemos fornecer as variaveis acima
#print('O dobro do número {} digitado acima é {}; \n'.format(n, (n*2)))
#print('O triplo do número {} digitado acima é {}; \n'.format(n, (n*3)))
#print('A raiz quadrada do número {} digitado acima é {:.2f};'.format(n, (n**(1/2))))
#Outra maneira abaixo de encontrar a raiz quadrada
#print('A raiz quadrada do número {} digitado acima é {:.2f};'.format(n, pow(n, (1/2)))

print('O dobro do número {} digitado acima é {}; \n'.format(n, do))
print('O triplo do número {} digitado acima é {}; \n'.format(n, tri))
print('A raiz quadrada do número {} digitado acima é {:.2f};'.format(n, raiz))