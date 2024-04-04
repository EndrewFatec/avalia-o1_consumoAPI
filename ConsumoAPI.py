import requests
 
 
Raca_nome = input("Digite o nome da raça de cachorro: ")
url = f"https://api.thedogapi.com/v1/breeds/search?q={Raca_nome}"
response = requests.get(url)
info = response.json()
 
 
if response.status_code == 200:
          info=info[0]
          print("Nome da raça: :",info['name'])
          print("Peso :", info['weight'])
          print("Objetivo:",info['bred_for'])
          print("Expectativa de Vida:",info['life_span'])
else:
          print("Erro ao achar um site")
 