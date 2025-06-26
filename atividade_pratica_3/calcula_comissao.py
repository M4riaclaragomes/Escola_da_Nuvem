# Entrada: nome do vendedor, salário fixo e total de vendas
nome_vendedor = input('Digite seu nome: ')

salario_fixo_str = input('Digite seu salário fixo: ')
salario_fixo = float(salario_fixo_str)

total_vendas_str = input('Quantas vendas você fez no total?: ')
total_vendas = float(total_vendas_str)

# Calcula a comissão (15% das vendas)
comissao = total_vendas * 0.15

# Calcula o total a receber
total_a_receber = salario_fixo + comissao

# Saída: Imprime o total que o funcionário deverá receber com duas casas decimais
print(f"TOTAL = R$ {total_a_receber:.2f}")