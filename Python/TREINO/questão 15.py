qH = int(input("Quanto você guanha por hora: "))
hT = int(input("Quantas horas você trabalhou: "))

salarioB = qH * hT

ir = (11/100.0 * salarioB)
inss = (8/100.0 * salarioB)
sindicato = (5/100.0 * salarioB)

vT = ir + inss + sindicato
salarioL = salarioB - vT

print ('Seu salário bruto é',salarioB)

print ('Valor dos impostos:')
print ('IR: ',ir)
print ('INSS: ',inss)
print ('Sindicato: ',sindicato)

print ('Seu salário liquido é: ',salarioL)