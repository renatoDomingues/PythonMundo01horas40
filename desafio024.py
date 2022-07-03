#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO";

''''''
print('Digite o nome da sua cidade, porque veremos se o nome digitado começará com a palavra "SANTO"')
cidade = str(input('Em que cidade você nasceu? ' )).strip()
print('A sua cidade digitada acima foi {}!'.format(cidade.upper()))
print(' ')

#santo = cidade.find('Santo')
print('A sua cidade é parecida com nome SANTO? ')
#print(cidade[0:5]=='Santo')
print(cidade[0:5].upper()=='SANTO')

#print('Sua cidade: {}'.format(cidade))
