#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. Ex: Ana Maria de Souza - primeiro=Ana - último=Souza;

print('Esse programa foi desenvolvido para ler o nome com sobrenome digitado "COMPLETO", sendo depois mostrar na tela o primeiro e o último nome separadamente!')
print(' ')
noSob = str(input('Por favor, digite o seu nome e sobrenome: ')).strip().upper()
print(' ')
print('Muito prazer em te conhecer {}'.format(noSob))
print(' ')

dividir = noSob.split()
print(dividir)
print('O seu primeiro nome é {}'.format(dividir[0]))
print('E já o seu último nome é {}'.format(dividir[len(dividir)-1]))
print(' ')
print('Obrigado por participar!!')
