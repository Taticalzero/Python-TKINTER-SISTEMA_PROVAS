pesos = int(input('Digite o numero de quilos de peixe vc pegou:'))
if pesos > 50:
    multa = (pesos - 50) * 4
    print (f'Total da multa: {multa}')
else:
    print ('Não teve excesso')