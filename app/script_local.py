from services.api_client import fetch_data
from utils.data_handler import process_data
from visualization.graph_generator import generate_graph

def main():
    # Fazendo a requisição para pegar os dados da API
    data = fetch_data()
    
    if data:
        print("Dados recebidos com sucesso!")
        
        # Processando os dados
        processed_data = process_data(data)
        print("Dados processados:", processed_data)
        
        # Gerando o gráfico com os dados processados
        generate_graph(processed_data)

if __name__ == "__main__":
    main()
