#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Site oficial da loja "Domingues"')
p = float(input('Por favor, passe o seu codigo de barra ou digite o preço aqui: R$'))

#Regra de três:
#R$10 = 100%
# X   = 5%
#10x5 = x.100

#d = (p*5)/100
#valorA = p-d
novoP = p - (p*5/100)

#print('O preço digitado foi R${}'.format(p))
#print('Que sorte, hoje esse produto está em promoção e terá um desconto de 5% que corresponde R${}, sendo o seu valor atualizado será de R${}'.format(d, valorA))
print('O produto que custava R${:.2f} reais, na promoção com desconto de 5% vai custar R${:.2f} reais'.format(p, novoP))
