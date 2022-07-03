#Crie um programa que leia o nome completo de uma pessao e mostra: (1)- O nome com todas as letras maiúsculas; (2)-O nome com todas minúsculas; (3)- Quantas letras ao todo (sem considerar espaços); (4)- Quantas letras tem o primeiro nome;

'''
nome = str(input('Digite o seu nome completo "nome e sobrenome": '))
print('O seu nome digitado acima foi {}'.format(nome))
print(' ')

divididoNome = nome.split()

print('O seu nome com todas as letras maiúscula: {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas: {}'.format(nome.lower()))
print('* Sabendo quantas letras ao todo tem o seu nome, desconsiderando os espaços: {}'.format(len(nome.strip())))
print('* Sabendo quantas letras ao todo tem o seu nome, considerando os espaços: {}'.format(nome.count('')))
print('* Quantas letras tem o seu primeiro nome: {}'.format(divididoNome[0].count('')))
'''

#nome = str(input('Digite o seu nome completo: '))
nome = str(input('Digite o seu nome completo: ')).strip()
print('Analisando o seu nome ...')
print(' ')
print('Seu nome em maiúscula é {}'.format(nome.upper()))
print('Seu nome em minúscula é {}'.format(nome.lower()))
#print('Seu nome tem ao todo {} letras.'.format(len(nome)))
print('Seu nome tem ao todo {} letras.'.format(len(nome)-nome.count(' ')))
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
print(' ')
print('Outra maneira codar: ')
separa = nome.split()
print('', separa)
print('O seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
