#Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A"; Em que posição ela aparece a primeira vez; Em que posição ela aparece a última vez;

print('Esse programa foi desenvolvido, para alertar quantas vezes junto a primeira e a última que aparece a letra "A"! ')
letra = str(input('Digite uma frasae qualquer: ')).strip().upper()
print('A frase digitada acima foi {}'.format(letra))
print(' ')

#vezes = len(letra.count('A'))
letraPri = letra.find('A')+1
letraUlt = letra.rfind('A')+1

print('A letra "A" foi encontrada na sua frase? {}', 'A' in letra)
print('Quantas vezes tem a letra "A": {}'.format(letra.count('A')))
#print('A primeira letra "A" apareceu na posição {}'.format(letra.find('A')+1))
print('A primeira letra "A" apareceu na posição {}'.format(letraPri))
#print('A última letra "A" apareceu na posição {}'.format(letra.rfind('A')+1))
print('A última letra "A" apareceu na posição {}'.format(letraUlt))
