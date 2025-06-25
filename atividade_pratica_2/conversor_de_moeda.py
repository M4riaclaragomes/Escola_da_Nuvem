# Dados
valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

# Conversão
valor_dolar = round(valor_reais / taxa_dolar, 2)
valor_euro = round(valor_reais / taxa_euro, 2)

# Exibição dos resultados
print(f"R$ {valor_reais:.2f} equivalem a:")
print(f"US$ {valor_dolar:.2f}")
print(f"€ {valor_euro:.2f}")