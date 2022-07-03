#Escreva um programa que converta uma temperatura digitada em °C celsius para °F fahrenheit.

cels = float(input('Informe a temperatua em °C celsius: '))

#novaTemp = 32+(cels*1.8)
novaTemp = ((9*cels)/5)+32

print('A temperatura informada acima de {}°C celsius, corresponde a {}°F Fahrenheit!!'.format(cels, novaTemp))
