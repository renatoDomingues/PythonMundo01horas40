#Escreva um programa que leia um valor em metros e o exibe convertido em centímetros e milímetros.

print('Olá, esse programa para conversão para centímetros e milímetros \n')

m = float(input('Oi, digite um número que será como base em metros, para a conversão? '))
print(' ')

# KM - HM - DAM - M - DM- CM - MM
km = m/100
hm = m/100
dam = m/10
m = m
dm = m*10
ce = m*100
mm = m*1000

print('O número {} em metros digitada acima, a conversão em km foi {} \n'.format(m, km))
print('O número {} em metros digitada acima, a conversão em hm foi {} \n'.format(m, hm))
print('O número {} em metros digitada acima, a conversão em dam foi {} \n'.format(m, dam))
print('O número {} em metros digitada acima, a conversão em dm foi {} \n'.format(m, dm))
print('O número {} em metros digitada acima, a conversão em centímetros foi {} \n'.format(m, ce))
print('O número {} em metros digitada acima, a conversão em milímetros foi {} \n'.format(m, mm))