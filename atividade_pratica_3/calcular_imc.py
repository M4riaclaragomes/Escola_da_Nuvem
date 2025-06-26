# Solicita o peso e a altura do usuário
peso_str = input("Digite seu peso em kg: ")
peso = float(peso_str)

altura_str = input("Digite sua altura em metros (exemplo:1.60) : ")
altura = float(altura_str)

# Calcula o IMC
imc = peso / (altura * altura)

# Determina a classificação 
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Apresenta o resultado
print(f"Seu IMC é: {imc:.2f}")
print(f"Classificação: {classificacao}")