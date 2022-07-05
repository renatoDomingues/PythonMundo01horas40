#Desenvolva um programa que leia o comprimento de 03 retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' *10, 'Analisador de TRIÂNGULOS', '-=-' *10)
print('Esse software calcula se pode ou não, formar um trângulo com os dados digitados abaixo ...')
rta1 = float(input('Por favor, digite um número: '))
rta2 = float(input('Por favor, digite o segundo número: '))
rta3 = float(input('Agora, digite o terceiro número: '))
print('Você digitou os números {}, {} e {}'.format(rta1, rta2, rta3))
print(' ')

if rta1<(rta2+rta3) and rta2<(rta1+rta3) and rta3<(rta1+rta2):
    print('Os números paresentados acima, são possiveis para formar um triângulo!')
else:
    print('ERRO, desculpa digite os números novamente, pois os números apresentados não são possiveis formar um triângulo!')

print(' ')
print('-=-' *15, 'FIM', '-=-' *15)
