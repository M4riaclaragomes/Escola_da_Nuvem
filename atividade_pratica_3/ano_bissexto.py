# Solicita o ano ao usuário
ano_str = input("Digite o ano: ")
ano = int(ano_str)

# Um ano é bissexto se for divisível por 4,
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")