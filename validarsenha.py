print("Informe a senha: ")

senha_informada = "python123"

while True:
    senha = input()
    if senha == senha_informada:
        print("Acesso liberado")
        break
    else:
        print("Senha errada, acesso negado")
