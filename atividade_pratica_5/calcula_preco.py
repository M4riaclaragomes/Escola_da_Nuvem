def calcular_preco_final_desconto():
  """
  Calcula o preço final de um produto após a aplicação de um desconto.
  """
  try:
    preco_original = float(input("Informe o preço original do produto: "))
    percentual_desconto = float(input("Informe o percentual de desconto (ex: 10 para 10%): "))

    if percentual_desconto < 0 or percentual_desconto > 100:
      print("O percentual de desconto deve estar entre 0 e 100.")
      return

    valor_desconto = preco_original * (percentual_desconto / 100)
    preco_final = preco_original - valor_desconto

    print(f"O preço final com desconto é: R${preco_final:.2f}")

  except ValueError:
    print("Entrada inválida. Por favor, digite apenas números.")

calcular_preco_final_desconto()
