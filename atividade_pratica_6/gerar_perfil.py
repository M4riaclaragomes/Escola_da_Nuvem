import requests

def gerar_perfil():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        print("Nome:", nome)
        print("Email:", email)
        print("País:", pais)
    else:
        print("Erro ao obter os dados do usuário.")

gerar_perfil()
