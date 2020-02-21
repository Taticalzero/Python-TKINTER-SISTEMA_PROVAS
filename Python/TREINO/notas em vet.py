notas = []
for x in range(4):
  nota = float(input("Digite a %da nota:" %(x+1)))
  notas.append(nota)
media = sum(notas)/4 
print("Média: %.2f" %media)