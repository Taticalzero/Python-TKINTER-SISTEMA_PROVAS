turno = str(input('Digite em que turno você estuda: M=maturnino, V=vespertino ou N-noturno: ').upper())

if turno == 'M':
    print('Bom dia!')

elif turno == 'V':
    print('Boa tarde!')

elif turno == 'N':
    print('Boa noite!')

else:
    print('Valor inválido!')