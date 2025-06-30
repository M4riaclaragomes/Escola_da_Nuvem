while True:
    senha = input("Digite sua senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Saindo do programa.")
        break

    if len(senha) < 8:
        print("Senha fraca: A senha deve ter pelo menos 8 caracteres.")
        continue

    tem_numero = False
    for char in senha:
        if char.isdigit():
            tem_numero = True
            break

    if not tem_numero:
        print("Senha fraca: A senha deve conter pelo menos um número.")
        continue

    print("Senha forte! Sua senha foi aceita.")
    break