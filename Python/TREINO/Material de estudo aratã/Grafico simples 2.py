import matplotlib.pyplot as plt
meses = ["janeiro","fevereiro","março","abril","maio","junho"]
valores = [105235,107697,110256,109236,108856,109986]

plt.plot(meses,valores)
plt.ylim(100000,120000)


plt.title("Faturamneto no primeiro semestre de 2017")
plt.xlabel("Meses")
plt.ylabel("Faturamento em R$")

plt.show()