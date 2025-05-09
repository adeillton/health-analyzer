import pandas as pd

def carregar_dados_dengue(caminho_arquivo):
    """Carrega e prepara os dados da dengue."""
    try:
        df = pd.read_csv(caminho_arquivo)
        if 'casos' not in df.columns or 'SE' not in df.columns:
            print("Erro: Colunas 'casos' ou 'SE' não encontradas")
            return None
        print("Dados carregados com sucesso!")
        return df.sort_values('SE').reset_index(drop=True)
    except Exception as e:
        print(f"Erro ao carregar dados: {e}")
        return None

def calcular_media_movel(df, janela=3):
    """Calcula métricas temporais."""
    if df is None or df.empty:
        return df
        
    df = df.copy()
    df["media_movel"] = df["casos"].rolling(window=janela, min_periods=1).mean()
    df["variacao"] = df["casos"].pct_change() * 100  # Variação percentual
    
    print("\nMétricas calculadas:")
    print(df[['SE', 'casos', 'media_movel', 'variacao']].tail())
    return df

def detectar_surtos(df, fator=1.3, variacao_minima=30):
    """Detecta surtos com múltiplos critérios."""
    if df is None or df.empty:
        return df

    df = df.copy()
    media = df["casos"].mean()
    
    # Critérios combinados
    df['surto_limiar'] = df["casos"] > (media * fator)
    df['surto_variacao'] = df["variacao"] > variacao_minima
    df['possivel_surto'] = df['surto_limiar'] | df['surto_variacao']
    
    print(f"\nCritérios: Média={media:.1f} | Limiar>={media*fator:.1f} | Variação>={variacao_minima}%")
    return df

def analisar_dados(municipios, codigos):
    """Analisa municípios para surtos e subnotificação."""
    alertas = []
    municipio_dict = {}

    for municipio, codigo in zip(municipios, codigos):
        if municipio not in municipio_dict:
            municipio_dict[municipio] = []
        
        if codigo == "Desconhecido" or not isinstance(codigo, (int, str)):
            codigo = 0
        elif isinstance(codigo, str):
            try:
                codigo = int(codigo)
            except ValueError:
                codigo = 0
        
        municipio_dict[municipio].append(codigo)

    for municipio, lista_codigos in municipio_dict.items():
        total = len(lista_codigos)
        positivos = sum(lista_codigos)

        if total >= 5 and positivos / total > 0.6:
            alertas.append({
                "municipio": municipio,
                "tipo": "Possível surto",
                "detalhes": f"{positivos} de {total} casos positivos."
            })
        elif total >= 5 and positivos <= 1:
            alertas.append({
                "municipio": municipio,
                "tipo": "Possível subnotificação",
                "detalhes": f"Apenas {positivos} de {total} casos positivos."
            })

    if not alertas:
        print("Nenhum alerta gerado. Verifique os dados.")
    else:
        print(f"Alertas gerados: {len(alertas)}")

    return alertas

if __name__ == "__main__":
    caminho_arquivo = 'app/data/dados_recife.csv'

    df = carregar_dados_dengue(caminho_arquivo)

    if df is not None:
        df = calcular_media_movel(df)
        df = detectar_surtos(df)

        if 'possivel_surto' in df.columns:
            print("Processamento concluído com sucesso!")
            print("\nSemanas com possível surto detectado:")
            print(df[df['possivel_surto']][['SE', 'casos', 'media_movel', 'variacao']])
        else:
            print("A coluna 'possivel_surto' não foi criada.")

        # Exemplo: análise de municípios
        municipios = ['Recife', 'Olinda', 'Jaboatão']
        codigos = ['5', '1', 'Desconhecido']

        alertas = analisar_dados(municipios, codigos)
        print("\nAlertas detectados:", alertas)
