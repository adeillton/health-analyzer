import matplotlib.pyplot as plt

def gerar_grafico_tendencia(df, cidade="Recife"):
    plt.figure(figsize=(12, 6))
    plt.plot(df["data_iniSE"], df["casos"], label="Casos Notificados", marker='o')
    plt.plot(df["data_iniSE"], df["media_movel"], label="Média Móvel (3 semanas)", linestyle='--')
    plt.title(f"Tendência de Casos de Dengue - {cidade}")
    plt.xlabel("Data (início da semana)")
    plt.ylabel("Número de casos")
    plt.legend()
    plt.grid(True)

    # ✅ Solução: rotacionar os rótulos do eixo X
    plt.xticks(rotation=45)  # você pode testar com 60 ou 90 também se precisar
    plt.tight_layout()  # ajusta automaticamente o layout
    plt.show()
