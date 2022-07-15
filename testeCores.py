#Testes para aplicarmos cores adversas no nosso terminal IDLE Python

print('Olá mundo!')
print(' ')
print('\033[4;30;45mOlá mundo!\033[m')
print(' ')
a = 3
b = 5
print('Os valores são \033[32m{} e \033[31m{} \033[m!!!'.format(a, b))
print(' ')
nome = 'Domingues'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[m', nome, '\033[m'))
print(' ')

'''
Alguns exemplos abaixos:
RED => \033[0:30:41m
BLUE => \033[4:33:44m
YELOW => \033[1:35:43m
GREEN => \033[30:42m
BLACK => \033[m
WHITE => \033[7:30m

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
a = 3
b = 5
c = 4
e = a*b+c**2
print(e)
