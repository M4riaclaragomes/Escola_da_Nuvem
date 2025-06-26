# Entrada: um valor de ponto flutuante para o raio
raio_str = input('Digite o valor do raio: ')
raio = float(raio_str)

# Definindo o valor de PI conforme especificado
pi = 3.14159265

# Calculando a área. 
area = pi * (raio * raio)

# Saída: Apresenta a mensagem "A=" seguido pelo valor da área com 4 casas decimais
print(f"A={area:.4f}")