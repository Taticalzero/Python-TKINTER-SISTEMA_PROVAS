

while True:
    user = str(input("Nome de usuario: "))
    senha = str(input("Senha: "))
    if user != senha :
        break

print("Usuário: %s | Senha: %s" %(user, senha))