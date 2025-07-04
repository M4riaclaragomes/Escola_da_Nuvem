import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" in dados:
            print("CEP inválido.")
        else:
            print("Logradouro:", dados.get("logradouro", "N/A"))
            print("Bairro:", dados.get("bairro", "N/A"))
            print("Cidade:", dados.get("localidade", "N/A"))
            print("Estado:", dados.get("uf", "N/A"))
    else:
        print("Erro ao consultar o CEP.")

cep = input("Digite o CEP (somente números): ")
consultar_cep(cep)
