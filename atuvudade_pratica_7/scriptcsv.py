# 2- Crie um script em Python que escreva dados em um arquivo CSV. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.​

import csv
with open('./teste.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(["Nome", "Idade", "Cidade"])
    writer.writerow(['João', '30', 'Pindamonhangaba' ])
    writer.writerow(['José', '27', 'Tartarugalzinho'])
    writer.writerow(['Pedro', '20', 'Xique-Xique'])

    