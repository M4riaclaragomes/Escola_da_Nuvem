import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        par = f"{moeda}BRL"
        if par in dados:
            info = dados[par]
            print("Moeda:", info["name"])
            print("Valor atual:", info["bid"])
            print("Valor máximo:", info["high"])
            print("Valor mínimo:", info["low"])
            print("Última atualização:", info["create_date"])
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao consultar a cotação.")

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ")
consultar_cotacao(moeda)
