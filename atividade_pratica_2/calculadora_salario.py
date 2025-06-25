# Leitura dos dados do funcionário
numero_funcionario = int(input('Digite seu número: '))
horas_trabalhadas = int(input('Digite a quantidade de horas trabalhadas: '))
valor_por_hora = float(input('Digite o valor da hora de trabalho: '))

# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora

# Exibição do resultado
print(f"NÚMERO = {numero_funcionario}")
print(f"SALÁRIO = R$ {salario:.2f}")