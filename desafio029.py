#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dezendo que ele foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

print('')
print('CUIDADO, limite de velocidade, pois radar proximo')
print('RADAR velocidade MAXIMA de até 80Km')
print(' ')
print('Por favor, digite a velocidade do seu veiculo: ')
velRad = float(input('=> '))
print(' ')
#print('Sua velocidade foi {}Km por hora.'.format(velRad))

multa = (velRad-80)*7
pontos = (velRad-80)*2

if velRad >80:
    print('Nesse instante, a sua velocidade foi {}Km por hora.'.format(velRad))
    print('O teu veiculo foi MULTADO e o valor cobrado será R$ {} reais!'.format(multa))
    print('E será creditada {:.0f} pontos na sua pontuação na sua carteira de habilitação'.format(pontos))
else:
    print('Nesse instante, a sua velocidade foi {}Km por hora.'.format(velRad))
    print('Velocidade abaixo da punição. Segue a viagem com atenção e cuidado')
    print('Se for dirijir, não bebe e nunca utiliza celular dirijindo!')


'''
# \033(style:tex:backM) =>personalisar o seu terminal no Python
# \033(0:33:44m) =>Um exemplo
# Alguns exemplos abaixo de varios:
STYLE      <=> TEXT <=> BACK
0 (none)        30       40 (branco)
1 (bold)        31       41 (vermelho)
4 (underline)   32       42 (verde)
7 (negative)    33       43 (amarelo)
                34       44 (azul)
                35       45 (roxo)
                36       46 (azul claro)
                37       47 (cinza)
'''