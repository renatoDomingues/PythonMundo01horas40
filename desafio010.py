#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere US$1,00 = R$3,27.

print('Tabela de conversão da moeda Real para o Dolar americano \n')
real = float(input('Digite, quantos em reais você tem na sua carteira? R$'))

#d = 327
#co = (r/d)*100
dolar = real/3.27

print('O cambio de hoje do Dolar americano EUA US$3,27 dólares')
print('Convertendo da moeda Real Brasil para Dolar americano \n')
print('Você digitou R${} \n'.format(real))

#print('A conversão do valor digitado acima é US${:1f}'.format(dolar))
print('Com R${:.2f} você pode comprar em dólares US${:.2f}'.format(real, dolar))