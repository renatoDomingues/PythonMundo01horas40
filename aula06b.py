numeroInteiro = int(input('(1)- Digite um valor, por favor: '))
print(numeroInteiro)
print(type(numeroInteiro))

numeroFloat = float(input('(2)- Digite um valor, por favor: '))
print(numeroFloat)
print(type(numeroFloat))

numeroBool = bool(input('(3)- Digite um valor, por favor: '))
print(numeroBool)
print(type(numeroBool))

numeroString = str(input('(4)- Digite um valor, por favor: '))
print(numeroString)
print(type(numeroString))

print('******************************************************************')

n = input('Digite algo: ')
print('O que digitou é númerico? {}'.format(n.isnumeric()))
print('O que digitou é alpha? {}'.format(n.isalpha()))
print('O que digitou é alpha e númerico? {}'.format(n.isalnum()))
print('O que digitou são letras maiusculas? {}'.format(n.isupper()))