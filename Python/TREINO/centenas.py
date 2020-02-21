numero = int(input("digite um numero menor que 1000 ---> "))
numeroStr = str(numero)
qtNumero = len(numeroStr)

if qtNumero == 3:
    centena = numeroStr[0:1]
    dezena = numeroStr[1:2]
    unidade = numeroStr[2:3]
    print( numeroStr+" = "+centena+" centenas , "+dezena+" dezenas, "+unidade+ " unidades")

if qtNumero == 2:
    dezena = numeroStr[0:1]
    unidade = numeroStr[1:2]
    print(numeroStr+" = "+dezena+" dezenas, "+unidade+ " unidades")

if qtNumero == 1:
    unidade = numeroStr[0:1]
    print (numeroStr+" = "+unidade+ " unidades")