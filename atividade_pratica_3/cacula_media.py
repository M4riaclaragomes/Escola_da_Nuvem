# Entrada das quatro notas separadamente
n1 = float(input("Digite a primeira nota (N1): "))
n2 = float(input("Digite a segunda nota (N2): "))
n3 = float(input("Digite a terceira nota (N3): "))
n4 = float(input("Digite a quarta nota (N4): "))

# Calcula a média ponderada com pesos 2, 3, 4 e 1
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

# Exibe a média inicial
print(f"Media: {media:.1f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    
    # Entrada da nota do exame
    exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {exame:.1f}")
    
    # Recalcula a média final
    media_final = (media + exame) / 2

    # Verifica a situação final
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    # Exibe a média final
    print(f"Media final: {media_final:.1f}")
