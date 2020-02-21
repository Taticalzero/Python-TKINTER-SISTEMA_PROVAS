while(True):
	nome = str(input("Nome: "))
	idade = int(input("Idade: "))
	salario = float(input("Salário: "))
	sexo = str(input("Sexo: "))
	estadoCivil = str(input("Estado civil: "))
	if(len(nome) > 3):
		if(idade > 0 and idade <= 150):
			if(salario > 0):
				if(sexo == "f" or sexo == "F" or sexo == "m" or sexo == "M"):
					if(estadoCivil == "s" or estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "d"):
						print("Tudo OK!")
						break
					else:
						print("Estado civil inválido!")
				else:
					print("Sexo inválido!")
			else:
				print("Salário inválido!")
		else:
			print("Idade inválida!")
	else:
		print("Nome inválido!!")