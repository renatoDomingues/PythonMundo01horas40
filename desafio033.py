#Faça um programa que leia 03 números e mostre qual é o maior e qual é o menor.

print('O intuito deste programa é demonstrar qual o MAIOR e o MENOR dos números digitados ABAIXO')
print('Por favor, digite 03 números ...')
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o primeiro número: '))
n3 = int(input('Digite o primeiro número: '))
print('Você digitou acima os números {}, {} e {}'.format(n1, n2, n3))
print(' ')


menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O MENOR valor digitado foi {}'.format(menor))

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O MENOR valor digitado foi {}'.format(maior))

'''
print(' ')
print('PROCESSANDO, avaliando o número MAIOR ...')
if n1==n2 or n2==n3 or n3==n1:
    print('ERRO, por favor digite novamente com números diferentes!')
if n1>n2 and n1>n3:
    maior1 = n1
    print('O número MAIOR é {}'.format(maior1))
if n2>n1 and n2>n3:
    maior2 = n2
    print('O número MAIOR é {}'.format(maior2))
if n3>n1 and n3>n2:
        maior3 = n3
        print('O número MAIOR é {}'.format(maior3))

print(' ')
print('PROCESSANDO, avaliando o número MENOR ...')
if n1<n2 and n1<n3:
    menor1 = n1
    print('O número MENOR é {}'.format(menor1))
if n2<n1 and n2<n3:
    menor2 = n2
    print('O número MENOR é {}'.format(menor2))
if n3<n1 and n3<n2:
        menor3 = n3
        print('O número MENOR é {}'.format(menor3))
'''
print(' ')
print('OBRIGADO por participar conosco! ...')