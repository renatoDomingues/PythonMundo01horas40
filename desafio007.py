#Desenvolva um programa que leia asa duas notas de um aluno, calcule e mostre a sua média.

nta1 = float(input('Por favor, digite a sua primeira nota: '))
nta2 = float(input('Agora, digite a sua segunda nota: '))
print('Calculando a sua média, por favor aguarde ...')
print(' ')

#s = nta1+nta2
#m = s/2

m = (nta1+nta2)/2

print('Resposta: \n')
#print('A média da primeira nota {} com a segunda nota {} acima é {}'.format(nta1, nta2, m))
print('A média da primeira nota {:.1f} com a segunda nota {:.1f} acima é {:.1f}'.format(nta1, nta2, m))