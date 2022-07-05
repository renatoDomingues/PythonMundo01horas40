#Desenvolva um programa que pergunta a distância de uma viagem em KM. Calcule o preço da passagem, cobrando R$0,50 centavos por KM para viagens de até 200KM e R$0,45 centavos para viagens mais longas.

print('SEJAM BEM VINDOS, ao Transporte terrestre DOMINGUES!!')
print('Contamos com os melhores e confortaveis onibus e carros, junto os motoristas profissionais e capacitados para a sua viagem.')
print(' ')
distKm = float(input('Digite a distancia da sua viagem: '))
print('A distancia digitada acima foi {}KM'.format(distKm))
print('Você está preste a começar uma viagem de {} Km'.format(distKm))
print(' ')

viaPr = distKm*0.50
viaLon = distKm*0.45


#preco = distKm *0.50 if distKm <=200 else distKm *0.45
#print('E o preço da sua passagem será de R${:.2f}'.format(preco))


if distKm <=200:
    print('O valor a cobrar da sua viagem acima {:.2f} reais'.format(viaPr))
else:
    print('O valor a cobrar da sua viagem acima {:.2f} reais'.format(viaLon))

print(' ')
print('Obrigado pela preferencia e VOLTEM LOGO!!')
