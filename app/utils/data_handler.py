# app/utils/data_handler.py
import os
import pandas as pd

def carregar_dados_csv(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        raise FileNotFoundError(f"O arquivo não foi encontrado: {caminho_arquivo}")
    df = pd.read_csv(caminho_arquivo)
    df["data_iniSE"] = pd.to_datetime(df["data_iniSE"])
    return df
