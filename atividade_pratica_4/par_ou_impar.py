numeros_pares = 0
numeros_impares = 0

print("Digite números inteiros (ou 'fim' para encerrar):")

while True:
    entrada = input("Número: ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"O número {numero} é PAR.")
            numeros_pares += 1
        else:
            print(f"O número {numero} é ÍMPAR.")
            numeros_impares += 1
    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite um número inteiro ou 'fim'.")

print("\n--- Resumo ---")
print(f"Quantidade de números pares inseridos: {numeros_pares}")
print(f"Quantidade de números ímpares inseridos: {numeros_impares}")