from fastapi import APIRouter
from app.utils.data_handler import carregar_dados_csv
from config import CSV_PATH

router = APIRouter()

@router.get("/analise/dengue")
def analisar_dados():
    try:
        df = carregar_dados_csv(CSV_PATH)

        total_casos = df["casos"].sum()
        media_semanal = df["casos"].mean()
        rt_medio = df["Rt"].mean()
        transmissao_ativa = df[df["transmissao"] == 1].shape[0]

        return {
            "total_casos": int(total_casos),
            "media_casos_semanais": round(media_semanal, 2),
            "Rt_medio": round(rt_medio, 2),
            "semanas_com_transmissao_ativa": transmissao_ativa,
            "periodo_inicio": df["data_iniSE"].min().strftime("%Y-%m-%d"),
            "periodo_fim": df["data_iniSE"].max().strftime("%Y-%m-%d"),
        }

    except Exception as e:
        return {"erro": str(e)}
