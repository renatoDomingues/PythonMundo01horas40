frase = 'Curso em Vídeo Python'
print(' ')
frases = 'Curso em Vídeo Python'
print(' ')

print('* 1 =>', frase.count('O'))
print('* 2 =>', frase.count('o'))
print('* 3 =>', frases.upper().count('O'))
print('* 4 =>', len(frase))
print(' ')
frasess = '  Curso em Vídeo Python  '
print('* 5 =>', len(frasess))
print('* 6 =>', len(frasess.strip()))
frase2 = 'Curso em Vídeo Python'
print('* 7 =>', frase2)
print('* 8 =>', frase2[0])
#print('9 =>', frase2.replace('Python', 'Android'))
print(' ')
frase2 = frase2.replace('Python', 'Android')
print('* 9 =>', frase2)
print('* 12 =>', 'Curso' in frase)
print('* 13 =>', frase.find('Curso'))
print('* 14 =>', frase.find('Vídeo'))
print('* 15 =>', frase.find('video'))
print('* 16 =>', frase.lower().find('vídeo'))
print(' ')
estudo = 'Estou estudando agora Python'
print('* 17 =>', estudo.split())
print(' ')
trabalho = 'Trabalhei hoje de madrugada'
dividido = trabalho.split()
print('* 18 =>', dividido)
print('* 19 =>', dividido[0])
print('* 20 =>', dividido[2])
print('* 21 =>', dividido[3][4])
