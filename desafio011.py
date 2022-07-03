#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m².

print('Realize o seu sonho de pintar o seu lar hoje mesmo!')
print('Calcular a sua área do seu ambiente da sua casa abaixo:')

l = float(input('Qual é a sua largura em metros? '))
a = float(input('Qual é a sua altura em metros? '))
print(' ')

calA = l*a
t1 = 2
at = calA/t1

print('A largura digitada foi {}m² e a altura digitada {}m², pois então a sua área é {} metros'.format(l, a, calA))
print('Uma lata de tinta pode pinta por volta de 2 metros quadrado de área \n')
print('Será necessário de {} litro(s) de tinta para pintar a área mencionada acima'.format(at))