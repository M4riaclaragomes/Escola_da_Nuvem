# Solicita a temperatura ao usuário
temperatura_str = input("Digite a temperatura: ")
temperatura = float(temperatura_str)

# Solicita a unidade de origem (C para Celsius, F para Fahrenheit, K para Kelvin)
unidade_origem = input("A temperatura está em Celsius (C), Fahrenheit (F) ou Kelvin (K)? ").upper()

# Solicita a unidade para a qual converter
unidade_destino = input("Para qual unidade você quer converter (C, F ou K)? ").upper()

resultado = 0.0
nome_unidade_destino = ""

# Lógica de conversão
if unidade_origem == 'C':
    if unidade_destino == 'F':
        resultado = (temperatura * 9/5) + 32
        nome_unidade_destino = "Fahrenheit"
    elif unidade_destino == 'K':
        resultado = temperatura + 273.15
        nome_unidade_destino = "Kelvin"
    elif unidade_destino == 'C':
        resultado = temperatura
        nome_unidade_destino = "Celsius"
    else:
        print("Unidade de destino inválida. Por favor, digite 'C', 'F' ou 'K'.")

elif unidade_origem == 'F':
    if unidade_destino == 'C':
        resultado = (temperatura - 32) * 5/9
        nome_unidade_destino = "Celsius"
    elif unidade_destino == 'K':
        resultado = (temperatura - 32) * 5/9 + 273.15
        nome_unidade_destino = "Kelvin"
    elif unidade_destino == 'F':
        resultado = temperatura
        nome_unidade_destino = "Fahrenheit"
    else:
        print("Unidade de destino inválida. Por favor, digite 'C', 'F' ou 'K'.")

elif unidade_origem == 'K':
    if unidade_destino == 'C':
        resultado = temperatura - 273.15
        nome_unidade_destino = "Celsius"
    elif unidade_destino == 'F':
        resultado = (temperatura - 273.15) * 9/5 + 32
        nome_unidade_destino = "Fahrenheit"
    elif unidade_destino == 'K':
        resultado = temperatura
        nome_unidade_destino = "Kelvin"
    else:
        print("Unidade de destino inválida. Por favor, digite 'C', 'F' ou 'K'.")

else:
    print("Unidade de origem inválida. Por favor, digite 'C', 'F' ou 'K'.")

# Exibe o resultado, se as entradas forem válidas
if nome_unidade_destino: # Isso verifica se nome_unidade_destino não está vazio, ou seja, se uma conversão foi definida
    print(f"{temperatura:.1f} {unidade_origem} é igual a {resultado:.1f} {nome_unidade_destino}.")