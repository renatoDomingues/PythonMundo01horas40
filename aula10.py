'''
nome = str(input('Qual é o seu nome? ')).upper().strip()
print(' ')

if nome=='RENATO':
    print('Que nome lindo você tem {}!'.format(nome))
else:
    print('Desculpa, mas que nome normal que tu tem!')
print('Bom dia {}!'.format(nome))
'''

#if m>=6.0
nta1 = float(input('Digite a primeira nota: '))
nta2 = float(input('Digite a segunda nota: '))
print(' ')

m = (nta1+nta2)/2

#print('PARABÉNS' if m>=6 else 'ESTUDE MAIS')

print('A sua média baseada com as notas digitadas acima foi {:.1f}'.format(m))
print(' ')

if m>=6.0:
    print('Sua média foi boa! Meus PARABÉNS ...')
else:
    print('Sua média foi ruim! ESTUDE MAIS ...')
