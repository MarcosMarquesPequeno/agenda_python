import requests

url = "https://www.globo.com"
response = requests.get(url)
print(f"Solicitacao HTTP para {url} retornou o status {response.status_code}")
