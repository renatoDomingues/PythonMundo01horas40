#Escreva um programa que pergunte a quantidade de KM percorrido por carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 reais por dia e R$0,15 centavos por KM rodado.

print('Sejam Bem Vindos, a nossa loja Familia Domingues!! !!')

diasAl = int(input('Por favor, digite quantos dias alugados? '))
kmRod = float(input('Agora, digite quantos Km rodados? '))

diasPorDia = diasAl*60
kmPorKm = kmRod*0.15
totalPagar = diasPorDia+kmPorKm
#pago = (dias*60)+(km*0.15)

print('Você informou que foi {} dias aluguel, que corresponde R${:.2f} reais;'.format(diasAl,diasPorDia))
print('Você informou que rodou {:.1f} Km, que corresponde R${:.2f} reais;'.format(kmRod ,kmPorKm))
print('O total a pagar é de R${:.2f} reais'.format(totalPagar))
