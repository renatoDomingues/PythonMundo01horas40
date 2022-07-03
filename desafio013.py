#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print(' ')
s = float(input('Por favor, informe o salário atual: R$'))
print('O salário informado acima é de R${} reais.'.format(s))

#Regra de três
#salário = 100%
#  X     =  15%
#SalárioX15 = X.100

#novoS = salario+(salario*15/100)
aumS = (s*15)/100
novoS = s+aumS

print('Com o aumento de 15% que corresponde R${:.2f} reais;'.format(aumS))
print('O seu novo salário será R${:.2f} reais;'.format(novoS))