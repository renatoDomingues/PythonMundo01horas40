n1 = int(input('Por favor, digite um valor: '))
n2 = int(input('Agora, digite outro valor: '))

print('O tipo primitivo digitado', type(n1), type(n2))

s = n1 + n2
#print('A soma entre', n1, 'e', n2, 'vale', s)
print('A soma entre o primeiro número {} e o segundo número digitado {}, são {}.'.format(n1, n2, s))
