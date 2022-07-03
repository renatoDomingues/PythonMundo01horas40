#nome = input('Qual é o seu nome? ')
#print('Prazer em te conhecer {:<20}!'.format(nome))
#print('Prazer em te conhecer {:^20}!'.format(nome))
#print('Prazer em te conhecer {:>20}!'.format(nome))

#n1 = int(input('Um valor: '))
#n2 = int(input('Outro valor: '))
#print('A soma vale {}'.format(n1+n2))

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(' ')

s = n1+n2
sub = n1-n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2

#print('A soma é {}, a subtração é {}, o produto multiplicação é {} e a divisão é {:.3f}'.format(s, sub, m, d), end=' ')
#print('A divisão inteira é {} e a potência é {}'.format(di, e))

print(' A soma é {}, \n A subtração é {}, \n O produto multiplicação é {} \n A divisão é {:.3f} \n'.format(s, sub, m, d), end='')
print(' A divisão inteira é {} \n A potência é {}'.format(di, e))
