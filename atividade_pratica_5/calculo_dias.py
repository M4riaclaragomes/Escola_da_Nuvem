from datetime import date

def calcular_idade_em_dias(ano_nascimento: int) -> int:
    """
    Calcula a idade da pessoa em dias com base no ano de nascimento.
    """
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    idade_dias = idade_anos * 365  # Aproximação simples, sem anos bissextos
    return idade_dias

# --- Programa principal ---
try:
    ano_nascimento = int(input("Digite seu ano de nascimento (ex: 2000): "))
    idade_dias = calcular_idade_em_dias(ano_nascimento)
    print(f"Você tem aproximadamente {idade_dias} dias de vida.")
except ValueError:
    print("Erro: por favor, insira um ano de nascimento válido.")
