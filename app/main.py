from fastapi import FastAPI
from app.utils.analyzer import carregar_dados_dengue, calcular_media_movel, detectar_surtos
from app.visualization.graph_generator import gerar_grafico_tendencia

def analisar_dados():
    caminho_csv = "app/data/dados_recife.csv"
    df = carregar_dados_dengue(caminho_csv)
    
    if df is not None:
        df = calcular_media_movel(df)
        df = detectar_surtos(df)
        gerar_grafico_tendencia(df)  # Mantém sua geração de gráfico original
        
        if 'possivel_surto' in df.columns:
            surtos = df[df['possivel_surto']]
            print("\n🔴 Alertas de surto:")
            print(surtos[['SE', 'casos', 'variacao']].to_markdown(tablefmt="grid"))
        else:
            print("\n✅ Nenhum surto detectado")

if __name__ == "__main__":
    analisar_dados()

app = FastAPI(title="Health Monitor", version="1.0")

@app.get("/")
def status():
    return {"status": "operacional"}