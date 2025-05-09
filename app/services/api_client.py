import requests

def fetch_data():
    url = 'https://dados.saude.go.gov.br/en/api/3/action/datastore_search?resource_id=6e0a083a-ed94-42bf-8778-b882a831332e&limit=50'
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Vai levantar uma exceção se o status code não for 2xx
        return response.json()  # Retorna os dados em formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar os dados: {e}")
        return None
