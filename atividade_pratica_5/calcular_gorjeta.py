def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    """
    Calcula o valor da gorjeta baseada no valor da conta e na porcentagem desejada.
    """
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# --- Programa principal ---
try:
    valor_conta = float(input("Digite o valor total da conta: R$ "))
    porcentagem = float(input("Digite a porcentagem de gorjeta que deseja deixar (ex: 10, 15, 20): "))

    valor_gorjeta = calcular_gorjeta(valor_conta, porcentagem)
    print(f"Gorjeta a ser deixada: R$ {valor_gorjeta:.2f}")

except ValueError:
    print("Erro: por favor, insira números válidos para o valor da conta e a porcentagem da gorjeta.")
