
a=float(input("Informe o valor de a : "))
b=float(input("Informe o valor de b : "))
c=float(input("Informe o valor de c : "))

raiz1=0
raiz2=0
delta = b**2 - 4*a*c
if delta == 0:
    raiz1 = (-b +(delta**(1/2))/(2*a))
raiz2 = (-b - (delta**(1/2))/(2*a))

print("O valor da primeira raiz", raiz1)
print("O valor da segunda raiz", raiz2)
