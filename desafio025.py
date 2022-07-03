#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome;

print('O nome digitado abaixo, irá confirmar se tem ou não o nome "SILVA" ')
nome = str(input('Por favor , digite o seu nome: ')).upper().strip()
print('O seu nome digitado acima foi {}'.format(nome))
print(' ')

#silva = nome[0:5]=='SILVA'
#'SILVA' in nome

print('O seu nome tem ou não tem o nome "SILVA"? ')
print('SILVA' in nome)
