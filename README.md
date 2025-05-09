# 🦠 Health Analyzer – Detecção de Surtos de Dengue

Este é um projeto de análise de dados que detecta possíveis surtos de dengue a partir de dados semanais públicos. Utilizando Python e bibliotecas como Pandas, Statsmodels e Matplotlib, o sistema calcula médias móveis, variações semanais e exibe alertas de surto com base em critérios definidos.

## 📊 O que o projeto faz?

- Carrega dados semanais da dengue (formato CSV).
- Calcula a **média móvel de 3 semanas** e a **variação percentual** dos casos.
- Identifica possíveis **surtos de dengue** com base nos seguintes critérios:
  - Casos ≥ 30% acima da média geral
  - Variação semanal ≥ 30%
- Exibe os alertas detectados em tabela no terminal.
- Gera gráficos com a **tendência dos casos** ao longo do tempo.

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/health-analyzer.git
cd health-analyzer
````

### 2. Crie e ative um ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # No macOS/Linux
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o projeto

```bash
python3 -m app.main
```

---

## 📈 Exemplo de saída no terminal

```
Dados carregados com sucesso!

Métricas calculadas:
        SE  casos  media_movel   variacao
13  202514    199   220.000000 -18.10
14  202515    110   184.000000 -44.72
...

🔴 Alertas de surto:
+----+--------+---------+------------+
|    |     SE |   casos |   variacao |
+====+========+=========+============+
|  6 | 202507 |     228 |   14.0     |
| 10 | 202511 |     217 |   48.63    |
+------------------------------------+
```

---

## 🧪 Requisitos e dependências

As principais bibliotecas usadas incluem:

* `pandas`
* `matplotlib`
* `statsmodels`
* `tabulate`
* `fastapi` (opcional, para futura API)

Todas estão listadas em `requirements.txt`.

---

## 📌 Observações

* Os dados utilizados são públicos, baixados do site [InfoDengue](https://info.dengue.mat.br/).
* Atualmente, o sistema roda localmente no terminal. Uma versão com API (FastAPI) pode ser implementada no futuro.

---

## 🤝 Contribuição

Sugestões, melhorias e colaborações são bem-vindas! Este projeto tem fins educacionais e sociais, com foco em aprendizado e utilidade pública.

---

## 🧑‍💻 Autor

**Adeilton Barros**

