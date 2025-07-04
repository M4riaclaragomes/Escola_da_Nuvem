import re

def verificar_palindromo_com_input():
  """
  Verifica se uma palavra ou frase inserida pelo usuário é um palíndromo,
  ignorando espaços e pontuação.
  """
  frase = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

  # Remove espaços, pontuação e converte para minúsculas
  frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()

  if frase_limpa == frase_limpa[::-1]:
    print("Sim") # É um palíndromo
  else:
    print("Não") # Não é um palíndromo

# --- Chame a função aqui para ela ser executada! ---
verificar_palindromo_com_input()