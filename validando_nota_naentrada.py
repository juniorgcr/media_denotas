nome_aluno = input('Digite seu nome completo: ')
bimestre_1 = float(input('Primeiro bimestre: '))
while bimestre_1 > 10:
    bimestre_1 = float(input('ATENÇÃO! Você digitou valor maior que 10. Primeiro bimestre: '))
bimestre_2 = float(input('Segundo bimestre: '))
while bimestre_2 > 10:
    bimestre_2 = float(input('ATENÇÃO! Você digitou valor maior que 10. Segundo bimestre: '))
bimestre_3 = float(input('Terceiro bimestre: '))
while bimestre_3 > 10:
    bimestre_3 = float(input('ATENÇÃO! Você digitou valor maior que 10. Terceiro bimestre: '))
bimestre_4 = float(input('Quarto bimestre: '))
while bimestre_4 > 10:
    bimestre_4 = float(input('ATENÇÃO! Você digitou valor maior que 10. Quarto bimestre: '))
media_final = (bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4) / 4

print('Olá {}'.format(nome_aluno), '!\nsua média final é: {}'.format(media_final))
if media_final >= 7:
    print('Parabéns, aluno!\nVocê passou de ano')
else:
    print('Infelizmente você foi reprovado, aluno!\nEstude mais no próximo ano')