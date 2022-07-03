import random
import emoji

num = random.random()
num2 = random.randint(1, 10)

#print(num)
print('Gerar um número aleatorio => {}'.format(num))
print('Gerar um número de 01 até 10 => {}'.format(num2))

print(emoji.emojize('Olá mundo : sunglasses:', use_aliases=True))
