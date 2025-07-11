# 4- Crie um script em Python que leia e escreva dados em um arquivo JSON. O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.​

import json

pessoa = {
    "nome": "Carlos",
    "idade": 30,
    "cidade": "Xique-Xique"
}

with open("dados.json", "w", encoding="utf-8") as file:
    json.dump(pessoa, file, ensure_ascii=False, indent=4)

with open("dados.json", 'r', encoding='utf-8') as f:
    dados = json.load(f)

print(dados)