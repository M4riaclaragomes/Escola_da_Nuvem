# 3- Crie um script em Python que leia um arquivo CSV e exiba os dados na tela. O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.

import csv
with open('./teste.csv') as csvfile:
    reader = csv.reader(csvfile)
    for x in reader:
      print(x)