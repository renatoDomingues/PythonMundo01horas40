#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,00 reais, calcule um aumento de 10% por cento. Para os inferiores ou iguais, o aumento é de R$15% por cento.

print('-=-' *10,'TESTANDO', '-=-' *10)
print('A fução desse software é para calcular aumento dos salários dos funcionarios')
print('Digite abaixo o salário para calcular: ')
salFunc = float(input('=> '))
print('O salário digitado acima foi R${} reais'.format(salFunc))
print(' ')

aum10 = (salFunc*10)/100
sal10 = salFunc+aum10
aum15 = (salFunc*15)/100
sal15 = salFunc+aum15
'''
novoSal15 = salFunc+(salFunc*15/100)
novoSal10 = salFunc+(salFunc*10/100)
'''

if salFunc<=1250:
    print('O aumento salarial será de R${:.2f} reais'.format(aum15))
    print('O seu salário antigo, já somados com aumento acima, será no total de R${} reais'.format(sal15))    
else:
    print('O aumento salarial será de R${} reais'.format(aum10))
    print('O seu salário antigo, já somados com aumento acima, será no total de R${} reais'.format(sal10))

print(' ')
print('-=-' *10,'FIM!', '-=-' *10)
