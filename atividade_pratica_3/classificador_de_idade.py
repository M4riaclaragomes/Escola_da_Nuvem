# Solicita a idade ao usuário
idade_str = input("Digite sua idade: ")
idade = int(idade_str)

# Classifica a idade usando condicionais
if idade >= 0 and idade <= 12:
    print("Classificação: Criança")
elif idade >= 13 and idade <= 17:
    print("Classificação: Adolescente")
elif idade >= 18 and idade <= 59:
    print("Classificação: Adulto")
else:  # idade >= 60
    print("Classificação: Idoso")